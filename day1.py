# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456

# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.


from collections import Counter

values = Counter()
nums = []
with open('day1.txt') as f:
    for line in f:
        nums.append(int(line.strip('\n')))

# def part_one(nums):
#     print(nums)
#     for num in nums:
#         difference = 2020 - num
#         if difference in values:
#             final = difference * num
#             print(f"SOLUTION IS {final}")
#             return(num,difference)
#         values[num] += 1
# expense_report(nums)

# Part 2
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?

def part_two(nums):
    print(nums)
    for x, i in enumerate(nums):
        for j in nums[x:]:
            if (2020-i-j) in values:
                final = i * j * (2020-i-j)
                print(f"SOLUTION IS {final}")
                return (f"Solution is {final}")
            values[j] += 1

if __name__ == "__main__":
    # part_one(nums)
    part_two(nums)