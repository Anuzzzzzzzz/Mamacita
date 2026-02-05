# Task 2.2: The Movie Ticket Clerk
# Scenario: A cinema has age restrictions for a horror movie.
# Instructions:
# 1. Set the ticket_price = 100.
# 2. Ask the user for their age.
# 3. Logic:
# o If age &lt; 18: Print &quot;Access Denied. You are
# too young.&quot;
# o If age &gt;= 18 AND age &lt; 65: Print &quot;Ticket
# costs $100.&quot;
# o If age &gt;= 65 (Senior citizen): Print &quot;Ticket
# costs $80 (Discount applied).&quot;

ticket_price =100
age = int(input("Enter yo age:"))
if age < 18:
    print("Access Denied. You are too young.")
elif age >= 18 and age < 65:
    print(f"Ticket costs ${ticket_price}.")
elif age >= 65:
    print("Ticket costs $80 (Discount applied).")

    