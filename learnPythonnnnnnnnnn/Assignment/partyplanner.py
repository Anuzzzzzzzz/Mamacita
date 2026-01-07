# Task 6.1: The Party Planner
# Scenario: You are organizing a party. The Guest List keeps
# changing (people coming and going), but the Party Location is
# fixed and cannot change.
# Instructions:
# 1. The Guests (List): Create a list called guests with 3
# names:
# [&quot;Alice&quot;, &quot;Bob&quot;, &quot;Charlie&quot;]
# 2. New Friend: &quot;David&quot; wants to come. Append him to the list.
# 3. Cancellation: &quot;Bob&quot; can&#39;t make it. Remove him from the
# list.
# 4. The Location (Tuple): Create a tuple called address with
# fixed details:
# (&quot;123 Main St&quot;, &quot;New York&quot;)
# 5. The Error Test: Try to change &quot;New
# York&quot; to &quot;London&quot; using index address[1] =
# &quot;London&quot;.
# Note: This will cause an error. Comment out the line and write
# a short comment saying &quot;Tuples cannot be changed&quot;
# 6. Final Check: Print the updated guests list and
# the address tuple.

guests = ["Alice", "Bob", "Charlie"]
guests.append("David")
guests.remove("Bob")
address = ("123 Main St", "New York")

# Tuples cannot be changed
# address[1] = "London"

print("Final Guest List:", guests)
print("Party Location:", address)
