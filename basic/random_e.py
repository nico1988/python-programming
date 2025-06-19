import random
from logging_cus import logger

logger.info("Random integer between 1 and 10: %d", random.randint(1, 10))
logger.info("Random float between 0 and 1: %f", random.random())
logger.info("Random choice from a list: %s", random.choice(['apple', 'banana', 'cherry']))
logger.info("Random sample of 2 elements from a list: %s", random.sample(['apple', 'banana', 'cherry', 'date'], 2))