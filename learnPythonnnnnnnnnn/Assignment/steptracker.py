# Task 3.1: The Daily Step Tracker
# Scenario: A fitness app needs to calculate the total steps
# taken in a week and find average.
# Instructions:
# 1. Create a list of steps for 7 days: steps = [4000, 5000,
# 3000, 8000, 10000, 2000, 6000].
# 2. Create a variable total_steps = 0.
# 3. Loop: Iterate through the list. Add each days steps
# to total_steps. Print &quot;Day [X]: [Steps] steps&quot;.
# 4. After Loop: Calculate the average (total / 7) and print: 
# Weekly Total: [Total]


steps = [4000, 5000, 3000, 8000, 10000, 2000, 6000]
total_steps = 0

for day in range(7):
    total_steps += steps[day]
    print(f"Day {day + 1}: {steps[day]} steps")

average_steps = total_steps / 7

print(f"Weekly Total: {total_steps}")
print(f"Average Steps: {average_steps}")
