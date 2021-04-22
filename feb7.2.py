import random
phrase = input("what is your phrase?.")
vowel = ["a", "e", "i", "o", "u"]
listphrase = []
listphrase = enumerate(phrase)
r = random.randint(1,8)
print(listphrase)
for char in phrase:
    if char in vowel:
        continue
    print(char, end="")
    print(r, end=" ")
