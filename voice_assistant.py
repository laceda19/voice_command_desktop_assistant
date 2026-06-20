class VoiceAssistant(Assistant):

    def __init__(self):
        super().__init__()

        self.__assistant_name = "Jarvis"
        self.__version = "1.0"

        self.recognizer = sr.Recognizer()

    # Getter methods
    def get_assistant_name(self):
        return self.__assistant_name

    def get_version(self):
        return self.__version



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

        elif "search" in command:

            search_term = command.replace("search", "")

            url = f"https://www.google.com/search?q={search_term}"

            webbrowser.open(url)

            self.speak(f"Searching {search_term}")

        elif "type" in command:

            text = command.replace("type", "")

            pyautogui.write(text, interval=0.05)

            self.speak("Typing completed")

        elif "move right" in command:
            pyautogui.moveRel(100, 0)

        elif "move left" in command:
            pyautogui.moveRel(-100, 0)

        elif "move up" in command:
            pyautogui.moveRel(0, -100)

        elif "move down" in command:
            pyautogui.moveRel(0, 100)

        elif "click" in command:
            pyautogui.click()

        elif "double click" in command:
            pyautogui.doubleClick()

        elif "right click" in command:
            pyautogui.rightClick()

        elif "scroll up" in command:
            pyautogui.scroll(500)

        elif "scroll down" in command:
            pyautogui.scroll(-500)

        elif "screenshot" in command:

            filename = f"screenshot_{int(time.time())}.png"

            screenshot = pyautogui.screenshot()

            screenshot.save(filename)

            self.speak("Screenshot taken")




