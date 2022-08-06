import csv


# # BAD BAD SYNTAX
# csvfile = open('data/addresses.csv')
# # print(type(csvfile))
# readfile = csv.reader(csvfile)
# print(type(readfile))
# # print(dir(readfile))
# for row in readfile:
#     print(readfile.line_num, '- ', row)

# GOOD SYNTAX
# with open('data/addresses.csv') as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     for row in reader:
#         # row is a `list`
#         print(row)


# with open('data/biostats.csv') as csvfile:
#     # print(type(csvfile))
#     reader = csv.DictReader(csvfile, skipinitialspace=True)
#     # print(type(reader))
#     for row in reader:
#         # print(type(row))
#          # row is a collections.OrderedDict

#         print(row['Name'], row['Sex'], int(row['Age']))


beatles = [
    { 'first_name': 'John', 'last_name': 'lennon', 'instrument': 'guitar'},
    { 'first_name': 'Ringo', 'last_name': 'Starr', 'instrument': 'drums'}
]

with open('data/beatles.csv', 'w') as csvfile:
    print(type(csvfile))
    writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
    print(type(writer))
    # writer.writeheader()
    for beatle in beatles:
          writer.writerow(beatle)
