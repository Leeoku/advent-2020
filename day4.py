import re

with open('day4.txt') as f:
    lines = f.read().split("\n\n")
    lines = [line.replace("\n", " ") for line in lines]
    passports = [line.split() for line in lines]



def validate_passport(passports):
    count = 0
    #Create two versions of passports that are valid
    valid_passport = dict.fromkeys(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"))
    valid_passport_two = dict.fromkeys(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    passed_passports = []
    for person in passports:
        #Create each person's ID with their valid passport identifiers
        id = {}
        for entry in person:
            field = entry.split(":")
            id[field[0]]=field[1]
        #Compare if the ID passport identifiers match the accepted versions
        if set(id.keys()) == set(valid_passport.keys()) or set(id.keys()) ==set(valid_passport_two.keys()):
            count+=1
            passed_passports.append(id)
    # print(passed_passports, count)
    return(passed_passports, count)

def second_validate_passport(passports):
    second_count = 0
    filtered_passports = passports[0]
    for passport in filtered_passports:
        # birth_check(int(passport["byr"]))
        # issue_year_check(int(passport["iyr"]))
        # expiry_year_check(int(passport["eyr"])) 
        # height_check(passport["hgt"]) 
        # hair_check(passport["hcl"]) 
        # eye_check(passport["ecl"])
        # passport_id_check(passport["pid"])
        if (birth_check(int(passport["byr"])) and
        issue_year_check(int(passport["iyr"])) and
        expiry_year_check(int(passport["eyr"])) and
        height_check(passport["hgt"]) and
        hair_check(passport["hcl"]) and
        eye_check(passport["ecl"]) and
        passport_id_check(passport["pid"])
        ):
            second_count+=1
    print(second_count)

def birth_check(birth_year):
    return 1920 <= birth_year <= 2002

def issue_year_check(issue_year):
    return 2010 <= issue_year <= 2020

def expiry_year_check(expiry_year):
    return 2020 <= expiry_year <= 2030

def height_check(height):
    if height[-2:] == 'cm':
        return 150 <= int(height[:-2]) <= 193
    elif height[-2:] == 'in':
        return 59 <= int(height[:-2]) <= 76
    else:
        return False

def hair_check(colour):
    print(bool(re.match('^#[0-9a-f]{6}', colour)), colour)
    return bool(re.match('^#[0-9a-f]{6}', colour))

def eye_check(colour):
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return colour in valid_colours

def passport_id_check(passport_id):
    return bool(re.match('^[0-9]{9}$', passport_id))

    
if __name__ == "__main__":
    # validate_passport(passports)
    second_validate_passport(validate_passport(passports))