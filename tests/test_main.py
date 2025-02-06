import unittest
from unittest.mock import patch
from context import Context
from states import S0, S1, S2
from binary_input_validator import BinaryInputValidator


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
        self.assertIsInstance(self.context.state, S0)  # Ensure state has changed

        bit = "1"
        self.s0.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S1)  # Ensure state has changed
    
    def test_S1_state_transition(self):
        bit = "0"
        self.s1.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S2)  # Ensure state has changed

        bit = "1"
        self.s1.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S0)  # Ensure state has changed

    def test_S2_state_transition(self):
        bit = "0"
        self.s2.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S1)  # Ensure state has changed

        bit = "1"
        self.s2.handle_state(self.context, bit)
        self.assertIsInstance(self.context.state, S2)  # Ensure state has changed
    
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

    def test_invalid_input(self):       
        user_input = "   "
        self.assertFalse(BinaryInputValidator.is_valid(user_input))

        user_input = " 1 1  0"
        self.assertFalse(BinaryInputValidator.is_valid(user_input))
  
        user_input = "%$!^*1001"
        self.assertFalse(BinaryInputValidator.is_valid(user_input))

        user_input = "%$!^*1001"
        self.assertFalse(BinaryInputValidator.is_valid(user_input))

        user_input = "18921001"
        self.assertFalse(BinaryInputValidator.is_valid(user_input))
    
    def test_valid_input(self):
        user_input = "111111"
        self.assertTrue(BinaryInputValidator.is_valid(user_input))

        user_input = "0000000"
        self.assertTrue(BinaryInputValidator.is_valid(user_input))

        user_input = "000010011"
        self.assertTrue(BinaryInputValidator.is_valid(user_input))





    


if __name__ == "__main__":
    unittest.main()
