# Task 3.2: The &quot;Blast Off&quot; Timer
# Scenario: You need to simulate a rocket launch countdown
# sequence.
# Instructions:
# 1. Ask the user for a start_number (e.g., 5 or 10).
# 2. Loop: Use range() to count backwards from
# the start_number down to 1. (Hint: step is -1).
# 3. Inside the loop, print the number (e.g., &quot;T-minus 10...&quot;).
# 4. After Loop: Print &quot;BLAST OFF! 


start_number = int(input("Enter the start number for the countdown: "))
for number in range(start_number, 0, -1):
    print(f"T-minus {number}...")           
print("BLAST OFF🚀🗿!") 
