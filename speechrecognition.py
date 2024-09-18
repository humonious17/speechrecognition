import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your command...")

        # Listen to the audio and store it
        audio = recognizer.listen(source)

        try:
            # Convert audio to text using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    recognize_speech()
