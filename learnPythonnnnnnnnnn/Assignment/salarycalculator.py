# Task 8.1: The Salary Calculator
# Scenario: HR needs a reusable tool to calculate monthly
# salary based on hours worked and tax.
# Instructions:
# 1. Define a function calculate_salary(hours,
# hourly_rate).
# 2. Logic: Calculate gross = hours * hourly_rate.
# 3. Apply Tax: If gross &gt; 5000, deduct 10%. Otherwise, deduct
# 5%.
# 4. Return the final net salary.
# 5. Call the function twice with different values (e.g., John
# worked 40hrs @ 100, Jane worked 60hrs @ 200)and print the result

def calculate_salary(hours, hourly_rate):
    gross = hours * hourly_rate
    if gross > 5000:
        net_salary = gross * 0.9  # Deduct 10%
    else:
        net_salary = gross * 0.95  # Deduct 5%
    return net_salary
# Calling the function for John
john_salary = calculate_salary(40, 100)
print(f"John's Net Salary: ${john_salary}")
# Calling the function for Jane
jane_salary = calculate_salary(60, 200)
print(f"Jane's Net Salary: ${jane_salary}")
