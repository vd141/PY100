import sys
import time
import random

def type_sequentially(text):
    for char in text:
        delay = random.randint(0,3)/10
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')  # Move to the next line after typing

# Example usage
type_sequentially("Hello, world!")