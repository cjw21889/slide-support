import csv

# No headers
# with open('data/addresses.csv') as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     for row in reader:
#         # row is a `list`
#         print(row)

# Headers
# with open('data/biostats.csv') as csvfile:
#     reader = csv.DictReader(csvfile, skipinitialspace=True)
#     for row in reader:
#         # print(row)
#         # row is a collections.OrderedDict
#         # print(row.keys())
#         print(row['Name'], row['Sex'], int(row['Age']))


# Saving a CSV

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
