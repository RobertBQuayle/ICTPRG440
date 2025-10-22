def matchUserInput():
    print("\n")
    print("Choose the Game you want to play\n")
    print("1 - Guess the Password\n")
    print("2 - Take Off!\n")

    userInput = input("Enter the game number: ")
    match userInput:
        case "1":
            Passwordaccess()
        case "2":
            Takeoff()
        case _:
            print("There is no game with this number")
            matchUserInput()


def Passwordaccess():
    Password = "555666"
    guess = ""
    counter = 1

    while guess != Password and counter < 4:
        guess = input(f"Enter Password, 3 tries allowed, Attempt {counter} - ")
        counter += 1

    if guess == Password:
        print("Access Granted")
    else:
        print("Go Away")


def Takeoff():
    counter = 10

    while counter < 11 and counter > -1:
        print(counter)
        counter -= 1
    print("Take Off...Boom!")


if __name__ == "__main__":
    matchUserInput()

