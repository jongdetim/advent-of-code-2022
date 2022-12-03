with open("./input.txt", 'r') as data:
    lines = data.read().splitlines()

splitlines = [(line[:len(line)//2], line[len(line)//2:]) for line in lines]
priority = 0

for comp1, comp2 in splitlines:
    common_char = ''.join([
        char for char in comp1
        if char in comp2])[0]
    if common_char.isupper():
        priority += ord(common_char) - ord('A') + 27
    else:
        priority += ord(common_char) - ord('a') + 1

print(priority)
