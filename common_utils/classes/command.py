# This is the abstract class that every command
# has to extends in order to inherited the command's
# common attributes and functionalities
from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, name: str, label: str):
        self.name = name
        self.label = label
        
    @abstractmethod
    def run(self, update, context):
        pass