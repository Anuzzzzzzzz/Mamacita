# Task 2.1: The Smart Coffee Machine
# Scenario: You are programming a vending machine that
# checks user credit and sugar preferences.
# Instructions:
# 1. Set a price: coffee_price = 250.
# 2. Ask user
# for credit_amount and sugar_level (High/Low).
# 3. Logic:
#  - If credit &lt; price: Print &quot;Insufficient funds.&quot;-If credit &gt;= price AND sugar_level is &quot;High&quot;:
# Print &quot;Dispensing Sweet Coffee. Change: [X]&quot;
#  - Otherwise: Print &quot;Dispensing Black Coffee. Return Money:[X]&quot;

coffee_price = 250
credit_amount = int(input("Enter your credit amount: "))
sugar_level = input("Enter sugar level (High/Low): ") 
if credit_amount < coffee_price:
    print("Insufficient funds.")
elif credit_amount >= coffee_price and sugar_level.lower() == "high":
    change = credit_amount - coffee_price
    print(f"Dispensing Sweet Coffee. Change: {change}")
else:
    change = credit_amount - coffee_price
    print(f"Dispensing Black Coffee. Return Money: {change}")   
