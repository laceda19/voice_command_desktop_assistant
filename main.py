from voice_assistant import VoiceAssistant
from text_assistant import TextAssistant


print("1 - Voice Assistant")
print("2 - Text Assistant")

choice = input("Choose assistant: ")

if choice == "1":
    assistant = VoiceAssistant()
else:
    assistant = TextAssistant()


assistant.speak("Assistant started")

while True:

    command = assistant.listen()

    if command == "":
        continue

    assistant.execute_command(command)

    if "exit" in command:
        break