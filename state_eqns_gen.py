""" Generates form for defining the energy balance across individual
elements in the thermodynamic model
"""
import argparse

from thermo_utils import csv_row_writer, read_csv_rows

# Define list of intrinsic thermodynamic properties
PARAMS_THERM = ['h', 'T', 'P', 's']

# Read input/output arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True)
parser.add_argument('-o', '--output', required=True)
parser.add_argument('-v', '--version', required=False)
args = parser.parse_args()
print('Input file: %s' % args.input)

# Read in data from points CSV file
NESTED_PTS = read_csv_rows(args.input)

# Determine number of points in the points CSV file using first row length
LEN_PTS = len(NESTED_PTS[0].split(','))-1
print('Number of points: %s' % LEN_PTS)

# Generate equation rows, with each row being an energy balance across a
# component
OUT_ROWS = [['', '(Node)']
            +PARAMS_THERM
            +['']
            +PARAMS_THERM
            +['(Node)', '', 'Q', 'W']] # Column headers
for rowInd in range(0, LEN_PTS):
    outRow = ['Eqn ' + str(rowInd+1)]
    for paramInd in range(0, len(PARAMS_THERM)+1):
        outRow.append('')
    outRow.append('-')
    for paramInd in range(0, len(PARAMS_THERM)+1):
        outRow.append('')
    outRow.append('=')
    OUT_ROWS.append(outRow)

# Write all rows to equations CSV file
csv_row_writer(args.output, OUT_ROWS)
print('Output file: %s' % args.output)
