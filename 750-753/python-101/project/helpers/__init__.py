import random
import string


def generate_password(size):
    """Generate a random lowercase ASCII password of given size"""
    letters = string.ascii_lowercase
    import ipdb; ipdb.set_trace()
    return ''.join(random.choice(letters) for i in range(size))
