def main():
    time = convert(input("What time is it? "))
    
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")


def convert(time):
    time = time.split(":")
    
    hours, minutes = float(time[0]), float(time[1][:2]) / 60
    
    if "p" in time[1]:
        hours += 12
        
    return hours + minutes


if __name__ == "__main__":
    main()