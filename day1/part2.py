# this time top 3
with open("./input.txt", 'r') as data:
    raw = data.read()

raw = raw.split("\n\n")

total_calories = []

for i, line in enumerate(raw):
    words = line.split("\n")
    linesum = sum([int(word) for word in words])
    total_calories.append(linesum)

total_calories.sort(reverse=True)

print(sum(total_calories[0:3]))