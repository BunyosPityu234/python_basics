def within_range(num: int, min: int, max: int) -> bool:
    return (min < number and number <= max)


def give_message(number: int) -> None:
    state: str = ""
    if 0 < number and number <= 99:
        # OK
        if number < 25:
            state = "young"
        elif number < 50:
            state = "adult"
        elif number < 75:
            state = "elderly"
        elif number <= 99:
            state = "ghost"
        pass

    match state:
        case "young":
            print("Lucky")
        case "adult":
            print("♥")
        case "elderly":
            print("legend")
        case "ghost":
            print("Fart")
        case _:
            pass


while (True):
    answer: str = input("How old are you?\n")
    # Check if input is between 0 and 99
    # 1. Check if valid number
    try:
        number = int(answer)
    except ValueError as err:
        print("Give valid number")
        continue
    # Check if input is between 0 and 99
    valid: bool = within_range(number, 0, 99)
    if not valid:
        print("between 0 and 99")
        continue
    give_message(number)
    break
