from logging_cus import logger
import hashlib

def hash_demo():
    # Example string to hash
    example_string = "Hello, World!"
    
    # Create a SHA-256 hash of the string
    sha256_hash = hashlib.sha256(example_string.encode()).hexdigest()
    
    # Log the hash
    logger.info("SHA-256 Hash: %s", sha256_hash)

    # md5 hash hexdigest
    logger.info("MD5 Hash: %s", hashlib.md5(example_string.encode()).hexdigest())
    # md5 hash digest
    logger.info("MD5 Digest: %s", hashlib.md5(example_string.encode()).digest())

    # sha1 hash
    logger.info("SHA-1 Hash: %s", hashlib.sha1(example_string.encode()).hexdigest())

    # sha512 hash
    logger.info("SHA-512 Hash: %s", hashlib.sha512(example_string.encode()).hexdigest())

if __name__ == "__main__":
    hash_demo()