import sys

if __name__ == '__main__':
    main_list = []
    try:
        user_input = int(input("Enter List of size: "))
        if user_input < 0:
            raise Exception("\033[1mPlease Enter Valid Positive Integer number.")
        for value in range(user_input):
            user_value = int(input("Enter {} index of value: ".format(value)))
            main_list.append(user_value)
    except ValueError:
        print("\033[1mInput Des not found! please Enter integers number.")
        sys.exit()
    except Exception as error:
        print(error)
        sys.exit()
    print("list is {} ".format(main_list))
