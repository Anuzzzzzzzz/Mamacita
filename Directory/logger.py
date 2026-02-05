def process_data(data_list):
    total = 0
    count = 0

    print(f"DEBUG: Starting process_data with data: {data_list}")

    for item in data_list:
       
        print(f"DEBUG: Processing item: {item}, Type: {type(item)}")
       
        # Let's add a check, but maybe make another mistake
        if isinstance(item, (int, float)):
             total += item
             count += 1
             
             print(f"DEBUG: Item is number. Current total: {total}, count: {count}")
             
        else:
             print(f"DEBUG: Skipping non-numeric item: {item}")
             
    print(f"DEBUG: Loop finished. Final total: {total}, final count: {count}")
   
    if count == 0:
       
        print("DEBUG: No numeric items found, division by zero possible.")
       
        return 0
       
    average = total / count

    print(f"DEBUG: Calculation complete. Average: {average}")

    return average

# Test with mixed data
data = [10, 20, "oops", 30, "error", 40.5]

result = process_data(data)
print(f"Final average: {result}")