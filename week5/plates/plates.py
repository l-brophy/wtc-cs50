def main():
    
    if is_valid(input("Plate: ")):
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
                return False
            else:
                first_num = i
                break
    
    if not s[first_num:].isdigit():
        return False
    
    return True


if __name__ == "__main__":
    main()