amount_due = 50

valid_coins = [25, 10, 5]

while amount_due > 0:
    
    print(f"Amount due: {amount_due}")
    
    paid = int(input("Insert coin: "))
    
    if paid in valid_coins:
        amount_due -= paid

change = abs(amount_due)

print(f"Change owed: {change}")