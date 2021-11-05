# CRUD
beatles = ['john', 'paul', 'ringo']

# CREATE
beatles.append('george')
# print(beatles)

# READ
# print(beatles[1])

# UPDATE
beatles[0] = 'John'
# print(beatles)

# DESTROY
del beatles[-1]
# print(beatles)



instruments = {'john': 'guitar', 'paul': 'bass'}
# CREATE
instruments['ringo'] = 'drums'
# print(instruments)

# READ
print(instruments.get('john', 'john not found'))

# UPDATE
# instruments['john'] = 'vocals'
# print(instruments)

# DESTROY
# del instruments['paul']
# print(instruments)
