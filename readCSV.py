__author__ = 'Jaynt'

import os
import csv

print(os.getcwd())
inFiles = ["2001.csv", "2002.csv", "2003.csv", "2004.csv", "2005.csv", "2006.csv"]
outFiles = ["2001.csv", "2002.csv", "2003.csv", "2004.csv", "2005.csv", "2006.csv"]

inFiles = ["./data/Original/" + ifile for ifile in inFiles]
outFiles = ["./data/Edited/" + ofile for ofile in outFiles]
print(inFiles)
print(outFiles)
for inFile, outFile in zip(inFiles, outFiles):
    with open(inFile, 'r') as f, open(outFile, 'w') as newFile:

        # Read the first line and get the index of required variables
        head = f.readline().split(",")
        print(len(head))
        header = {j: i for i, j in enumerate(head)}
        reqVars = ['Year', 'Trade Flow Code', 'Reporter Code', 'Partner Code', 'Commodity Code', 'Trade Value (US$)']
        reqInd = [header[el] for el in reqVars]

        # Write the header on a new file
        wr = csv.writer(newFile, quoting=csv.QUOTE_ALL)
        wr.writerow(reqVars)

        totLines = 0
        reader = csv.reader(f)
        for line in reader:

            newline = [line[j] for j in reqInd]

            if len(newline[4]) == 2:
                wr.writerow(newline)
            totLines += 1
            if totLines % 1000000 == 0:   # Monitor the progress
                print(totLines)

    print(str(totLines) + " " + outFile)


