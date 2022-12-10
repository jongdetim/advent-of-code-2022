import numpy as np

def find_visible_trees(forest, visible_trees, col_len, row_len, horizontal=False):
    for x, row in enumerate(forest):
        height = -1
        for y, tree in enumerate(row):
            if tree > height:
                height = tree
                if horizontal:
                    visible_trees.add((abs(row_len - y), abs(col_len - x)))
                else:
                    visible_trees.add((abs(col_len - x), abs(row_len - y)))

forest = np.genfromtxt("./input.txt", delimiter=1, dtype=int)
visible_trees = set()
x_len, y_len = forest.shape[0] - 1, forest.shape[1] - 1
find_visible_trees(forest.T, visible_trees, 0, 0) # top to bottom
find_visible_trees(forest, visible_trees, 0, 0, horizontal=True) # left to right
forest = np.flip(forest, axis=(0, 1))
find_visible_trees(forest.T, visible_trees, x_len, y_len) # bottom to top
find_visible_trees(forest, visible_trees, x_len, y_len, horizontal=True) # right to left
print(len(visible_trees))
