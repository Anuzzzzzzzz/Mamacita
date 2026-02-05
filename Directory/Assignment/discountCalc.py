# Task 8.2: The Discount Calculator
# Scenario: An online store has a sale. You need a function to
# calculate the final price after a discount percent.
# Instructions:
# 1. Define a
# function apply_discount(original_price,
# discount_percent).
# 2. Logic:
# o Calculate saved_amount =
# original_price * (discount_percent
# / 100).
# o Calculate final_price =
# original_price - saved_amount.
# o return the final_price.
# 3. Main Code:
# o Call the function: shirt =
# apply_discount(50, 10) (Price 50, 10%
# off).
# o Call the function: laptop =
# apply_discount(1000, 20) (Price 1000,
# 20% off).

# 4. Output: Print the final price for both the shirt and the
# laptop.

def apply_discount(original_price, discount_percent):
    saved_amount = original_price * (discount_percent / 100)
    final_price = original_price - saved_amount
    return final_price

#call the function

shirt = apply_discount(50, 10)  # Price 50, 10% off
laptop = apply_discount(1000, 20)  # Price 1000, 20% off


print(f"Final price for the shirt: ${shirt}")
print(f"Final price for the laptop: ${laptop}")
