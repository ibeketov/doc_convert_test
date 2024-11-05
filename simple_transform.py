from docling.document_converter import DocumentConverter

def main():
    source = "URS_Hazardous_Substance_Master.docx"  # document per local path or URL
    converter = DocumentConverter()
    result = converter.convert(source)
    print(result.document.export_to_markdown())
    # output: ## Docling Technical Report [...]"


if __name__ == "__main__":
    main()
