from collections import Counter



with open('day6.txt') as f:
    lines = f.read().strip().split("\n\n")
    data = [item.split() for item in lines]
    # print(data)
def first_custom(data):
    total = 0
    for group in data:
        letter_set = set(group[0]).union(*group[1:])
        total += len(letter_set)
    print(f"Total individual questions with yes is {total}")

def second_custom(data):
    total = 0
    for group in data:
        letter_set = set(group[0]).intersection(*group[1:])
        total += len(letter_set)
    print(f"Total number of combined questions with yes is {total}")

if __name__ == '__main__':
    first_custom(data)
    second_custom(data)