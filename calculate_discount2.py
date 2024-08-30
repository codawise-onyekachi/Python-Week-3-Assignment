""" Using the calculate_discount function,
 prompt the user to enter the original price of an item and the discount percentage.
 Print the final price after applying the discount, 
 or if no discount was applied, print the original price.""" 

def  calculate_discount(price, discount_percent):
    final_price = price - (price * (discount_percent / 100))

    
    if discount_percent >= 20:

        return final_price
    else:
        return price
    
price = int(input("Please enter a price: "))
discount_percent = int(input("Please enter the discount on the price in percentage: "))
final = calculate_discount( price, discount_percent)
print("The final price is: ", final)