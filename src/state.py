from abc import ABC, abstractmethod

class State(ABC):
    """
    An abstract base class representing a state in the State Design Pattern.

    This class defines the structure for concrete state implementations.  
    Each concrete state must implement the `handle_state` method to define 
    how the state transitions based on input, and the `get_remainder` method 
    to retrieve any relevant data associated with the state.
    """

    @abstractmethod
    def handle_state(self, context, bit):
        """Handles the state transition based on the given input."""
        pass

    @abstractmethod
    def get_remainder(self):
        """Returns state-specific data (e.g., remainder value)."""
        pass
