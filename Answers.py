def calculate_discount(price, discount_percent):
    if discount_percent>= 20:
        discount= price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percent: "))
#calculate and print
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: {final_price}")