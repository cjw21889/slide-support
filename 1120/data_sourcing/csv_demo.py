import csv

### BAD FORMAT
# csvfile = open('data/addresses.csv')
# reader = csv.reader(csvfile, skipinitialspace=True)
# for row in reader:
#     print(type(row))
# csvfile.close()


### GOOD FORMAT #### Use nested open statement to avoid file corruption
# TURN CSV INTO LIST OF LIST
with open('data/addresses.csv') as csvfile:
    ## csvfile is an IO text type
    reader = csv.reader(csvfile, skipinitialspace=True)
    ## reader is a csv.reader type, we can loop!
    for row in reader:
        # row is a `list`
        print(row)


# TURN CSV TO DICT
with open('data/biostats.csv', 'r') as csvfile:
    ## csvfile is an IO text type
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    ## reader is a csv.dictreader type, we can loop!
    for row in reader:
        # row is a dict
        print(row['Name'], row['Sex'], int(row['Age']))


beatles = [{
    'first_name': 'John',
    'last_name': 'lennon',
    'instrument': 'guitar'
}, {
    'first_name': 'Ringo',
    'last_name': 'Starr',
    'instrument': 'drums'
}]

## Writing from dict to CSV with headers
with open('data/beatles.csv', 'w') as csvfile:
    #csvfile is an io text writer ('w') use 'a' to append
    writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
    # our headers have been set to the keys of the first dict (not in file yet)
    writer.writeheader()
    # we write the headers into the file before we loop (only want them once)
    for beatle in beatles:
        #write row will just write the values from each dict
        writer.writerow(beatle)
