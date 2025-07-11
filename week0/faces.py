# Program replaces emoticons with emojis

def convert(string):
    
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    
    return string

print(convert(input("")))