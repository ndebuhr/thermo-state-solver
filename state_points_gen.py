# Thermo State Solver
# Solves for state parameters at various points in a simple thermodynamic model
# Developed by Neal DeBuhr

import csv
import argparse
import itertools
import math

def csv_row_writer(outFile,inList):
    with open(args.output, 'wt') as csvfile:
        writeCsv = csv.writer(csvfile, delimiter=',',
                              quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for row in inList:
            writeCsv.writerow(row)

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

parser = argparse.ArgumentParser()
parser.add_argument('-o','--output',required=True)
args = parser.parse_args()

paramsPoints = ['mdot','h','T','P','s']
outRows = []

numPoints = int(input('Number of points in analysis:'))

outRows.append(['']+letter_incrementer(numPoints))
for param in paramsPoints:
    outRows.append([param])

csv_row_writer(args.output,outRows)

print('Output file: %s' % args.output)
