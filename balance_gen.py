import csv
import argparse
import itertools

from thermo_utils import csv_row_writer, read_csv_rows

# Read input/output arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i','--input',required=True)
parser.add_argument('-o','--output',required=True)
parser.add_argument('-v','--version',required=False)
args = parser.parse_args()
print('Input file: %s' % args.input)

# Read in data from points CSV file
nestedPts = read_csv_rows(args.input)

# Determine number of points in the points CSV file using first row length
lenPts = len(nestedPts[0].split(','))-1
print('Number of points: %s' % lenPts)

outRows=[]
# Generate table for full system energy balance
outRow = ['']
for eqnInd in range(0,lenPts):
    outRow.append('E'+str(eqnInd+1))
outRows.append(outRow) # Full system column headers
outRow = ['Balance']
outRows.append(outRow) # Full system row header

# Write all rows to equations CSV file
csv_row_writer(args.output,outRows)
print('Output file: %s' % args.output)
