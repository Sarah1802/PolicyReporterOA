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
    
    def test_trivial_remainder(self):
        binary_number = "0"
        answer = 0
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S0)

        self.context.set_state(S0())
        binary_number = "1"
        answer = 1
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S1)

        self.context.set_state(S0())
        binary_number = "10"
        answer = 2
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S2)
    
    def test_small_cases(self):
        # Test binary representation of 12 -> remainder should be 0
        binary_number = "1100"
        answer = 0
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S0)

        # Test binary representation of 7 -> remainder should be 1
        self.context.set_state(S0())
        binary_number = "0111"
        answer = 1
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S1)

        # Test binary representation of 14 -> remainder should be 2
        self.context.set_state(S0())
        binary_number = "1110"
        answer = 2
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S2)
    
    def test_large_case(self):
         # Test binary representation of 67381920 -> remainder should be 0
        binary_number = "100000001000010101010100000"
        answer = 0
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S0)

        # Test binary representation of 89068 -> remainder should be 1
        self.context.set_state(S0())
        binary_number = "10101101111101100"
        answer = 1
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S1)

        # Test binary representation of 170688905 -> remainder should be 2
        self.context.set_state(S0())
        binary_number = "001010001011001000000110001001"
        answer = 2
        calculated_remainder = self.context.get_remainder(binary_number)
        self.assertEqual(calculated_remainder, answer)
        self.assertIsInstance(self.context.state, S2)





    


if __name__ == "__main__":
    unittest.main()
