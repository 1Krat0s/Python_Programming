def create_message(*args, **kwargs):
    pass

def process_numbers(*args):
    if not args:
        return 0
    operation = args[-1]
    if operation == "sum":
        return sum(args[:-1])
    elif operation == "product":
        result = 1
        for num in args[:-1]:
            result *= num
        return result
    elif operation == "max":
        return max(args[:-1])
    return None

print(process_numbers(1, 2, 3, 4, "sum"))
print(process_numbers(1, 2, 3, 4, "product"))
print(process_numbers(1, 2, 3, 4, 100, "max"))
print(process_numbers(1, 2, 3, 4, -1, 9, "average"))
print(create_message("1", "2", "Hello", separator = "-"))