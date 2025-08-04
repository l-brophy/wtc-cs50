from pyfiglet import Figlet
import random
import sys


figlet = Figlet()
fonts = figlet.getFonts()


def check_args():
    
    if len(sys.argv) == 1:
        return random.choice(fonts)
    
    if len(sys.argv) != 3:
        return
    
    if sys.argv[1] != "-f" and sys.argv[1] != "--f":
        return
    
    if sys.argv[2] not in fonts:
        return
    
    return sys.argv[2]


f = check_args()

if f is None:
    raise SystemExit("Invalid usage")
else:
    figlet.setFont(font=f)

print(figlet.renderText(input("Input: ")))