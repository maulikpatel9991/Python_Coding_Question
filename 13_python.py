"""
Read a sentence from the standard input. Find out how many times each word appear in given string.
1. Input : This is a Python learning
2. Output :
This 1
Is  1
a 1
Python 1
Learning 1
"""
import sys


def word_appear(user_input: list) -> None:
    """
    function to tack word appear in given string
    :param user_input: {list}    user input string
    :return: None
    """
    """
    first convert in set why set not store duplicated value
    
    """
    user_input_set = set(user_input)
    for value in user_input_set:
        print("{} {}".format(value, user_input.count(value)))


if __name__ == '__main__':
    input_string = input("Enter Input: ").strip()
    try:
        if not input_string:
            raise Exception("\033[1mInput String does not Found! please enter a valid String.")
    except Exception as error:
        print(error)
        sys.exit()
    list_input = input_string.split(" ")
    word_appear(list_input)
