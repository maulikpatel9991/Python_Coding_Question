""""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged."
"""
import sys


def check(number: str) -> str:
    """
    function to tack add and remove string
    :param number: {list}    user input string
    :return: {str}
    """
    if len(number) > 3:
        if number.lower().endswith("ing"):
            input_check = number.replace("ing", "ly")
            return "{}".format(input_check)
        input_check = "".join([number, "ing"])
        return input_check
    return "leave it unchanged"
