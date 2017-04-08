import csv
import argparse
import itertools
import math

# Write out csv file, from list input
def csv_row_writer(outFile,inList):
    with open(args.output, 'wt') as csvfile:
        writeCsv = csv.writer(csvfile, delimiter=',',
                              quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for row in inList:
            writeCsv.writerow(row)

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

# Read input/output arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o','--output',required=True)
args = parser.parse_args()

# Define mdot and intrinsic thermodynamic properties
paramsPoints = ['mdot','h','T','P','s']

# Read in user specified number of points
numPoints = int(input('Number of points in analysis:'))
# TODO make number of points into execution argument

# Generate list/table with point labels as the column headers and intrinsic
# thermodyanmic properties (and mass flow) as the row headers 
outRows = []
outRows.append(['']+letter_incrementer(numPoints)) # Column headers
for param in paramsPoints:
    outRows.append([param]) # Additional rows

# Write rows to points file
csv_row_writer(args.output,outRows)
print('Output file: %s' % args.output)
