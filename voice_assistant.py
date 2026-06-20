class VoiceAssistant(Assistant):

    def __init__(self):
        super().__init__()

        self.__assistant_name = "Jarvis"
        self.__version = "1.0"

        self.recognizer = sr.Recognizer()