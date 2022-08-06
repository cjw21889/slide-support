import csv

# BAD FORMAT
# opened_file = open('data/addresses.csv')
# read_file = csv.reader(opened_file, skipinitialspace=True)
# # print(type(read_file))
# for row in read_file:
#     print(row)
# opened_file.close()



# GOOD FORMAT
# with open('data/addresses.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     for row in reader:
#         # row is a `list`
#         print(row)

# print('hello')

# with open('data/biostats.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile, skipinitialspace=True)
#     print(type(reader))
#     for row in reader:
#         # row is a collections.OrderedDict
#         print(type(row))
#         print(row['Name'], row['Sex'], int(row['Age']))


beatles = [{
    'first_name': 'John',
    'last_name': 'lennon',
    'instrument': 'guitar'
}, {
    'first_name': 'Ringo',
    'last_name': 'Starr',
    'instrument': 'drums'
}]

with open('data/beatles.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
    writer.writeheader()
    for beatle in beatles:
        writer.writerow(beatle)
