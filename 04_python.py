import sys
from typing import Any


def number_operations(number1: int, number2: int, operator: str) -> str | Any:
    """
    Arithmetic operation perform number_sum function
    :param number1: {int}   first input
    :param number2: {int}   second input
    :param operator: {str}  operator input
    :return: {str | Any}
    """
    try:
        output = eval("{}{}{}".format(number1, operator, number2))
        return output
    except ArithmeticError as ae:
        print("Invalid operations {}".format(ae))
        sys.exit()


if __name__ == '__main__':
    try:
        first_number = int(input("Enter First Number: "))
        second_number = int(input("Enter Second Number: "))
        operator_list = ['+', '*', '/', '**', '-', '%']
        print(operator_list)
        operator_input = input("Enter operator in above list: ")
        if not operator_input in operator_list:
            raise Exception("\033[1mArithmetic operation does not found! please Enter Valid arithmetic operation")
    except ValueError:
        print("\033[1mInput value does not Found! please enter a valid Integer number.")
        sys.exit()
    except Exception as error:
        print(error)
        sys.exit()
    print(number_operations(first_number, second_number, operator_input))
