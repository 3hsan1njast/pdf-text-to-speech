import PyPDF2
import pyttsx3

pdf_reader = PyPDF2.PdfReader(open('sample.pdf', 'rb'))
speaker = pyttsx3.init()

for page in pdf_reader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()
