
def contains_any(lower, upper):
    if lower[0] <= lower[1] and lower[1] <= upper[0] or \
    lower[1] <= lower[0] and lower[0] <= upper[1]:
        return True
    return False

with open("./input.txt", 'r') as data:
    lines = data.read().splitlines()
pairs = [line.split(',') for line in lines]
contained_pairs = 0

for pair in pairs:
    elves = []
    lower = []
    upper = []
    for i, elf in enumerate(pair):
        print(i)
        elves.append(elf.split('-'))
        
    for ids in elves:
        lower.append(int(ids[0]))
        upper.append(int(ids[1]))

    contained_pairs += contains_any(lower, upper)

print(contained_pairs)
