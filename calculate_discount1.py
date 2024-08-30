""" Create a function named calculate_discount(price, discount_percent) 
that calculates the final price after applying a discount. 
The function should take the original price (price) 
and the discount percentage (discount_percent) as parameters. 
If the discount is 20% or higher, apply the discount; otherwise, return the original price."""

def  calculate_discount(price, discount_percent):
    final_price = price - (price * (discount_percent / 100))

    price = 2500
    discount_percent = 20

    if discount_percent >= 20:
        return final_price
    
    else:
        return price
    
print(calculate_discount(price= 2500, discount_percent= 20))