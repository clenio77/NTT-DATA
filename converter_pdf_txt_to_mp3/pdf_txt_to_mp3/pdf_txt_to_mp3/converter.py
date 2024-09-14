import PyPDF2
import pyttsx3
from gtts import gTTS

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def text_to_speech_pyttsx3(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()

def text_to_speech_gtts(text, output_path):
    tts = gTTS(text=text, lang='pt')
    tts.save(output_path)

def convert_file_to_mp3(file_path, output_path, use_gtts=False):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.txt'):
        text = extract_text_from_txt(file_path)
    else:
        raise ValueError('Formato de arquivo não suportado')

    if use_gtts:
        text_to_speech_gtts(text, output_path)
    else:
        text_to_speech_pyttsx3(text, output_path)
