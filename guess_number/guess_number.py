# Guess a random number
import random

def main():
    # the sys will generate a random number every time
    secrect_number = random.randint(1,100)

    # ask the user to guess a number
    print("\n--------------------\nI have a number in mind, try your best to guess which number it is, you have an maximum of 10 times to guess it, come on.\n--------------------\n")
    user_str = input("which number is in your mind now? give me your best guess: ")
    user_guess = int(user_str)
    # compare and tell whether user have answered it right
    while user_guess != secrect_number:
        if user_guess < secrect_number:
            user_str=input("Sorry! That guess was too low! Take another guess.")
        if user_guess > secrect_number:
            user_str=input("Sorry! That guess was too high! Take another guess.")
        user_guess = int(user_str)
    print(f"Wow!! \n--------------------\nyou are so great, \n--------------------\nyou made it! \n--------------------\nit is the correct number:{user_guess}")

if __name__ =="main":
    main()
    


print("\n--------------------\nlet us begin and have fun.")

main()
