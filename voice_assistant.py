class VoiceAssistant(Assistant):

    def __init__(self):
        super().__init__()

        self.__assistant_name = "Jarvis"
        self.__version = "1.0"

        self.recognizer = sr.Recognizer()

    def listen(self):

        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=0.3)

            try:
                audio = self.recognizer.listen(source, timeout=5)

                command = self.recognizer.recognize_google(audio).lower()

                print(f"✅ YOU SAID: {command}")

                return command

            except:
                return ""
