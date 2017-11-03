"""Parses points, equations, and energy balance files"""
import argparse

from thermo_utils import read_csv_rows

# Read input/output arguments
PARSER = argparse.ArgumentParser()
PARSER.add_argument('-ip', '--inputpoints', required=True)
PARSER.add_argument('-ie', '--inputeqns', required=True)
PARSER.add_argument('-ib', '--inputbalance', required=True)
PARSER.add_argument('-v', '--version', required=False)
ARGS = PARSER.parse_args()
print('Input points file: %s' % ARGS.inputpoints)
print('Input equations file: %s' % ARGS.inputeqns)
print('Input balance file: %s' % ARGS.inputbalance)

# Read in files
FILE_PTS = read_csv_rows(ARGS.inputpoints)
FILE_EQNS = read_csv_rows(ARGS.inputeqns)
FILE_BAL = read_csv_rows(ARGS.inputbalance)

# Pull horizontal property vectors from points file
for ptsRow in range(0, len(FILE_PTS)):
    FILE_PTS[ptsRow] = FILE_PTS[ptsRow].split(',')
    if ptsRow > 0:
        if FILE_PTS[ptsRow][0] == 'mdot':
            mdot_v = FILE_PTS[ptsRow]
        elif FILE_PTS[ptsRow][0] == 'h':
            h_v = FILE_PTS[ptsRow]
        elif FILE_PTS[ptsRow][0] == 'T':
            T_v = FILE_PTS[ptsRow]
        elif FILE_PTS[ptsRow][0] == 'P':
            P_v = FILE_PTS[ptsRow]
        elif FILE_PTS[ptsRow][0] == 's':
            s_v = FILE_PTS[ptsRow]

# Pull vertical property vectors from equations file
for eqnsRow in range(0, len(FILE_EQNS)):
    FILE_EQNS[eqnsRow] = FILE_EQNS[eqnsRow].split(',')
    if eqnsRow > 0:
        for eqnsCol in range(0, len(FILE_EQNS[eqnsRow])):
            if FILE_EQNS[eqnsRow][eqnsCol] == '-':
                splitPoint = eqnsCol
NODE_A = ['node_A']
h_A = ['h_A']
T_A = ['T_A']
P_A = ['P_A']
s_A = ['s_A']
NODE_B = ['node_B']
h_B = ['h_B']
T_B = ['T_B']
P_B = ['P_B']
s_B = ['s_B']
Q_C = ['Q_C']
W_C = ['W_C']

for eqnsRow in range(0, len(FILE_EQNS)):
    if eqnsRow > 0:
        for eqnsCol in range(0, len(FILE_EQNS[eqnsRow])):
            if eqnsCol < splitPoint:
                if FILE_EQNS[0][eqnsCol] == '(Node)':
                    NODE_A.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 'h':
                    h_A.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 'T':
                    T_A.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 'P':
                    P_A.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 's':
                    s_A.append(FILE_EQNS[eqnsRow][eqnsCol])
            if eqnsCol > splitPoint:
                if FILE_EQNS[0][eqnsCol] == '(Node)':
                    NODE_B.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 'h':
                    h_B.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 'T':
                    T_B.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 'P':
                    P_B.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 's':
                    s_B.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 'Q':
                    Q_C.append(FILE_EQNS[eqnsRow][eqnsCol])
                elif FILE_EQNS[0][eqnsCol] == 'W':
                    W_C.append(FILE_EQNS[eqnsRow][eqnsCol])

print(NODE_A)
print(h_A)
print(T_A)
print(P_A)
print(s_A)
print(NODE_B)
print(h_B)
print(T_B)
print(P_B)
print(s_B)
print(Q_C)
print(W_C)
