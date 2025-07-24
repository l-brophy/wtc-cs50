def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    if len(s) < 2 or len(s) > 6:
        return False
    
    if not s.isalnum():
        return False
    
    if not s[0].isalpha():
        return False
    
    if s.isalpha():
        return True
    
    for i in range(0, len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                # early return if first digit is a 0
                return False
            else:
                # exit loop once first number is found
                first_num = i
                break
    
    if not s[first_num:].isdigit(): # check substring for letters after first number appeearance
        return False
    
    return True


main()