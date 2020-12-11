# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#

# These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

# ..##.........##.........##.........##.........##.........##.......  --->
# #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........#.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...##....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

# The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

# In this example, traversing the map using this slope would cause you to encounter 7 trees.

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

map = []
with open('day3.txt') as f:
    for line in f:
        map.append(line.strip())

# while row +1 < len(map):
#     row +=1
#     col +=3
#     if map[row][col % length] == '#':
#         trees+=1

# for val in range(len(map)):
#     print(row, col%length, col)
#     if map[row][col % length] == '#':
#         trees+=1
#     row += row_inc
#     col += col_inc

def tree_check(map, row_inc, col_inc):
    trees = 0
    row = 0
    col = 0
    length = len(map[row])
    while row +1 < len(map):
        row += row_inc
        col += col_inc
        if map[row][col % length] == '#':
            trees+=1
    return trees
tree_check(map, 1, 3)

# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

#     Right 1, down 1.
#     Right 3, down 1. (This is the slope you already checked.)
#     Right 5, down 1.
#     Right 7, down 1.
#     Right 1, down 2.

# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

product_trees = tree_check(map, 1, 3) * tree_check(map, 1, 1) * tree_check(map, 1, 5) * tree_check(map, 1, 7) * tree_check(map, 2, 1)
print(product_trees)