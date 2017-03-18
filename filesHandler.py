# Thermo State Solver
# Solves for state parameters at various points in a simple thermodynamic model 
# Developed by Neal DeBuhr

import csv
import argparse
import itertools

paramsTherm=['h','T','P','s']

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input',required=True)
parser.add_argument('-o','--output',required=True)
args = parser.parse_args()

print("Input file: %s" % args.input)

nestedPts=[]
with open(args.input, 'rt') as csvfile:
    filePts = csv.reader(csvfile, delimiter=',', quotechar="'")
    for row in filePts:
        nestedPts.append(','.join(row))

lenPts=len(nestedPts[0].split(','))-1
print("Number of points: %s" % lenPts)

outRows=[['','Node']+paramsTherm+['']+paramsTherm+['Node']]
for rowInd in range(0,lenPts):
    outRow=['Eqn ' + str(rowInd+1)]
    for paramInd in range(0,len(paramsTherm)+1):
        outRow.append('')
    outRow.append('=')
    for paramInd in range(0,len(paramsTherm)+1):
        outRow.append('')
    outRows.append(outRow)

with open(args.output, 'wt') as csvfile:
    fileEqns = csv.writer(csvfile, delimiter=',',
                            quotechar="'", quoting=csv.QUOTE_MINIMAL)
    for row in outRows:
        fileEqns.writerow(row)
