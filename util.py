import random
import string

def generate_random_string(min_length=7, max_length=16):
    """Generate a random string of varying length between min_length and max_length."""
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
