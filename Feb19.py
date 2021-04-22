import random
# answer = answer.strip()[0].lower()
def main():
    while True:
        user_choice_input = int(input("What Function do you want to Use?\nPlease type 1 for the No vowels function, type 2 for the random vowels function, and 3 for the even or odd calculator.\n"))
        if user_choice_input == 1:
            vowelLessCommand()
        elif user_choice_input == 2:
            randomWords()
        elif user_choice_input ==3:
            evenOdd()
        else:
            print("Please choose one of those numbers!")
            user_quit_option = input("If you wise to exit please press X")
            if user_quit_option.lower() == "x":
                print("Exiting....")
                break
            else:
                return
        return

def vowelLessCommand():
    vowels = ["a","e","i","o","u"]
    user_input = input("Please input your sentence: ")
    vowelless = ""
    for i in user_input:
        if i not in vowels:
            if i != vowels:
                vowelless = vowelless + i
    print(vowelless)

def randomWords():
    x = 0
    vowels = ["a","e","i","o","u"]
    user_input2 = input("Please input your sentence: ")
    randomvalues = ""
    for i in user_input2:
        if i in vowels:
            i = random.choice(vowels)
            randomvalues += i
        else:
            randomvalues += i
    print(randomvalues)
def evenOdd():
    user3_input = float(input("Please pick a number."))
    if user3_input % 2 == 0:
        print("The number is even!")
    else:
        print("The number is odd!")

def addUp():
    x = 0
    user_number_input = int(input("Pick a number!")) 
main()
