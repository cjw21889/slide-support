# CRUD
# LISTS
beatles = ['john', 'paul', 'ringo']

# CREATE
beatles.append('george')

# READ
beatles[0] #first item
beatles[-1] #last item
beatles[-2] #2nd to last item
beatles[0:2] #returns index 0 and 1

# UPDATE
beatles[0] = 'John'

# DESTROY
del beatles[0] #Deletes first item and re-indexs


instruments = {'john': 'guitar', 'paul': 'bass'}  # Keys are `str`, Values too

# CREATE
instruments['ringo'] = 'drums' #just define

# READ
instruments['john']

# UPDATE
instruments['john'] = 'voice'

# DESTROY
del instruments['paul']

















