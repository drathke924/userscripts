import re
height_num = re.compile("^\d+")
height_unit = re.compile("\w{2}$")
pid_search = re.compile("^\d{9}$")
hcl_search = re.compile("^#[0-9a-f]{6}")



def split_on_colon(data_in):
    return tuple(data_in.split(":"))

def prep_data(data_in):
    return tuple(map(split_on_colon, data_in.replace("\n", " ").split()))

def validate_passport(passport):
    required = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for check in required:
        try:
            passport[check]
        except KeyError:
            return 0
    return 1

def validate_height(hgt):
    unit = height_unit.search(hgt).group(0)
    number = int(height_num.search(hgt).group(0)) 
    if (unit == "cm" and 150 <= number <= 193) or (unit == "in" and 59 <= number <= 76):
        return True
    else:
        return False

def validate_years(byr, iyr, eyr):
    return 1920 <= int(byr) <= 2002 and 2010 <= int(iyr) <= 2020 and 2020 <= int(eyr) <= 2030

def validate_hair(hcl):
    return hcl_search.match(hcl) != None

def validate_pid(pid):
    return pid_search.match(pid) != None

def validate_eyes(ecl):
    acceptable = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    return ecl in acceptable

def validate_all(passport):
    return validate_eyes(passport["ecl"]) and validate_hair(passport["hcl"]) and validate_height(passport["hgt"]) and validate_pid(passport["pid"]) and validate_years(passport["byr"], passport["iyr"], passport["eyr"])
    
def part_one(data_in):
    passed = 0
    for pport in data_in:
        passed += validate_passport(pport)
    return passed
    
def part_two(data_in):
    passed = 0
    for pport in data_in:
        if validate_passport(pport) and validate_all(pport):
            passed += 1
    return passed
            
            
            

with open("input4.txt" , "r") as f:
	data = list(map(prep_data, f.read().split("\n\n")))

for index in range(0, len(data)):
    passport = data[index]
    new_passport = {passport[i][0] : passport[i][1] for i in range(0, len(passport))}
    data[index] = new_passport

print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))
