def main():
    ...


def convert(fraction):
    
    fraction = fraction.split("/")
    
    try:
        result = int(fraction[0]) / int(fraction[1])
        if result < 0:
            raise ValueError()
    except (ValueError, ZeroDivisionError):
        raise
    
    return round(result * 100)


def gauge(percentage):
    
    if percentage <= 1:
        return "E"
    
    if percentage >= 99:
        return "F"
    
    return f"{percentage}%"


if __name__ == "__main__":
    main()