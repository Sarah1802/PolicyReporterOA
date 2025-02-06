from src.state import State

class S0(State):
    """
    Represents the state S0 in the State Design Pattern.

    This state transitions based on the input bit:
    - If the input is "1", it transitions to S1.
    - If the input is "0", it remains in S0.

    Attributes:
        REMAINDER (int): The remainder value associated with this state.
    """

    REMAINDER = 0

    def handle_state(self, context, bit):
        """Transitions the context to the appropriate next state."""
        if bit == "1":
            context.set_state(S1())
        else:
            context.set_state(S0())

    def get_remainder(self):
        """Returns the remainder value for this state."""
        return self.REMAINDER


class S1(State):
    """
    Represents the state S1 in the State Design Pattern.

    This state transitions based on the input bit:
    - If the input is "1", it transitions to S0.
    - If the input is "0", it transitions to S2.

    Attributes:
        REMAINDER (int): The remainder value associated with this state.
    """

    REMAINDER = 1

    def handle_state(self, context, bit):
        """Transitions the context to the appropriate next state."""
        if bit == "1":
            context.set_state(S0())
        else:
            context.set_state(S2())

    def get_remainder(self):
        """Returns the remainder value for this state."""
        return self.REMAINDER


class S2(State):
    """
    Represents the state S2 in the State Design Pattern.

    This state transitions based on the input bit:
    - If the input is "0", it transitions to S1.
    - If the input is "1", it remains in S2.

    Attributes:
        REMAINDER (int): The remainder value associated with this state.
    """

    REMAINDER = 2

    def handle_state(self, context, bit):
        """Transitions the context to the appropriate next state."""
        if bit == "0":
            context.set_state(S1())
        else:
            context.set_state(S2())

    def get_remainder(self):
        """Returns the remainder value for this state."""
        return self.REMAINDER
