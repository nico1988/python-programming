from logging_cus import logger
import hashlib

def hash_demo():
    # Example string to hash
    example_string = "Hello, World!"
    
    # Create a SHA-256 hash of the string
    sha256_hash = hashlib.sha256(example_string.encode()).hexdigest()
    
    # Log the hash
    logger.info("SHA-256 Hash: %s", sha256_hash)

if __name__ == "__main__":
    hash_demo()