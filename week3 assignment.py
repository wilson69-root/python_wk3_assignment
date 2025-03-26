# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Calculate the discount amount
    discount = (discount_percent / 100) * price
    
    # Check if the discount is 20% or higher
    if discount >= (20/100) * price:
        # Apply the discount
        return price - discount
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price of an item
price = float(input("Enter the original price: "))

# Prompt the user to enter the discount percentage
discount = float(input("Enter the discount percentage: "))

# Print the final price after applying the discount, or the original price if no discount was applied
print(calculate_discount(price, discount))


