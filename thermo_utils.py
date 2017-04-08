import csv

# Write out csv file, from list input
def csv_row_writer(outFile,inList):
    with open(outFile, 'wt') as csvfile:
        writeCsv = csv.writer(csvfile, delimiter=',',
                              quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for row in inList:
            writeCsv.writerow(row)

# Read in csv as list
def read_csv_rows(inFile):
    result = []
    with open(inFile, 'rt') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar="'")
        for row in rows:
            result.append(','.join(row))
    return result

# Generate list of letters (point labels)
# Starts at "A" and increments to a maximum of "ZZ"
def letter_incrementer(size):
    result = []
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letList = list(letters)
    for point in range(0,size):
        if point/26 >= 1:
            let1 = math.floor(point/26)-1
            let2 = point%26
            result.append(letList[let1]+letList[let2])
        else:
            result.append(letList[point])
    return result
