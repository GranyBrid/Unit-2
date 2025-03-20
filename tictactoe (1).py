codes = {
    "Newfoundland": "A",
    "Nova Scotia": "B",
    "Prince Edward Island": "C",
    "New Brunswick": "E",
    "Quebec": "G",
    "Quebec": "H",
    "Quebec": "J",
    "Ontario": "K",
    "Ontario": "L",
    "Ontario": "M",
    "Ontario": "N",
    "Ontario": "P",
    "Manitoba": "R",
    "Saskatchewan": "S",
    "Alberta": "T",
    "British Colombia": "V",
    "Nunavut": "X",
    "Northwest Territories": "X",
    "Yukon": "Y"
}

user_code = input("What is your postal code? ")
first_digit = user_code[0]
first_num = user_code[1]
length = len(user_code.replace(' ',''))

if first_num == "0":
    area = "Rural"
else:
    area = "Urban"
    
if length == 6:    
    if first_num.isdigit() == True:
        if first_digit == "X":
            print(f"Your postal code is from Nunavut or Northwest Territories, and is {area}.")
        else:
            for key, value in codes.items():
                if value == first_digit:
                    print(f"Your postal code is from {key}, and is {area}.")
                    break
            else:
                print("That code is invalid.")
    else:
        print("That code is invalid.")
else:
    print("That code is invalid.")
