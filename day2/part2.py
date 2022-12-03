with open("./input.txt", 'r') as data:
    raw = data.read()

lines = [line.split(" ") for line in raw.split("\n")]

score = 0

for line in lines:
    p1, p2 = ord(line[0]) - ord('A') + 1, ord(line[1]) - ord('X') + 1
    if (p2 == 1): # lose
        response = p1 - 1 if p1 - 1 else 3
    elif (p2 == 2): # draw
        response = p1 + 3
    elif (p2 == 3): # win
        response = (p1 % 3) + 1 + 6

    score += response
    # print(p1, p2, response, score)
print(score)
