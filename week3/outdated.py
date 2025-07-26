MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def correct_date():
    date = input("Date: ")

    if date[0].isalpha():
        
        date = date.replace(",", "").split()
        date[0] = MONTHS.get(date[0], 13)
        
    else:
        date = date.split("/")
    
    day, month, year = int(date[1]), int(date[0]), date[2]
    
    if month > 12 or day > 31:
        correct_date()
    
    print(f"{year}-{month:02}-{day:02}")
    
correct_date()
# test cases want input rejections not reprompts for certain incorrect formats. a bit of a lol