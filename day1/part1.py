with open("./input.txt", 'r') as data:
    raw = data.read()

raw = raw.split("\n\n")

max = 0

for i, line in enumerate(raw):
    words = line.split("\n")
    linesum = sum([int(word) for word in words])
    if linesum > max:
        max = linesum

print(max)