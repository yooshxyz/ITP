# we learned variables first
# then conditionals and iterations.
# class.function(parameters)

def main():
    numtimes = int(input("How many times do you want to be repeated?"))
    simpleOperators.sayHello(numtimes)

    # go to corresponding function and these values equal those variables. IF NAME IS MENTIONED ORDER DOES NOT MATTER.
    simpleOperators.helloWorld("world", 5, True)
    want_to_continue = input("Do you want to continue?")

    if want_to_continue.lower() == "yes" or want_to_continue.lower() == "y":
        user_input = int(input("Hello, pick a number: "))
        user_input_calc = int(input("What do you want the multiplier to be? "))
        simpleOperators.calc(user_input, user_input_calc)


class simpleOperators:
    def sayHello(numtimes):
        for i in range(numtimes):
            name = ("Baran")
            print(name)

    def calc(user_input, user_input_calc):
        calc_output = user_input * user_input_calc
        print(f"Here is {user_input} * {user_input_calc}:") #calc_output is it's output
        return calc_output

    def helloWorld(world, runtime=1, hello=False):
        for i in range(runtime):
            if hello:
                print("Helllloooooo")
            else:
                print(f"Hello {world}")

main()
