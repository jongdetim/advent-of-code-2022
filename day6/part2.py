with open("./input.txt", 'r') as data:
    datastream = data.read()

i = 0
while i < len(datastream) - 14:
    if len(set(datastream[i:i+14])) == 14:
        break
    i += 1

print(i + 14)
