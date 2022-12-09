from dataclasses import dataclass, field

TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000

@dataclass
class Directory:
    parentdir: object
    filesize_total: int = 0
    subdirs: dict = field(default_factory=dict)

def parse_command(line, wd):
    if line[2] == 'c':
        if line[5] == '.':
            return wd.parentdir
        elif line[5] == '/':
            return wd
        else:
            return wd.subdirs[line.split()[2]]
    return wd

def build_tree(lines):
    wd = Directory(None)
    for line in lines:
        if line[0] == '$':
            wd = parse_command(line, wd)
        elif line[0] == 'd':
            dir_name = line.split()[1]
            wd.subdirs[dir_name] = Directory(wd)
        else:
            wd.filesize_total += int(line.split()[0])
    while wd.parentdir is not None:
        wd = wd.parentdir
    return wd # returns root dir

def recursive_dir_size(wd, dir_sizes):
    total_subdir_size = 0
    for subdir in wd.subdirs.values():
        subdir_size = recursive_dir_size(subdir, dir_sizes)
        total_subdir_size += subdir_size
    total = wd.filesize_total + total_subdir_size
    dir_sizes.append(total)
    return total

with open("./input.txt", 'r') as data:
    lines = data.read().splitlines()

root = build_tree(lines)
dir_sizes = []
root_total = recursive_dir_size(root, dir_sizes)
free_space = TOTAL_SPACE - root_total
dir_sizes.sort()
for dirsize in dir_sizes:
    if REQUIRED_SPACE - free_space < dirsize:
        print(dirsize)
        break
