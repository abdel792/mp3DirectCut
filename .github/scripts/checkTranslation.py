import sys
import os
from crowdin_api import CrowdinClient

def find_file_id(client, project_id, base_target, search_ext):
	"""
	Iterates through all project files (using pagination) to find the ID
	of the source file matching the target name and extension.
	"""
	offset = 0
	limit = 100

	while True:
		resp = client.source_files.list_files(
			projectId=project_id,
			limit=limit,
			offset=offset
		)

		data = resp['data']
		for f in data:
			path_crowdin = f['data']['path'].lower()
			# Check if the path ends with addon_id.pot or addon_id.xliff
			if path_crowdin.endswith(f"{base_target}{search_ext}"):
				file_id = f['data']['id']
				print(f"DEBUG: Match found: {path_crowdin} (ID: {file_id})")
				return file_id

		if len(data) < limit:
			break

		offset += limit

	return None

def get_score_from_api(file_name_to_search: str, lang_id: str) -> float:
	"""
	Retrieves the translation progress score for a specific language and file.
	Handles pagination for both file listing and language status.
	"""
	token = os.environ.get("crowdinAuthToken")
	p_id_env = os.environ.get("CROWDIN_PROJECT_ID")

	if not token or not p_id_env:
		print("ERROR: Missing environment variables 'crowdinAuthToken' or 'CROWDIN_PROJECT_ID'.")
		return 0.0

	client = CrowdinClient(token=token)
	p_id = int(p_id_env)

	try:
		# Clean and prepare search patterns
		# Example: 'addon/locale/fr/LC_MESSAGES/myaddon.po' -> base_target: 'myaddon'
		base_target = file_name_to_search.replace('\\', '/').split('/')[-1].rsplit('.', 1)[0].lower()
		ext_target = file_name_to_search.split('.')[-1].lower()

		# On Crowdin, the source for a .po file is usually a .pot file
		search_ext = ".pot" if ext_target == "po" else f".{ext_target}"

		print(f"DEBUG: Searching for source file: {base_target}{search_ext}")

		file_id = find_file_id(client, p_id, base_target, search_ext)

		if file_id is None:
			print(f"WARNING: File '{base_target}{search_ext}' not found on Crowdin.")
			return 0.0

		# Pagination for translation status (Progress)
		offset = 0
		limit = 100

		while True:
			resp = client.translation_status.get_file_progress(
				projectId=p_id,
				fileId=file_id,
				limit=limit,
				offset=offset
			)

			data = resp['data']
			for item in data:
				lang_api = item['data']['languageId']
				
				# Flexible matching (e.g., 'fr' will match 'fr' or 'fr-FR' from API)
				# Also handles underscore to dash conversion for Crowdin compatibility
				if lang_api.lower().startswith(lang_id.lower().replace('_', '-')):
					progress = float(item['data']['translationProgress'])
					return progress / 100

			# Check pagination total
			total = resp['pagination']['totalCount']
			if offset + limit >= total:
				break
			offset += limit

		print(f"DEBUG: Language '{lang_id}' not found in progress list for this file.")
		return 0.0

	except Exception as e:
		print(f"API ERROR: {e}")
		return 0.0

def main():
	if len(sys.argv) < 3:
		print("Usage: python checkTranslation.py <file_path> <lang_id>")
		sys.exit(2)

	input_file = sys.argv[1]
	lang = sys.argv[2]

	score = get_score_from_api(input_file, lang)

	# Output formatted for capture by the PowerShell script (crowdinSync.ps1)
	print(f"translationRatio={score}")

	if input_file.lower().endswith('.md'):
		print(f"mdScore={score}")
	else:
		print(f"poScore={score}")

	# Exit with success (0) if there is at least some translated content
	sys.exit(0 if score > 0.05 else 1)

if __name__ == "__main__":
	main()
