# Task 6.2: The RPG Inventory System
# Scenario: You are managing a player&#39;s backpack in a role-
# playing game.
# Instructions:
# 1. Inventory (List): Create a list backpack =

# [&quot;Sword&quot;, &quot;Potion&quot;, &quot;Map&quot;].
# 2. Loot: The player finds a &quot;Shield&quot;. .append() it to the
# backpack.
# 3. Use Item: The player drinks the
# Potion. .remove() &quot;Potion&quot; from the list.
# 4. Game Settings (Tuple): Create a tuple dimensions
# = (1920, 1080) representing screen resolution.
# 5. Print: Display the final backpack and
# the dimensions.
# 6. Comment Check: Add a comment explaining why you
# utilized a tuple for dimensions (e.g., &quot;# Screen size
# shouldn't change during gameplay&quot;).

backpack = ["Sword", "Potion", "Map"]
backpack.append("Shield")
backpack.remove("Potion")       
dimensions = (1920, 1080)  #screen should not change while game is running

print("Backpack Contents:", backpack)
print("Game Dimensions:", dimensions)
