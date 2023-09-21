class Author:
    """
    Author class is programming language Author name
    """

    def __init__(self, author_name: str) -> None:
        """
        constructor for Author Class
        :param author_name: {str}   author name pass
        :return: None
        """
        self.author_name = author_name

    def author_name_call(self) -> None:
        """
        method print programming language author name
        :return: None
        """
        print("Author Name is {}".format(self.author_name))


class ProgrammingLanguage(Author):
    """
    define dictionary for programming language is key and
    Author name is value
    """
    language_author_dict = {
        'python': 'Guido van Rossum',
        'java': 'James A. Gosling',
        'c': 'Dennis Richie',
        'php': 'Rasmus Lerdorf'
    }

    def __init__(self, language_name: str) -> None:
        """
        constructor for ProgrammingLanguage Class
        :param language_name: {str}    language name
        """
        self.language_name = language_name
        super().__init__(self.language_author_dict[self.language_name])

    def language_name_print(self):
        """
        method tack to language name print
        :return: None
        """
        print("language name is {}".format(self.language_name))

    def language_author(self) -> str:
        """
        method to tack print language and author name
        :return: str
        """
        return "language selected name is {} author is {}".format(self.language_name,
                                                                  self.language_author_dict[self.language_name])


if __name__ == '__main__':
    print(ProgrammingLanguage.language_author_dict.keys())
    user_input = input("Enter programming language: ").lower().strip()
    if user_input in ProgrammingLanguage.language_author_dict:
        '''
        ProgrammingLanguage class object has create 
        '''
        language = ProgrammingLanguage(user_input)
        print(language.language_author())
    else:
        print("please select provided list of language {}".format(ProgrammingLanguage.language_author_dict.keys()))
