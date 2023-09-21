import sys

if __name__ == '__main__':
    try:
        user_input = int(input("Please enter a number: "))
    except ValueError:
        print("\033[1mPlease Enter Integer number")
        sys.exit()
    if user_input in range(0, 11):
        print("small")
    elif user_input in range(11, 101):
        print("Medium")
    elif user_input in range(101, 1001):
        print("Large")
    else:
        print("\033[1mInvalid Number.")
