cart = {
    "apple":2.5,
    "banana":1.2,
    "milk":3.0
}

total = 0
for item, price in cart.items():
    print(f"{item}: ${price}")
    total += price
    
print(f"Total: ${total}")    