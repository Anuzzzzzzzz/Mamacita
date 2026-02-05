import monday
import  data

print("Running main_program.py")

print(data.APP_NAME)

message = monday.greet("BIT Student")
print(message)

sum_result = monday.add_numbers(10, 25)
print(f"The sum is: {sum_result}")

print(f"Value of PI: {data.PI}")

area = monday.calculate_area(4)
print("Area of circle:", area)
