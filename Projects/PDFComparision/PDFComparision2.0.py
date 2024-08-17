import PyPDF2

def extract_text_from_pdf(file_name):
    """Extract text from a PDF file."""
    try:
        with open(file_name, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_name}: {e}")
        return None

def compare_pdf_content(file_name1, file_name2):
    """Compare the text content of two PDF files."""
    text1 = extract_text_from_pdf(file_name1)
    text2 = extract_text_from_pdf(file_name2)
    
    if text1 is None or text2 is None:
        print("Could not compare files due to an error.")
        return
    
    if text1 == text2:
        print("The text content of the PDF files is identical.")
    else:
        print("The text content of the PDF files is not identical.")

# Example usage
compare_pdf_content("PD1.pdf", "PD3.pdf")
