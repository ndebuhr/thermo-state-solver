import csv
import argparse
import itertools

from thermo_utils import csv_row_writer, read_csv_rows

# Read input/output arguments
parser = argparse.ArgumentParser()
parser.add_argument('-ip','--inputpoints',required=True)
parser.add_argument('-ie','--inputeqns',required=True)
parser.add_argument('-ib','--inputbalance',required=True)
parser.add_argument('-v','--version',required=False)
args = parser.parse_args()
print('Input points file: %s' % args.inputpoints)
print('Input equations file: %s' % args.inputeqns)
print('Input balance file: %s' % args.inputbalance)

# Read in files
filePts = read_csv_rows(args.inputpoints)
fileEqns = read_csv_rows(args.inputeqns)
fileBal = read_csv_rows(args.inputbalance)

# Pull horizontal property vectors from points file
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

# Pull vertical property vectors from equations file
for eqnsRow in range(0,len(fileEqns)):
    fileEqns[eqnsRow]=fileEqns[eqnsRow].split(',')
    if eqnsRow>0:
        for eqnsCol in range(0,len(fileEqns[eqnsRow])):
            if fileEqns[eqnsRow][eqnsCol]=='-':
                splitPoint=eqnsCol
node_A=['node_A']
h_A=['h_A']
T_A=['T_A']
P_A=['P_A']
s_A=['s_A']
node_B=['node_B']
h_B=['h_B']
T_B=['T_B']
P_B=['P_B']
s_B=['s_B']
Q_C=['Q_C']
W_C=['W_C']

for eqnsRow in range(0,len(fileEqns)):
    if eqnsRow>0:
        for eqnsCol in range(0,len(fileEqns[eqnsRow])):
            if eqnsCol<splitPoint:
                if fileEqns[0][eqnsCol]=='(Node)':
                    node_A.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='h':
                    h_A.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='T':
                    T_A.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='P':
                    P_A.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='s':
                    s_A.append(fileEqns[eqnsRow][eqnsCol])
            if eqnsCol>splitPoint:
                if fileEqns[0][eqnsCol]=='(Node)':
                    node_B.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='h':
                    h_B.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='T':
                    T_B.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='P':
                    P_B.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='s':
                    s_B.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='Q':
                    Q_C.append(fileEqns[eqnsRow][eqnsCol])
                elif fileEqns[0][eqnsCol]=='W':
                    W_C.append(fileEqns[eqnsRow][eqnsCol])

print(node_A)
print(h_A)
print(T_A)
print(P_A)
print(s_A)
print(node_B)
print(h_B)
print(T_B)
print(P_B)
print(s_B)
print(Q_C)
print(W_C)
