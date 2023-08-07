import random

def main():
    # the sys will generate a random number every time
    secrect_number = random.randint(1,100)

    # ask the user to guess a number
    user_str = input("I have a number in mind, try your best to guess which number it is, you have an maximum of 10 times to guess it, come on.")
    user_guess = int(user_str)
    # compare and tell whether user have answered it right
    while user_guess != secrect_number:
        if user_guess < secrect_number:
            user_str=input("Sorry! That guess was too low! Take another guess.")
        if user_guess > secrect_number:
            user_str=input("Sorry! That guess was too high! Take another guess.")
        user_guess = int(user_str)
    print(f"Wow, you are so great, you have made it! it is the correct number:{user_guess}")

if __name__ =="main":
    main()
