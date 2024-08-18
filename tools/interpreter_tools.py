from PyPDF2 import PdfReader
from langchain.tools import tool


class InterpreterTools:

    @tool("Convert PDF to text")
    def pdf_to_text_tool(file_path: str) -> str:
        """
        Convert PDF content to text.
        
        Args:
            file_path (str): The path to the PDF file.
        
        Returns:
            str: Extracted text from the PDF.
        """
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            return f"An error occurred while reading the PDF: {str(e)}"
        
