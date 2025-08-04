def main():
    tweet = input("Your tweet: ")
    
    print(f"Yr twt: {shorten(tweet)}")


def shorten(word):
    twt = ""
    
    for i in word:
        if i.lower() not in "aeiou":
            twt += i
    
    return twt


if __name__ == "__main__":
    main()