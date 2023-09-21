"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return "Empty String"
"""
import sys


def split(number: str) -> str:
    """
    function to tack split to string
    :param number: {str}    input string
    :return: {str}
    """
    if len(number) > 2:
        return "{} is first character is {} last character is {}".format(number, number[0:2], number[-2:])
    return "{} is Empty String. Please Enter String length of Greater-than two".format(number)


if __name__ == '__main__':
    user_input = input("Please enter the string: ").strip()
    try:
        if not user_input:
            raise Exception("\033[1mString does not Found! please enter a valid String.")
    except Exception as error:
        print(error)
        sys.exit()
    print(split(user_input))
