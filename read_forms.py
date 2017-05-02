import csv
import argparse
import itertools

from thermo_utils import csv_row_writer, read_csv_rows

# Read input/output arguments
parser = argparse.ArgumentParser()
parser.add_argument('-ip','--inputpoints',required=True)
parser.add_argument('-ie','--inputeqns',required=True)
parser.add_argument('-v','--version',required=False)
args = parser.parse_args()
print('Input points file: %s' % args.inputpoints)
print('Input equations file: %s' % args.inputeqns)

# Read in points file
filePts = read_csv_rows(args.inputpoints)

# Read in equations file
fileEqns = read_csv_rows(args.inputeqns)

# Create horizontal property vectors from points file
for ptsRow in range(0,len(filePts)):
    filePts[ptsRow]=filePts[ptsRow].split(',')
    if ptsRow>0:
        if filePts[ptsRow][0]=='mdot':
            mdot_v=filePts[ptsRow]
        elif filePts[ptsRow][0]=='h':
            h_v=filePts[ptsRow]
        elif filePts[ptsRow][0]=='T':
            T_v=filePts[ptsRow]
        elif filePts[ptsRow][0]=='P':
            P_v=filePts[ptsRow]
        elif filePts[ptsRow][0]=='s':
            s_v=filePts[ptsRow]

print(mdot_v)
print(h_v)
print(T_v)
print(P_v)
print(s_v)

# Create vertical property vectors from equations file
for eqnsRow in range(0,len(fileEqns)):
    fileEqns[eqnsRow]=fileEqns[eqnsRow].split(',')
    if eqnsRow>0:
        for eqnsCol in range(0,len(fileEqns[eqnsRow])):
            print(fileEqns[0][eqnsCol])
    
