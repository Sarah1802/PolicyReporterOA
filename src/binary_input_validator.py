class BinaryInputValidator:
    @staticmethod
    def is_valid(binary_str: str) -> bool:
        return isinstance(binary_str, str) and all(char in "01" for char in binary_str)
