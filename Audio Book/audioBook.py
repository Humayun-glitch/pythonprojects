import pyttsx3

book=open(r"book.txt")

bookText=book.readlines()

engine = pyttsx3.init()

for i in bookText:
    engine.say(i)
    engine.runAndWait()
