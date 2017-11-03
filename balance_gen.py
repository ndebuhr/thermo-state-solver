"""Generates energy balance table template in csv format"""
import argparse

from thermo_utils import csv_row_writer, read_csv_rows

# Read input/output arguments
PARSER = argparse.ArgumentParser()
PARSER.add_argument('-i', '--input', required=True)
PARSER.add_argument('-o', '--output', required=True)
PARSER.add_argument('-v', '--version', required=False)
ARGS = PARSER.parse_args()
print('Input file: %s' % ARGS.input)

# Read in data from points CSV file
NESTED_PTS = read_csv_rows(ARGS.input)

# Determine number of points in the points CSV file using first row length
LEN_PTS = len(NESTED_PTS[0].split(','))-1
print('Number of points: %s' % LEN_PTS)

OUT_ROWS = []
# Generate table for full system energy balance
OUT_ROW = ['']
for eqnInd in range(0, LEN_PTS):
    OUT_ROW.append('E'+str(eqnInd+1))
OUT_ROWS.append(OUT_ROW) # Full system column headers
OUT_ROW = ['Balance']
OUT_ROWS.append(OUT_ROW) # Full system row header

# Write all rows to equations CSV file
csv_row_writer(ARGS.output, OUT_ROWS)
print('Output file: %s' % ARGS.output)
