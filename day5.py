with open('day5.txt') as f:
    lines = f.read().strip().split()

#Plane is 128 rows x 8 columns

def seat_check(seats):
    seat_id = []
    # Part One to  parse through the seats
    for index, seat in enumerate(seats):
        seat_id.append(row_check(seat) * 8 + column_check(seat))
    seat_id= sorted(seat_id, key=int)
    #  Part Two to get my seat ID
    for sorted_seat in seat_id:
        if sorted_seat+1 not in seat_id and sorted_seat+2 in seat_id:
            my_seat = sorted_seat+1
    return max(seat_id), my_seat

def row_check(input):
    row_string = input[:-3]
    row_start = 0
    row_end = 127
    #Do continuous checks for first 6 letters, last do a different check
    for letter in row_string[:-1]:
        half = (row_start + row_end) // 2
        if letter == "F":
            row_end = half
        if letter == "B":
            row_start = half+1
    #Logic for last char in row_string 
    if row_string[6] == "F":
        return row_start
    elif row_string[6] == "B":
        return row_end
    else:
        raise StringError("Invalid string input")
    

def column_check(input):
    col_string = input[-3:]
    col_start = 0
    col_end = 7
    #Do continuous checks for first 6 letters, last do a different check
    for letter in col_string[:-1]:
        half = (col_start + col_end) // 2
        if letter == "L":
            col_end = half
        if letter == "R":
            col_start = half+1
    #Logic for last char in row_string 
    if col_string[-1] == "L":
        return col_start
    elif col_string[-1] == "R":
        return col_end
    else:
        raise StringError("Invalid string input")
class StringError(Exception):
    pass

seat_check(lines)