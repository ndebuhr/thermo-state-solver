# Thermo State Solver
# Solves for state parameters at various points in a simple thermodynamic model 
# Developed by Neal DeBuhr

import csv
import argparse
import itertools
import string

numPoints=int(input('Number of points in analysis:'))
num2alpha = dict(zip(range(1, 27), string.ascii_uppercase))
outRow=['']
outRows=[]
paramsPoints=['mdot','h','T','P','s']

parser = argparse.ArgumentParser()
parser.add_argument('-o','--output',required=True)
args = parser.parse_args()

for point in range(1,numPoints+1):
    outRow.append(num2alpha[point])
outRows.append(outRow)
for param in paramsPoints:
    outRows.append([param])

with open(args.output, 'wt') as csvfile:
    fileEqns = csv.writer(csvfile, delimiter=',',
                            quotechar="'", quoting=csv.QUOTE_MINIMAL)
    for row in outRows:
        fileEqns.writerow(row)

print("Output file: %s" % args.output)
