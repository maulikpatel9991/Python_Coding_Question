"""
Write a Python function to remove the characters which have odd index values of a given string.
"""
import sys


def remove_odd(number: str) -> str:
    """
    remover odd number for given string
    :param number: {str}    user input string
    :return: {str}
    """
    odd_string = number[::2]
    return "odd characters from input string: {}".format(odd_string)


if __name__ == '__main__':
    user_input = input("please enter the string: ").strip()
    try:
        if not user_input:
            raise Exception("\033[1mString does not Found! please enter a valid String.")
    except Exception as error:
        print(error)
        sys.exit()
    print(remove_odd(user_input))
