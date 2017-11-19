""" Generates form to capture the thermodynamic state variables
at all established points in the system
"""
import argparse

from thermo_utils import csv_row_writer, letter_incrementer

# Read input/output arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', required=True)
parser.add_argument('-p', '--points', required=True)
args = parser.parse_args()
NUM_POINTS = int(args.points)

# Define mdot and intrinsic thermodynamic properties
PARAMS_POINTS = ['mdot', 'h', 'T', 'P', 's']

# Generate list/table with point labels as the column headers and intrinsic
# thermodyanmic properties (and mass flow) as the row headers
OUT_ROWS = []
OUT_ROWS.append(['']+letter_incrementer(NUM_POINTS)) # Column headers
for param in PARAMS_POINTS:
    OUT_ROWS.append([param]) # Additional rows

# Write rows to points file
csv_row_writer(args.output, OUT_ROWS)
print('Output file: %s' % args.output)
