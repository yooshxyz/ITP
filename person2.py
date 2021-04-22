from person1 import Person

first_name_input = input("What is your person's first name?")
last_name_input = input("What is your persons last name?")
p1 = Person(first_name_input, last_name_input)
p1.age = 16

p2 = Person("bill", "Billicheck")
p2.age = 35

print(p1)
print(p2)

people = []
people.append(p1)
people.append(p2)

print(people)

# def get_first_name(p):            # SORTS BY FIRST NAME
#    return p.first_name
# two ways

people.sort(key = lambda p:p.first_name) # the second way is to change the lambda to the name of the function
print(people)

people.sort(key = lambda p:p.age)
print(people)