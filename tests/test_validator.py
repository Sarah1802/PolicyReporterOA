import unittest
from unittest.mock import patch
from src.context import Context
from src.states import S0, S1, S2
from src.binary_input_validator import BinaryInputValidator


class TestStateMachine(unittest.TestCase):

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
