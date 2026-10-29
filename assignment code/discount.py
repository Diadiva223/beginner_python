#i creaste a function that returns the price after discount
def calculate_discount(price, discount_percent):
    discount_amount =  (price * discount_percent/100)
    return price - discount_amount
#i create a function that returns the price after tax
def calculate_tax(price, tax_percent):
    tax_amount = (price * tax_percent/100)
    return price + tax_amount
def final_price(price, discount_percent, tax_percent):
    price_after_discount = calculate_discount(price, discount_percent)
    price_after_tax = calculate_tax(price_after_discount, tax_percent)
    return price_after_tax

price = float(input("Enter the price\n"))
discount = float(input("Enter the discount %\n"))
tax = float(input("Enter the tax percent %\n"))
result = final_price(price, discount, tax)
print(f"final price is at {result:.2f}")