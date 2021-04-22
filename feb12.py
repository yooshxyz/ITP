import random
finbonacci = [1, 1]

for i in range (2, 10):
    num = finbonacci[i - 1] + finbonacci[i - 2]
    finbonacci.append(num)
print(finbonacci)

word = "abcdef"
print(word[-1]) # NOTE that it loops around and prints the last number
seclist = [letter for letter in word if letter != "a"] # now the list won't include "a"
print(seclist)
randomlist = [random.choice(seclist) for i in range(10)] # takes a random letter from the list created from the word
print(randomlist)
seclist.reverse()
print(seclist)
search = input("What do you want to find")
if search in seclist:
    print(search in seclist)
