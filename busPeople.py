from math import fmod
from math import ceil

avgbus = 0
evenonbus = 0
people = int(input("how many people are coming on the bus?"))
peopleonbus = int(input("how many people can fit on one bus?"))
notfullbus = fmod(people, peopleonbus)
if people // peopleonbus <= 1:
    print("You only need one bus.")
average = ceil(people / ceil(people / peopleonbus))
if people // peopleonbus and fmod(people, peopleonbus):
    print(f"You need {ceil(people / peopleonbus)} buses and the last bus will have {notfullbus} people on it.")
elif people // peopleonbus:
    print(f"You need {people // peopleonbus} buses")
