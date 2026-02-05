import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def process_data_with_logging(data_list):
    total = 0
    count = 0
   
    logging.debug(f"Starting process_data with data: {data_list}")
   
    for item in data_list:
        logging.debug(f"Processing item: {item}, Type: {type(item)}")
       
        if isinstance(item, (int, float)):
             total += item
             count += 1
             logging.debug(f"Item is number. Current total: {total}, count: {count}")
        else:
             
             logging.info(f"Skipping non-numeric item: {item}")
             logging.warning(f"Skipping unexpected non-numeric item: {item}")

    logging.debug(f"Loop finished. Final total: {total}, final count: {count}")
   
    if count == 0:
        logging.warning("No numeric items found, division by zero possible.")
        return 0
       
    try:
        average = total / count
        logging.info(f"Calculation complete. Average: {average}")
        return average
    except ZeroDivisionError:
        logging.error("Caught division by zero unexpectedly!", exc_info=True)
        return 0


data = [10, 20, "oops", 30, "error", 40.5]
result = process_data_with_logging(data)
print(f"Final average: {result}")


result_zero = process_data_with_logging(["not a number"])
print(f"Final average (zero case): {result_zero}")