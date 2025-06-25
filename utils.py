import fitz
def extract_text_from_pdf(uploaded_file):
    doc=fitz.open(stream=uploaded_file.read(),filetype="pdf")
    text=""
    for page in doc:
        text+=page.get_text()
    return text
