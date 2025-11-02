def calculate_discount(price, discount_percent):
    # If the discount is 20% or higher, apply the discount
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Otherwise, return the original price
        return price


# Ask the user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and store the result
final_price = calculate_discount(price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"The final price after {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {price}")
