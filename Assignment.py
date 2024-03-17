def calculate_discount(price,discount_percent):
 final_price = price * (100-discount_percent) / 100
 if discount_percent >= 20:
    return final_price
 else:
    return price

original_price = float(input('Enter the price: '))
discount = float(input('Enter the discount: '))
new_price = calculate_discount(original_price,discount)
print('the new price is: ',new_price)