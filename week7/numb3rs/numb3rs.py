import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    pattern = r"(0|1\d{0,2}|2[0-5]{0,2}\.|$){4}"
    
    return True if re.search(pattern, ip) else False


if __name__ == "__main__":
    main()
