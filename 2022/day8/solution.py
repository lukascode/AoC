
trees = []

def is_tree_visible(y, x):
    if x == 0 or x == len(trees[y])-1:
        return True
    if y == 0 or y == len(trees)-1:
        return True
    height = trees[y][x]
    visible_from_top = True
    visible_from_bottom = True
    visible_from_left = True
    visible_from_right = True
    for i in range(len(trees)):
        if i != y and height <= trees[i][x]:
            if i < y:
                visible_from_top = False
            else:
                visible_from_bottom = False
                break
    for j in range(len(trees[y])):
        if j != x and height <= trees[y][j]:
            if j < x:
                visible_from_left = False
            else:
                visible_from_right = False
                break
    return visible_from_top or visible_from_bottom or visible_from_left or visible_from_right 

def calculate_highest_scenic():
    points = []
    for y,row in enumerate(trees):
        for x,column in enumerate(row):
            left_count = 0
            right_count = 0
            top_count = 0
            bottom_count = 0
            for i in range(y - 1, -1, -1):
                if column <= trees[i][x]:
                    top_count += 1
                    break
                else:
                    top_count += 1
            for i in range(y + 1, len(trees)):
                if column <= trees[i][x]:
                    bottom_count += 1
                    break
                else:
                    bottom_count += 1
            for j in range(x - 1, -1, -1):
                if column <= trees[y][j]:
                    left_count += 1
                    break
                else:
                    left_count += 1
            for j in range(x + 1, len(trees[y])):
                if column <= trees[y][j]:
                    right_count += 1
                    break
                else:
                    right_count += 1
            points.append(left_count * right_count * top_count * bottom_count)
    return max(points)

def solve():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            tree_row = []
            for tree_height in line:
                tree_row.append(int(tree_height))
            trees.append(tree_row)
        total = 0
        for y,row in enumerate(trees):
            for x,column in enumerate(row):
                if is_tree_visible(y, x):
                    total += 1
        print(total)
        print(calculate_highest_scenic())
        
solve()