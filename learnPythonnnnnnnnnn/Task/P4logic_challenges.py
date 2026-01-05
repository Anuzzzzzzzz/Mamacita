import random

# ------------------------------
# 1. Number Guessing Game
# ------------------------------
def number_guessing_game():
    """
    User has to guess a random number between 1 and 20.
    Program tells if guess is too high or too low.
    """
    secret = random.randint(1, 20)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    while True:
        try:
            guess = int(input("Guess a number (1-20): "))
            attempts += 1
            if guess < 1 or guess > 20:
                print("Number must be between 1 and 20.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret:
            print(f"Congrats! You guessed it in {attempts} attempts.")
            break
        elif guess < secret:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

# ------------------------------
# 2. Password Strength Checker
# ------------------------------
def password_strength_checker():
    """
    Checks password strength based on length and character variety.
    """
    print("\n--- Password Strength Checker ---")
    password = input("Enter a password: ")
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()-_+=" for c in password):
        strength += 1

    if strength <= 2:
        print("Weak password")
    elif strength <= 4:
        print("Moderate password")
    else:
        print("Strong password")

# ------------------------------
# 3. Text Analysis Tool
# ------------------------------
def text_analysis_tool():
    """
    Analyze user input text: word count, vowel count, character count.
    """
    print("\n--- Text Analysis Tool ---")
    text = input("Enter a sentence or paragraph: ")

    words = len(text.split())
    vowels = sum(1 for c in text.lower() if c in "aeiou")
    chars = len(text)

    print(f"Word count: {words}")
    print(f"Vowel count: {vowels}")
    print(f"Total characters: {chars}")

# ------------------------------
# Main Menu
# ------------------------------
def main():
    while True:
        print("\n--- Logic Challenges ---")
        print("1. Number Guessing Game")
        print("2. Password Strength Checker")
        print("3. Text Analysis Tool")
        print("4. Exit")

        choice = input("Choose: ")
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            password_strength_checker()
        elif choice == "3":
            text_analysis_tool()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
