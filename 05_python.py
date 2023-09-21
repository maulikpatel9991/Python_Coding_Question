def swap_number(number1: int, number2: int) -> str:
    """
    swap to number
    :param number1: {int}   first input
    :param number2: {int}   second input
    :return: {str}
    """
    number2, number1 = number1, number2
    return "number one is: {} & second Number is: {}".format(number1, number2)


if __name__ == '__main__':
    try:
        first_number = int(input("Enter First Number: "))
        second_number = int(input("Enter Second Number: "))
    except ValueError:
        print("\033[1mNumber does not Found! Both values have to be integers.")
        sys.exit()
    print(swap_number(first_number, second_number))
