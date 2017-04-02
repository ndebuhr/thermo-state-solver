# Thermo State Solver
# Solves for state parameters at various points in a simple thermodynamic model 
# Developed by Neal DeBuhr

import csv
import argparse
import itertools

def csv_row_writer(outFile,inList):
    with open(args.output, 'wt') as csvfile:
        writeCsv = csv.writer(csvfile, delimiter=',',
                              quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for row in inList:
            writeCsv.writerow(row)

def read_csv_rows(inFile):
    result = []
    with open(inFile, 'rt') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar="'")
        for row in rows:
            result.append(','.join(row))
    return result

paramsTherm = ['h','T','P','s']

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input',required=True)
parser.add_argument('-o','--output',required=True)
args = parser.parse_args()

print('Input file: %s' % args.input)

nestedPts = read_csv_rows(args.input)

lenPts = len(nestedPts[0].split(','))-1
print('Number of points: %s' % lenPts)

outRows = [['','(Node)']+paramsTherm+['']+paramsTherm+['(Node)','','Q','W']]
for rowInd in range(0,lenPts):
    outRow = ['Eqn ' + str(rowInd+1)]
    for paramInd in range(0,len(paramsTherm)+1):
        outRow.append('')
    outRow.append('-')
    for paramInd in range(0,len(paramsTherm)+1):
        outRow.append('')
    outRow.append('=')
    outRows.append(outRow)
outRows.append([''])
outRow = ['']
for eqnInd in range(0,lenPts):
    outRow.append('E'+str(eqnInd+1))
outRows.append(outRow)
outRow = ['Balance']
outRows.append(outRow)

csv_row_writer(args.output,outRows)

print('Output file: %s' % args.output)
