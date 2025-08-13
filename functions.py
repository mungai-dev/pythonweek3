#created the calculate_discount that takes two parameters
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount = price *discount_percent/100
        discounted_price = price - discount
        return discounted_price
    else:
        return price

#tested the discounted-price with lower and high discount as in the conditional statement
finalprice1 = calculate_discount(500,10)
finalprice2 = calculate_discount(500,25)

print("### Fixed test values ###")

print(finalprice1)
print(finalprice2)

#enable user to put input
print("\n### User input ###")

price=float(input("price:"))
discount_percent=float(input("discount_percent:"))
finalprice = calculate_discount(price,discount_percent)

#discounted price from user input
print(f"finalprice:{finalprice}")
