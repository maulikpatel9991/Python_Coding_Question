"""
Write a Python function to insert a string in the middle of a string.
"""
import sys


def insert_string(main_string: str, new_string: str) -> str:
    """
    function to tack insert middle of string
    :param main_string: {str}   First input string
    :param new_string: {str}    second input string
    :return: {str}
    """
    '''
    if condition check odd or even 
    if condition is even part
    '''
    if len(main_string) % 2 == 0:
        size = int(len(main_string) // 2)
        update_string = main_string[:size] + "{}".format(new_string) + main_string[size:]
        return "string is even , new string: {}".format(update_string)
    size = int(len(main_string) // 2)
    update_string = main_string[:size] + "{}".format(new_string) + main_string[size + 1:]
    return "String is ODD new string is: {}".format(update_string)


if __name__ == '__main__':
    user_input = input("please enter the string: ").strip()
    try:
        if not user_input or len(user_input) < 2:
            raise Exception("\033[1mEnter string should be length more then two.Please enter a valid string")
        new_input = input("please enter one more string that you want to insert: ").replace(" ", "")
        if not new_input:
            raise Exception("\033[1mInsert String Not found! Please enter Valid Insert String")
    except Exception as error:
        print(error)
        sys.exit()
    print(insert_string(user_input, new_input))
