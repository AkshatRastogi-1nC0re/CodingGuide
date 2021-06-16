import pyttsx3
import speech_recognition as sr
import pyperclip
import pyautogui

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.runAndWait()
    engine.stop()

engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"

    return query

if __name__ == "__main__":

    while True:

        query = takecommand().lower()

        if "function in python" in query:
            x = 'def sample(a,b):\n\tsam = a+b\n\treturn sam'
            pyperclip.copy(text=x)
            speak("okay")
            pyautogui.hotkey('ctrl', 'v', interval=0.15)

        elif "class in python" in query:
            x = 'class Sample:\n\tdef __init__(self, a, b):\n\t\ta = a\n\t\tb = b'
            pyperclip.copy(text=x)
            speak("okay")
            pyautogui.hotkey('ctrl', 'v', interval=0.15)

        elif "edit text in android" in query:
            x = '<TextView\n\tandroid:layout_width="wrap_content"\n\tandroid:layout_height="wrap_content"\n\tandroid:layout_marginStart="30dp"\n\tandroid:layout_marginEnd="30dp"\n\tandroid:layout_marginTop="50dp"\n\tandroid:gravity="center"\n\tandroid:text="Enter Customer ID"\n\tandroid:textColor="@color/colorTextPrimary"\n\tandroid:textSize="14sp"/>'
            pyperclip.copy(text=x)
            speak("okay")
            pyautogui.hotkey('ctrl', 'v', interval=0.15)
        
        elif "indent in android" in query:
            x = 'Intent registerIntent = new Intent(SampleActivity1.this, SampleActivity2.class);\nSplashScreen.this.startActivity(registerIntent);'
            pyperclip.copy(text=x)
            speak("okay")
            pyautogui.hotkey('ctrl', 'v', interval=0.15)
        
        elif "declare a button in android" in query:
            x = 'final Button button1 = findViewById(R.id.sampleid);'
            pyperclip.copy(text=x)
            speak("okay")
            pyautogui.hotkey('ctrl', 'v', interval=0.15)
        
        elif "declare an edit text in android" in query or "declare a edit text in android" in query:
            x = 'final EditText et1 = findViewById(R.id.sampleid)'
            pyperclip.copy(text=x)
            speak("okay")
            pyautogui.hotkey('ctrl', 'v', interval=0.15)
        
        elif "declare an image in android" in query:
            x = 'final Image im1 = findViewById(R.id.sampleid)'
            pyperclip.copy(text=x)
            speak("okay")
            pyautogui.hotkey('ctrl', 'v', interval=0.15)

        if "break" in query:
            break

