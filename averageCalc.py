average = 0
while True:
    user_input = int(input("what would like to add to your dataset? Please only add integers. If you ever want to leave, press X and then press enter"))
    if user_input.upper() == "X":
        print("Thank you for using the average calculator!")
        break
    x = 1
    average = user_input/x
    print("The average is: " average)
