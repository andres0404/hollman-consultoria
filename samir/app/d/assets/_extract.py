import importlib, sys

mods = ['pypdf', 'fitz', 'pdfplumber', 'PyPDF2']
avail = [m for m in mods if importlib.util.find_spec(m) is not None]
print('AVAILABLE:', avail)

path = '/home/andres/hollman-consultoria/samir/app/d/assets/Hoja de Vida 2024- final.pdf'

text = None
for m in avail:
    try:
        if m == 'pypdf':
            from pypdf import PdfReader
            r = PdfReader(path)
            text = '\n'.join((p.extract_text() or '') for p in r.pages)
        elif m == 'PyPDF2':
            import PyPDF2
            r = PyPDF2.PdfReader(path)
            text = '\n'.join((p.extract_text() or '') for p in r.pages)
        elif m == 'fitz':
            import fitz
            d = fitz.open(path)
            text = '\n'.join(pg.get_text() for pg in d)
        elif m == 'pdfplumber':
            import pdfplumber
            with pdfplumber.open(path) as pdf:
                text = '\n'.join((pg.extract_text() or '') for pg in pdf.pages)
        if text and text.strip():
            break
    except Exception as e:
        print('ERR', m, repr(e))
        text = None

if text:
    print('===TEXT_START===')
    print(text)
    print('===TEXT_END===')
else:
    print('NO_TEXT_EXTRACTED')
