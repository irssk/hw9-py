from classes.Calculator import Calculator

from utils.utilities import greeting, choose_action, number_list, choose_repeat


def main():
    is_running = True

    print(greeting())

    while is_running:

        new_arr = number_list([])

        try:
            match(choose_action()):
                case 1:
                    Calculator(new_arr[0], new_arr[1]).division()
                case 2:
                    Calculator(new_arr[0], new_arr[1]).multiplication()
                case 3:
                    Calculator(new_arr[0], new_arr[1]).addition()
                case 4:
                    Calculator(new_arr[0], new_arr[1]).subtraction()
                case 5:
                    print("Huck tou!".upper())
                    is_running = False
                    continue
                case _:
                    print(f"\nIncorrect data\nPlease, Try again\n".upper())
                    continue
        except:
            print(f"\nIncorrect data\nPlease, Try again\n".upper())
            continue

        match(choose_repeat().lower()):
            case "y":
                continue
            case "n":
                print("Huck tou!".upper())
                is_running = False
                continue
            case _:
                print(f"\nIncorrect data\nPlease, Try again\n".upper())
                is_running = False
                continue


if __name__ == "__main__":
    main()