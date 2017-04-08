import csv
import argparse
import itertools
import math

from thermo_utils import csv_row_writer, letter_incrementer

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