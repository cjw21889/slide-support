import csv

# # csvfile = info inside data/address.csv
# with open('data/addresses.csv') as csvfile:
#     # pass our variable into the reader function
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     # iterate through the reader
#     for row in reader:
#         print(type(row))
#         # row is a `list`
#         print(row)

# # reading file saving it csvfile variable
# with open('data/biostats.csv') as csvfile:
#     # using the csv DictReader
#     reader = csv.DictReader(csvfile, skipinitialspace=True)
#     # iterating through reader
#     for row in reader:
#         # row is a collections.OrderedDict
#         # print(type(row))
#         print(row)
#         # print(row['Name'], row['Sex'], int(row['Age']))

beatles = [{
    'first_name': 'John',
    'last_name': 'lennon',
    'instrument': 'guitar'
}, {
    'last_name': 'Starr',
    'first_name': 'Ringo',
    'instrument': 'drums'
}]

# targeting end location in WRITE mode assigned csvfile
with open('data/beatles.csv', 'w') as csvfile:
    # use the dictWRITER function, and pass headers to fieldnames
    writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
    # write headers once knows to look at fieldnames
    writer.writeheader()
    for beatle in beatles:
        # writerow knows to look at dict values
        writer.writerow(beatle)
