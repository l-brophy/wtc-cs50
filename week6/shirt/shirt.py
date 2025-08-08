import sys
from PIL import Image


def check_args():
    
    valid_filetypes = ["jpg", "jpeg", "png"]
    
    if len(sys.argv) > 3:
        raise SystemExit("Too many command-line arguments")
    
    if len(sys.argv) < 3:
        raise SystemExit("Too few command-line arguments")
    
    if "." not in sys.argv[1] or "." not in sys.argv[2]:
        raise SystemExit("Invalid input")
    
    exts = []
    for i in range(1, 3):
        exts.append(sys.argv[i].split(".")[1])
    
    if exts[0] not in valid_filetypes or exts[1] not in valid_filetypes:
        raise SystemExit("Invalid input")
    
    if exts[0] != exts[1]:
        raise SystemExit("Extensions do not match")
    
    return [sys.argv[1], sys.argv[2]]


check_args()