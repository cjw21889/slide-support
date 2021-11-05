from helpers import generate_password  # Module import here

length = input("How long do you want your passowrd? ")

print(f'app.py name', __name__)
print(generate_password(int(length)))
