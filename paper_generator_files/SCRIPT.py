from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
import logging
logging.basicConfig(level=logging.INFO)

def main():
    ## create document for extraction with configurations
    pdf_document = Document(
        document_path = r'C:\Users\Admin\OneDrive\Desktop\notes\EL\upsc\GENERAL_STUDIES_PAPER_II_2023.pdf',
        language='eng',
        )
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    print(content)

if __name__ == "__main__":
    main()