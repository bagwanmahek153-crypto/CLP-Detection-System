import speech_recognition as sr


def get_voice_input():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio)
        return text.lower()

    except sr.WaitTimeoutError:
        return "timeout"

    except sr.UnknownValueError:
        return "unknown"

    except sr.RequestError:
        return "error"

    except Exception:
        return "error"