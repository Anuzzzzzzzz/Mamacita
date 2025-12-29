

# Conversion Functions
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

# Temperature Warning
def warning(c):
    if c <= 0:
        return "Freezing point!"
    elif c >= 100:
        return "Boiling point!"
    else:
        return ""

# History list
history = []

# Simple menu loop
while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Show History")
    print("6. Exit")
    
    choice = input("Choose option (1-6): ")
    
    if choice == "1":
        c = float(input("Enter Celsius: "))
        f = c_to_f(c)
        msg = f"{c}°C = {f:.2f}°F {warning(c)}"
        print(msg)
        history.append(msg)
        
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        c = f_to_c(f)
        msg = f"{f}°F = {c:.2f}°C {warning(c)}"
        print(msg)
        history.append(msg)
        
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        k = c_to_k(c)
        msg = f"{c}°C = {k:.2f}K {warning(c)}"
        print(msg)
        history.append(msg)
        
    elif choice == "4":
        k = float(input("Enter Kelvin: "))
        if k < 0:
            print("Kelvin cannot be negative!")
            continue
        c = k_to_c(k)
        msg = f"{k}K = {c:.2f}°C {warning(c)}"
        print(msg)
        history.append(msg)
        
    elif choice == "5":
        print("\n--- Conversion History ---")
        for record in history:
            print(record)
            
    elif choice == "6":
        print("Exiting. Goodbye!")
        break
        
    else:
        print("Invalid choice! Pick 1-6.")
