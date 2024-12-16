from markitdown import MarkItDown

markitdown = MarkItDown()
result = markitdown.convert("tests/data/URS_Hazardous_Substance_Master.docx")

with open("tests/data/output.md", "w") as file:
    file.write(result.text_content)