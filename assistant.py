from abc import ABC, abstractmethod

class Assistant(ABC):

    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        ...

    @abstractmethod
    def listen(self):
        pass

    @abstractmethod
    def execute_command(self, command):
        pass