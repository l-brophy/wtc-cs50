def check_tank():
    
    gauge = input("Fraction: ").split("/")
    
    try:
        fraction = int(gauge[0]) /int(gauge[1])
    except (ValueError, ZeroDivisionError):
        check_tank()
    
    if fraction < 0:
        raise ValueError(check_tank())
    
    percentage = round(fraction * 100)
    if percentage > 100:
        check_tank()
    elif percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")
    
check_tank()