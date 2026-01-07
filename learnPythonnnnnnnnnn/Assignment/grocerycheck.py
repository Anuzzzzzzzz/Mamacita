# Task 7.2: The Grocery Price Checker
# Scenario: You have a shopping list and a database of prices.
# You need to calculate the bill.
# Instructions:
# 1. Database: Create a dictionary prices = {&quot;Apple&quot;:
# 2, &quot;Banana&quot;: 1, &quot;Milk&quot;: 5}.
# 2. Shopping List: cart = [&quot;Apple&quot;, &quot;Apple&quot;,
# &quot;Milk&quot;, &quot;Banana&quot;].
# 3. Bill Calculation:
# o Create total_cost = 0.
# o Loop through the cart.
# o For each item, look up its price in prices and
# add it to total_cost.

# 4. Unique Items: Print the unique items bought
# using set(cart).
# 5. Final Output: Print &quot;Total Bill: $[Amount]&quot;.

prices={"Apple":2,"banana":1,"Milk":5}
cart=["Apple","Apple","Milk","Banana"]
total_cost=0
for item in cart:
    item_lower=item.lower()
    if item_lower in prices:
        total_cost += prices[item_lower]
print("Unique items bought:", set(cart))
print(f"Total Bill: ${total_cost}")
