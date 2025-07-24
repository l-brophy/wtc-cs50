vowels = "aeiou"

tweet = input("Input: ")
twt = ""

for i in tweet:
    if i.lower() not in vowels:
        twt += i

print(f"Output: {twt}")