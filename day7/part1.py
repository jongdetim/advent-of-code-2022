from dataclasses import dataclass, field

with open("./input.txt", 'r') as data:
    lines = data.read().splitlines()

@dataclass
class directory:
    parentdir: object
    filesize_total: int
    subdirs: dict = field(default_factory=dict)

def parse_file(lines):
    cursor = root_folder
    for line in lines:
        if line[0] == '$':
            cursor = parse_command(line)
