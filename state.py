from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle_state(self, context, bit):
        pass

    @abstractmethod
    def get_remainder(self):
        pass
