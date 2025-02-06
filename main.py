from context import Context
from states import S0
from binary_input_validator import BinaryInputValidator


def main():
    context = Context(S0())

    while True:
        binary_number = input("Enter binary number (or type 'exit' to quit): ")
        
        if binary_number.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if not BinaryInputValidator.is_valid(binary_number):
            print("Please enter a valid number.")
            continue
        
        context.get_remainder(binary_number)
        context.set_state(S0())
 
    


if __name__ == "__main__":
    main()
