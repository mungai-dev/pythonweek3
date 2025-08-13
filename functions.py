def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount = price *discount_percent/100
        discounted_price = price - discount
        return discounted_price
    else:
        return price

finalprice1 = calculate_discount(500,10)
finalprice2 = calculate_discount(500,25)

print("### Fixed test values ###")

print(finalprice1)
print(finalprice2)

print("\n### User input ###")

price=float(input("price:"))
discount_percent=float(input("discount_percent:"))
finalprice = calculate_discount(price,discount_percent)
print(f"finalprice:{finalprice}")
