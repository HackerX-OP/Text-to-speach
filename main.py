import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    say = input("Enter what you want to say: ")
    speak(say)
    if say == "exit":
        break
