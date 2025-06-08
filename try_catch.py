# error catching in Python
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: {e}. Cannot divide by zero.")
        return None
    except TypeError as e:
        print(f"Error: {e}. Please provide numbers.")
        return None
    else:
        return result

# Example usage
print(divide_numbers(10, 2))  # Should print 5.0
print(divide_numbers(10, 0))  # Should print an error message
print(divide_numbers(10, 'a'))  # Should print an error message 