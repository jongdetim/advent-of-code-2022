with open("./input.txt", 'r') as data:
    raw = data.read()

lines = [line.split(" ") for line in raw.split("\n")]

score = 0

for line in lines:
    p1, p2 = ord(line[0]) - ord('A') + 1, ord(line[1]) - ord('X') + 1
    # print(p1, p2)

    score += p2
    if p1 == p2:
        score += 3
    elif p2 == p1 + 1 or p2 == p1 - 2:
        score += 6

print(score)
