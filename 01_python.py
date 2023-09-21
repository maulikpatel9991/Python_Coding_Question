def arguments_input(args) -> None:
    """
    Function To Tack user input arguments print
    :param args: str, user input
    :return: None
    """
    for element in args:
        print(element)


if __name__ == '__main__':
    arguments_user = []
    try:
        number_arguments = int(input("please enter no. of arguments: "))
        if number_arguments <= 0:
            raise Exception("\033[1mPlease enter a valid positive Integer value")
        for row in range(number_arguments):
            user_input = input("please enter {} value: ".format(row + 1))
            if not user_input:
                raise Exception("\033[1mValue does not found! please Enter Valid Value.")
            arguments_user.append(user_input)
        arguments_input(arguments_user)
    except ValueError:
        print("\033[1mArguments does not found!Please Enter Integer number")
    except Exception as error:
        print(error)
