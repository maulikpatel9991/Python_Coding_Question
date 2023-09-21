import sys
from typing import Any


def student_information(student_list: list) -> list[Any]:
    """
    function to tack student details sort first name , last name, roll no
    :param student_list: {list}     User input list
    :return: {list[Any]}
    """
    print("1.student information sort by first name \n"
          "2.student information sort by last name \n"
          "3.student information sort by roll-no ")
    user_option = int(input("choose any options: "))
    if not user_option in range(1, 4):
        raise Exception("Selected options is not found! Please Select Valid Options.")
    if user_option == 1:
        print("sort by First Name")
        return sorted(student_list, key=lambda i: i['first'])
    elif user_option == 2:
        print("sort by Last Name")
        return sorted(student_list, key=lambda i: i['last'])
    print("sort by Roll No")
    return sorted(student_list, key=lambda i: i['roll'])


if __name__ == '__main__':
    user_dict = {}
    student_details_list = []
    try:
        student_input = int(input("Enter Student Information add "))
        if student_input < 0:
            raise Exception("\033[1mAdd Student Information not found! please Enter Valid Positive integer Number")
        for value in range(student_input):
            first_name = input("Enter First Name: ")
            if not first_name.isalpha():
                raise Exception("\033[1mFirst Name is not found! Please Enter valid First Name.")
            last_name = input("Enter Last Name: ")
            if not last_name.isalpha():
                raise Exception("\033[1mLast Name is Not found! Please Enter Valid Last Name.")
            roll_no = int(input("Enter Roll-No: "))
            print(user_dict)
            user_dict['first'] = first_name
            user_dict['last'] = last_name
            user_dict['roll'] = roll_no
            student_details_list.append(user_dict.copy())
    except ValueError:  # If user input is not an integer than value error exception will occur
        print("\033[1mPlease enter valid integer number.")
        sys.exit()
    except Exception as error:
        print(error)
        sys.exit()
    print(student_details_list)
    print(student_information(student_details_list))
