# Akhbaar Padhke Sunaao

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.Spvoice")

    speak.Speak(str)

if __name__ == '__main__':
    speak("i am mister perfect coder and the best learning plateform on youtube channel code with harry")
