def count_character_string(input_string: str, input_character: str) -> str:
    """
    function tack to count charter for string
    :param input_string: {str}  User Input String
    :param input_character: {str} USer Input Charter
    :return: {str}
    """
    if len(input_character) == 1:
        count = input_string.count(input_character)
        return "{} == {}".format(input_character, count)
    return "please enter only single character"


if __name__ == '__main__':
    user_input = input("Enter String: ")
    try:
        if not user_input:
            raise Exception("\033[1mString is not found! please enter valid string.")
        user_input_char = input("Enter single character: ").strip()
        if not user_input_char:
            raise Exception("\033[1mSingle Character is not found! please enter valid single Character")
    except Exception as error:
        print(error)
        sys.exit()
    print(count_character_string(user_input, user_input_char))
