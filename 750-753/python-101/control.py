# age = int(input("How old are you?"))


# def my_response(age):
#     if age >= 21:
#         return "You can become president"
#     elif age >= 18:
#         return "You can vote"
#     return "Be patient!"

# print(my_response(age))

words = ['cat', 'wolf', 'beetle']
# upper_words = []
# for word in words:
#     upper_words.append(word.upper())

# print(upper_words)

# upper_words = [word.upper() for word in words]
# print(upper_words)

# for index, word in enumerate(words):
#     print(index, word.upper())


instruments = {'paul': 'bass', 'ringo': 'drums'}

for key, value in instruments.items():
    print(f'{key.capitalize()} plays the {value}')
