# Task 5.2: The Email Validator
# Scenario: A user is signing up, and you need to ensure their
# email format is loosely correct.
# Instructions:
# 1. Ask the user to input an email.
# 2. Clean: Convert the input to lowercase
# using .lower() and remove spaces using .strip().
# 3. Logic:
# o Check if the cleaned email
# contains &quot;@&quot; and ends with &quot;.com&quot;.
# o If yes: Print &quot;Valid Email: [cleaned_email]&quot;.
# o If no: Print &quot;Invalid format.&quot;
# 4. Bonus: Extract just the username (everything before
# the @) using .split(&quot;@&quot;).

email = input("Enter your email: ")
cleaned_email = email.lower().strip()   
if "@" in cleaned_email and cleaned_email.endswith(".com"):
    print(f"Valid Email: {cleaned_email}")
    username = cleaned_email.split("@")[0]
    print(f"Username: {username}")
else:
    print("Invalid format.")

