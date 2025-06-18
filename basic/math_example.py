import math
import logging

def math_example():
    """
    Example function to demonstrate basic math operations.
    """
    # Calculate square root
    sqrt_value = math.sqrt(16)
    
    # Calculate factorial
    factorial_value = math.factorial(5)
    
    # Calculate sine of 30 degrees
    sine_value = math.sin(math.radians(30))

    
    return sqrt_value, factorial_value, sine_value

if __name__ == "__main__":
    sqrt_value, factorial_value, sine_value = math_example()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"Square root of 16: {sqrt_value}")
    logging.info(f"Factorial of 5: {factorial_value}")
    logging.info(f"Sine of 30 degrees: {sine_value}")
    # logging another example of math
    logging.info(f"Pi value: {math.pi}")
    logging.info(f"Euler's number: {math.e}")
    logging.info(f"Cosine of 60 degrees: {math.cos(math.radians(60))}")
    logging.info(f"Logarithm base 10 of 100: {math.log10(100)}")
    logging.info(f"Exponential of 2: {math.exp(2)}")
    logging.info(f"Ceiling of 4.2: {math.ceil(4.2)}")
    logging.info(f"Floor of 4.8: {math.floor(4.8)}")
    logging.info(f"Greatest common divisor of 48 and 18: {math.gcd(48, 18)}")
    logging.info(f"Least common multiple of 4 and 6: {math.lcm(4, 6)}")
    logging.info(f"Power of 2 raised to 3: {math.pow(2, 3)}")
    logging.info(f"Trigonometric tangent of 45 degrees: {math.tan(math.radians(45))}")
    logging.info(f"Hyperbolic sine of 1: {math.sinh(1)}")
    logging.info(f"Hyperbolic cosine of 1: {math.cosh(1)}")
    logging.info(f"Hyperbolic tangent of 1: {math.tanh(1)}")