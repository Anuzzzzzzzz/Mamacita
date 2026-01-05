

# Cyber-ID Generator 
# Task 1.1: The &quot;Cyber-ID&quot; Generator
# Scenario: You are building a registration system for a futuristic
# gaming convention.
# Instructions:
# 1. Ask the user for their username, birth_year (as integer),
# and is_member (True/False).
# 2. Calculate their current age (assume current year is 2025).
# 3. Create a variable entry_fee. If they are a member, fee is
# 10.5, otherwise 20.0.
# 4. Output: Print a formatted ID card:
# &quot;User : {username}”
# “Age : {21}”
# “Is Member : {False}”

# 1. Get Inputs (Using snake_case)
username = input("Enter your username: ")
birth_year = int(input("Enter your birth year: "))

# .lower() makes "True" or "true" both work
is_member_input = input("Are you a member? (True/False): ")
is_member = is_member_input.lower() == "true"

# 2. Calculations (Data Types: int and float)
age = 2025 - birth_year

entry_fee = (is_member * 10.5) + ((not is_member) * 20.0)

print(f"User : {username}\nAge : {age}\nIs Member : {is_member}\nEntry Fee : ${entry_fee}")

