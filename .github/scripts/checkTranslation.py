import sys
import os
import xml.etree.ElementTree as ET
import polib


def normalize(s: str) -> str:
    # Normalize strings for reliable comparison (trim, lowercase, collapse spaces)
    return " ".join((s or "").strip().lower().split())


# -----------------------------
# PO FILE CHECK
# -----------------------------
def checkPo(path: str) -> float:
    # Parse PO file using polib
    po = polib.pofile(path)

    translated = 0
    total = 0

    for entry in po:
        # Skip empty msgid entries
        if not entry.msgid.strip():
            continue

        total += 1

        # Consider entry translated only if msgstr differs from msgid
        if entry.msgstr and normalize(entry.msgstr) != normalize(entry.msgid):
            translated += 1

    return translated / total if total else 0.0


# -----------------------------
# XLIFF CHECK (skeleton-safe generic parsing)
# -----------------------------
def checkXliff(path: str) -> float:
    # Parse XML XLIFF file
    tree = ET.parse(path)
    root = tree.getroot()

    translated = 0
    total = 0

    source = None

    for elem in root.iter():

        # Capture source segments
        if elem.tag.endswith("source"):
            source = normalize(elem.text)

        # Compare with target segments
        elif elem.tag.endswith("target"):
            target = normalize(elem.text)

            if source:
                total += 1

                # Count as translated only if target differs from source
                if target and target != source:
                    translated += 1

    return translated / total if total else 0.0


# -----------------------------
# MAIN ENTRY POINT
# -----------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage: checkTranslation.py <file>")
        sys.exit(2)

    path = sys.argv[1]

    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(2)

    ext = os.path.splitext(path)[1].lower()

    # Dispatch based on file type
    if ext == ".po":
        ratio = checkPo(path)

    elif ext in [".xliff", ".xlf"]:
        ratio = checkXliff(path)

    else:
        print(f"Unsupported file type: {ext}")
        sys.exit(2)

    print(f"translation_ratio={ratio}")

    # Threshold: consider file translated if above 5%
    if ratio > 0.05:
        sys.exit(0)  # translated
    else:
        sys.exit(1)  # not translated


if __name__ == "__main__":
    main()