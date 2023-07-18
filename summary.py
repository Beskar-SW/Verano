from PyPDF2 import PdfReader
import os

class Summary:
    def __init__(self, file_path) -> None:
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            raise FileNotFoundError
        self.reader = PdfReader( open(self.file_path, 'rb'))
        self.num_pages = len(self.reader.pages)

    def extractText(self) -> str:
        text = ''
        for page in range(self.num_pages):
            text += self.reader.pages[page].extract_text()
        return text
    

# if __name__ == '__main__':
#     summary = Summary('CV_Johan_Franco_Rogel.pdf')
#     text = summary.extractText()
#     print(text)