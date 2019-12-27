phoneBook = {}
break_loop = False


def enter_phone_number():
    global break_loop
    number = int(input(' Enter a number: '))
    if len(number) == 0:
        break_loop = True
    print(number[:3], number[3:6], number[6:])
    phoneBook[number] = {number}
    print(phoneBook)


def main():
    while not break_loop:
        enter_phone_number()


main()
