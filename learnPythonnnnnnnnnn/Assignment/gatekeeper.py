# Task 4.1: The &quot;Infinite&quot; Gatekeeper
# Scenario: A security door requires a PIN code. It allows 3
# attempts before locking out.
# Instructions:
# 1. Set a secret PIN: secret = 1234. Set attempts = 0
# 2. Start a while loop
# 3. Ask user to &quot;Enter PIN&quot;. Increase attempts by 1.
# 4. Conditions: - If input matches secret:
# Print &quot;Access Granted&quot; and break.
#  - If attempts reaches
# 3: Print &quot;System Locked&quot; and break.
#  - Else: Print &quot;Wrong PIN, try again

secret = 1234
attempts = 0

while True:
    user_input = int(input("Enter PIN: "))
    attempts += 1

    if user_input == secret:
        print("Access Granted")
        break
    elif attempts == 3:
        print("System Locked")
        break
    else:
        print("Wrong PIN, try again.")