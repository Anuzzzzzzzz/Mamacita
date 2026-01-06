# Task 4.2: The Number Guessing Game
# Scenario: You are building a simple game where the user
# guesses a number between 1 and 10.
# Instructions:
# 1. Set correct_number = 7.
# 2. Start a while True loop.
# 3. Ask user to &quot;Guess the number&quot;.
# 4. Conditions:
# o If guess is correct_number: Print &quot;You won!&quot;
# and break.
# o If guess is not correct: Print &quot;Try again!&quot;.
# o (Optional Challenge): If the user types
# &quot;quit&quot;, break the loop immediately.

correct_number = 7
while True:
    user_input = input("Guess the number (or type 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Game exited.")
        break

    guess = int(user_input)

    if guess == correct_number:
        print("You won!🏆")
        break
    else:
        print("Try again!😔🌀")
