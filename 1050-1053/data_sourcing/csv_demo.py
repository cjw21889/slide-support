import csv

# csvfile = open('data/addresses.csv')
# csvfile.close()

# with open('data/addresses.csv') as csvfile:
#     # print(type(csvfile))
#     # print(dir(csvfile))
# reader = csv.reader(csvfile, skipinitialspace=True)
#     # print(type(reader))
#     # print(dir(reader))
#     for row in reader:
#         print(row[0])
#     #     # row is a `list`
#     #     print(row)


# with open('data/biostats.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile, skipinitialspace=True)
#     for row in reader:
#         # row is a collections.OrderedDict
#         print(row['Name'], row["Sex"], int(row['Age']))

beatles = [{
    'first_name': 'Chris',
    'last_name': 'Westerman',
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
