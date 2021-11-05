# words = ['cat', 'wolf', 'beetle']
# for _, word in enumerate(words, 10):
#     print(f"{_}, {word}")

# instruments = {'paul': 'bass', 'ringo': 'drums'}
# for key, instrument in instruments.items():
#     print(key, '-', instrument)
#     # print(f'{beatle.capitalize()} plays the {instrument}')


def full_name(first_name='Chris', last_name='Westerman', capitalize=False):
    if capitalize:
        return f"{first_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name} {last_name}"

print(full_name(last_name='james', first_name='phil', capitalize=False))

