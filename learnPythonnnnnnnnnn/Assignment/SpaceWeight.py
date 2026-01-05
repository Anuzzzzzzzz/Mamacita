# Task 1.2: The &quot;Space Weight&quot; Converter
# Scenario: You are an astronaut traveling to the Moon. You
# need to calculate your weight there (gravity is 16.5% of
# Earth&#39;s).
# Instructions:
# 1. Ask the user for their name and
# current earth_weight (float).
# 2. Create a variable moon_factor = 0.165.
# 3. Calculate moon_weight (earth_weight *
# moon_factor).
# 4. Output: Print a sentence using f-string or
# concatenation:
# &quot;Hello [Name], your weight on the Moon
# would be [moon_weight] kg.&quot;

name = input("Enter your name: ")
earth_weigth = float(input("Enter your weight on Earth in(kg): "))
moon_factor = 0.165
moon_weight = earth_weigth * moon_factor
print(f"Hello {name}, your weight on the Moon would be {moon_weight} kg")
