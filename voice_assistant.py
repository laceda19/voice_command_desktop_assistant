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

    def execute_command(self, command):

        if "open chrome" in command:
            os.system("start chrome")
            self.speak("Opening Chrome")

        elif "open calculator" in command:
            os.system("start calculator")
            self.speak("Opening Calculator")

        elif "open notepad" in command:
            os.system("start notepad")
            self.speak("Opening Notepad")

        elif "open paint" in command:
            os.system("mspaint")
            self.speak("Opening Paint")

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            self.speak("Opening YouTube")

        elif "open google" in command:
            webbrowser.open("https://google.com")
            self.speak("Opening Google")

