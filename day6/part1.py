with open("./input.txt", 'r') as data:
    datastream = data.read()

i = 0
while i < len(datastream) - 4:
    if len(set(datastream[i:i+4])) == 4:
        break
    i += 1

print(i + 4)
