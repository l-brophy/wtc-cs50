def main():
    print(f"${value(input("Greeting: ").strip())}")


def value(greeting):
    
    if greeting.lower() == "hello":
        return 0
    
    if greeting.lower()[0] == "h":
        return 20
    
    return 100


if __name__ == "__main__":
    main()