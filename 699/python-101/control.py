def my_age(age):
    if age >= 21:
        return "You can vote"
    if age >= 18:
        return "You can become president"
    return "Be patient!"

age = int(input("How old are you?"))
my_status = my_age(age)
print(my_status)





# words = ['cat', 'wolf', 'beetle']
# upper_words =[]
# for x in words:
#     upper_words.append(x.upper())

# upper_words = [x.upper() for x in words]
# print(upper_words)

# for word, index in enumerate(words):
#     print(index, word)


# instruments = {'paul': 'bass', 'ringo': 'drums'}

# for beatle, instrument in instruments.items():
#     print(f'{beatle.capitalize()} plays the {instrument}')


# def full_name(first_name, last_name='westerman', capitalize=False):
#     if capitalize:
#         return f"{first_name.capitalize()} {last_name.capitalize()}"
#     else:
#         return f"{first_name} {last_name}"


# print(full_name('chris', False, 'westerman'))


