import random
import string


def generate_password(size):
    """Generate a random lowercase ASCII password of given size"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))



# print(generate_password(5))


# print("password file name")
# print(__name__)

if __name__ == '__main__':
    print(generate_password(5))
    print(generate_password(10))
    print(generate_password(0))
