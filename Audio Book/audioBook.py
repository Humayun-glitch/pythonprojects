import pyttsx3

book=open(r"D:\Python Programs\Python Projects\book.txt")

bookText=book.readlines()

engine = pyttsx3.init()

for i in bookText:
    engine.say(i)
    engine.runAndWait()