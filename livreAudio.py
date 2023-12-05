import pyttsx3
import PyPDF2
#pip install --upgrade PyPDF2==2.12.1
livre = open("IntroML_Azencott.pdf", "rb")

lecture = PyPDF2.PdfFileReader(livre)
pages = lecture.numPages
print(pages)

droid = pyttsx3.init()
debutlecture = lecture.getPage(2)
texte = debutlecture.extractText()

droid = pyttsx3.init()
droid.say(texte)
droid.runAndWait()