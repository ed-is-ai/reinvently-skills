import sys
from pypdf import PdfReader
print("\n".join(page.extract_text() or "" for page in PdfReader(sys.argv[1]).pages))
