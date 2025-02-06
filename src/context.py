from src.state import State

class Context:
    """
    Manages state transitions within the State design pattern.

    The Context class maintains a reference to an instance of a State subclass
    and delegates state-specific behavior to it. The state can transition dynamically
    based on input.

    Attributes:
        state (State): The current state of the context.
    """
    
    def __init__(self, state: State):
        """
        Initializes the Context with an initial state.

        Args:
            state (State): The initial state of the context.
        """
        self.state = state  

    def set_state(self, state: State):
        """
            Updates the current state of the context.

            Args:
            state (State): The new state to transition to.
        """
        self.state = state
        print(state)

    def transitionState(self, bit):
        """
            Delegates state transition logic to the current state's handleState method.

            Args:
            bit (int): The input used to determine the next state transition.
        """
        self.state.handleState(self, bit) 
    
    def get_remainder(self, binary_number):
        """
            Computes the remainder of a binary number when divided by 3.

            Args:
            binary_string (str): A string consisting of '0' and '1' characters.

            Returns:
            int: The remainder when the binary number is divided by 3.    
        """   

        for bit in binary_number:
            self.state.handle_state(self, bit)

        remainder = self.state.REMAINDER
        return remainder
