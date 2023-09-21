import sys


def largest_number(number1: int, number2: int) -> str:
    """
    Function Tack to large number to find
    :param number2: {int} first input user
    :param number1:  {int} second input user
    :return:    {str}
    """
    if number1 > number2:
        return "{} is larger than {}".format(number1, number2)
    elif number2 > number1:
        return "{} is larger than {}".format(number2, number1)
    return "Both Number are same"


if __name__ == '__main__':
    '''
    Input From User Two Int Number
    '''
    try:
        first_input_user = int(input("Enter First Number: "))
        second_input_user = int(input("Enter Second number: "))
    except ValueError:
        print("\033[1mNumber does not Found! please enter Both values have to be integers.")
        sys.exit()
    print(largest_number(first_input_user, second_input_user))
