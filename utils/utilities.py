def decorating_string(string: str):
    decor = "*" * len(string)

    return decor


def greeting():
    string = "welcome to calculator"

    return f"\n{decorating_string(string)}" \
           f"\n{string.upper()}\n" \
           f"{decorating_string(string)}\n"


def actions_list():
    print("\nYou must choose action what you want to do :\n")

    actions = ["/", "*", "+", "-", "quit"]

    i = 0
    while i < len(actions):
        print(f"{i + 1}) {actions[i].upper()}")
        i += 1


def choose_action():

    actions_list()

    try:
        user_choose = int(input("\nEnter number :\n"))
    except:
        print("\nIncorrect data\nPlease, Try again\n".upper())
        return

    return user_choose


def number_list(num_list: list):
    try:
        num1 = int(input("Enter first number\n"))
        num2 = int(input("Enter second number\n"))
        num_list.append(num1)
        num_list.append(num2)

    except:
        print(f"\nIncorrect data\nPlease, Try again\n".upper())
        return

    return num_list


def choose_repeat():
    print("Do you want to repeat\n")
    repeat = input("y/n ? :\n")

    return repeat