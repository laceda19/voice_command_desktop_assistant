from assistant import Assistant


class TextAssistant(Assistant):

    def listen(self):

        command = input("Enter command: ").lower()

        return command

    def execute_command(self, command):

        self.speak(f"You typed: {command}")