import unittest
from pdf_txt_to_mp3.converter import extract_text_from_pdf, extract_text_from_txt

class TestConverter(unittest.TestCase):

    def test_extract_text_from_pdf(self):
        text = extract_text_from_pdf('sample.pdf')
        self.assertIsInstance(text, str)

    def test_extract_text_from_txt(self):
        text = extract_text_from_txt('sample.txt')
        self.assertIsInstance(text, str)

if __name__ == '__main__':
    unittest.main()