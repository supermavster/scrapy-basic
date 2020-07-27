# # Generate the first 100 numbers pairs
# Pairs: [num for num in range(100) if num % 2 == 0]
def check_value(num):
    value = num if num % 2 == 0 else None
    yield value

def start(range_items):
    response = list()
    for num in range(range_items):
        value = next(check_value(num))
        if value is not None:
            response.append(value)
    print(f"The pair number of the range {range_items} is:\n{response}")

# Start Process
range_items = 100
start(range_items)
