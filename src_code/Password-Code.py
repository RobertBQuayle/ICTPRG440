
def Passwordaccess():

        Password = "555666"
        guess = ""
        counter = 1

        while guess != Password and counter < 4:
                
            guess = input(f"EnterPassword, 3 trys allowed, Attempt {counter} - ")
            counter += 1

        if guess == Password:
            print("Access Granted")
        else:
             print("Go Away")




if __name__ == "__main__":
     Passwordaccess()

