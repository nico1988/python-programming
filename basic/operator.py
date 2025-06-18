import operator
import logging

def add(x, y):
    """Add two numbers."""
    return operator.add(x, y)

def subtract(x, y):
    """Subtract two numbers."""
    return operator.sub(x, y)

def multiply(x, y):
    """Multiply two numbers."""
    return operator.mul(x, y)

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return operator.truediv(x, y)

def modulus(x, y):
    """Return the modulus of two numbers."""
    return operator.mod(x, y)

def power(x, y):
    """Raise x to the power of y."""
    return operator.pow(x, y)

def floor_divide(x, y):
    """Perform floor division of x by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return operator.floordiv(x, y)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.DEBUG)

def main():
    """Main function to demonstrate operator usage."""
    x = 10
    y = 5

    logging.info(f"Adding {x} and {y}: {add(x, y)}")
    logging.info(f"Subtracting {y} from {x}: {subtract(x, y)}")
    logging.info(f"Multiplying {x} and {y}: {multiply(x, y)}")
    logging.info(f"Dividing {x} by {y}: {divide(x, y)}")
    logging.info(f"Modulus of {x} and {y}: {modulus(x, y)}")
    logging.info(f"{x} raised to the power of {y}: {power(x, y)}")
    logging.info(f"Floor division of {x} by {y}: {floor_divide(x, y)}")

def operator_compare_example():
    """Example of using operator module for comparison."""
    a = 10
    b = 20
    logging.info(f"Is {a} less than {b}? {operator.lt(a, b)}")
    logging.info(f"Is {a} greater than {b}? {operator.gt(a, b)}")
    logging.info(f"Is {a} equal to {b}? {operator.eq(a, b)}")
    logging.info(f"Is {a} not equal to {b}? {operator.ne(a, b)}")
    logging.info(f"Is {a} less than or equal to {b}? {operator.le(a, b)}")
    logging.info(f"Is {a} greater than or equal to {b}? {operator.ge(a, b)}")

if __name__ == "__main__":
    main()

    operator_compare_example()