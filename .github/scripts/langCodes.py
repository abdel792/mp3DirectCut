import sys

# Mapping between Crowdin language IDs (keys) and standard NVDA directory names (values).
# This dictionary acts as the symmetrical counterpart to 'languageMappings.json' implemented by @nvdaes.
# It ensures that translations exported from Crowdin are stored in the correct
# local paths (e.g., 'es-ES' from Crowdin goes into the 'es' folder).
CROWDIN_TO_NVDA = {
	# Arabic variants
	"ar-SA": "ar_SA",
	# Spanish variants
	"es-ES": "es",
	"es-CO": "es_CO",
	# Portuguese variants
	"pt-BR": "pt_BR",
	"pt-PT": "pt_PT",
	# Chinese variants
	"zh-CN": "zh_CN",
	"zh-HK": "zh_HK",
	"zh-TW": "zh_TW",
	# Other specific mappings from the NVDA ecosystem
	"af": "af_ZA",
	"de-CH": "de_CH",
	"nb": "nb_NO",
	"nn-NO": "nn_NO",
	"sr-CS": "sr",
}


def get_nvda_code(crowdin_code):
	"""
	Returns the appropriate local directory name for a given Crowdin language ID.

	Args:
	    crowdin_code (str): The language identifier from Crowdin (e.g., 'pt-BR', 'fr').

	Returns:
	    str: The corresponding NVDA locale folder name (e.g., 'pt_BR', 'fr').
	"""
	# 1. Direct check in our verified map (Priority)
	if crowdin_code in CROWDIN_TO_NVDA:
		return CROWDIN_TO_NVDA[crowdin_code]

	# 2. Automated conversion for regional variants: Crowdin "xx-YY" -> NVDA "xx_YY"
	# This handles regional codes not explicitly defined in the map.
	if "-" in crowdin_code:
		return crowdin_code.replace("-", "_")

	# 3. Default: Return as is.
	# This covers base languages that don't use regional folders in NVDA
	# (e.g., 'fr', 'tr', 'bg', 'fi', 'fa').
	return crowdin_code


if __name__ == "__main__":
	# Ensure a language code was provided as a command-line argument
	if len(sys.argv) > 1:
		# Standardize input and output the mapped code for PowerShell to capture
		print(get_nvda_code(sys.argv[1]))
