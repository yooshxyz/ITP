import random
nouns_file = open("nouns.txt")
# names = open()
adj_file = open("adj.txt")
# print(nouns_file)
# for line in nouns_file:
#    word = line.strip()
#   nouns.append(word)

nouns = [line.strip() for line in nouns_file if line.strip()!=""]
adjectives = [line.strip() for line in adj_file if line.strip() !=""]

adjused = random.choice(adjectives).capitalize()   # could also do noun_index = random.randrange(len(nouns)) then use noun = nouns[noun_index]
nounsused = random.choice(nouns).capitalize()
print(f"The band name is: {adjused} {nounsused}")
gennumber = int(input("How many bad names do yo wish to generate?"))
f = open("bandNames.txt", "a+")
f.write("Here are some more band names:")
for x in range(gennumber):
    f.write(f"The band name is: {random.choice(adjectives).capitalize()} {random.choice(nouns).capitalize()} \n")
