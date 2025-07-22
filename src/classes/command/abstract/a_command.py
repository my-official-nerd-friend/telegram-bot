# This is the abstract class that every command
# has to extends in order to inherited the command's
# common attributes and functionalities
from abc import ABC, abstractmethod

from src.auth.decorator import require_authorized_user

class ACommand(ABC):
    def __init__(self, name: str, label: str, ):
        self.name = name
        self.label = label
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if 'run' in cls.__dict__:
            original_run = cls.__dict__['run']
            cls.run = require_authorized_user(original_run)
        
    @abstractmethod
    def run(self, update, context):
        pass