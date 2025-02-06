import unittest
from unittest.mock import patch
from src.context import Context
from src.states import S0, S1, S2
from src.binary_input_validator import BinaryInputValidator


class TestStateMachine(unittest.TestCase):

    def setUp(self):
        """Set up the test case with a fresh Context."""
        self.context = Context(S0())
        self.s0 = S0()
        self.s1 = S1()
        self.s2 = S2()

    def test_initial_state(self):
        """Test that the initial state is S0."""
        self.assertIsInstance(self.context.state, S0)

    def test_S0_state_transition(self):
        bit = "0"
        self.s0.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S0)  

        bit = "1"
        self.s0.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S1)  
    
    def test_S1_state_transition(self):
        bit = "0"
        self.s1.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S2)  

        bit = "1"
        self.s1.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S0)  

    def test_S2_state_transition(self):
        bit = "0"
        self.s2.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S1)  

        bit = "1"
        self.s2.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S2)  

if __name__ == "__main__":
    unittest.main()
