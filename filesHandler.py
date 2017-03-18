import csv
import argparse
 
parser.add_argument('-i','--input', help='Input file name',required=True)
 
print ("Input file: %s" % args.input )

import csv
with open(args.input, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print ', '.join(row)
