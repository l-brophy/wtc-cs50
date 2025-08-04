from emoji import emojize, emoji_count

user_string = input("Input: ")

if emoji_count(user_string) == 0:
    print(f"Output: {emojize(user_string, language="alias")}")
else:
    print(f"Output: {emojize(user_string)}")