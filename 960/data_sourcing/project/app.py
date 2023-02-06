import helpers.password as password # Module import here

# HERE is a simple app for generating passwords based on user needs
print('Welcome to the password generator')
size = input('How many characters does your password need? ')


print(password.generate_password(int(size)))

print('app file name')
print(__name__)
