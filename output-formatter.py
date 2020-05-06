#/usr/bin/python3

import argparse

# Retrieve file path from passed-in arguments
parser = argparse.ArgumentParser()
parser.add_argument("infile")
args = parser.parse_args()

# Attempt to open the file, read only, at the given file path
infile = None
try:
    infile = open(args.infile, 'rt', encoding='utf-8', errors='replace')
except FileNotFoundError as e:
    print("Error:' ",args.infile," 'could not be found.")
    exit()

# Read the file and parse the content
file_content = infile.read()
infile.close()
hdr_content, data_content = file_content.rsplit("KW\00", 1)
hdrs = hdr_content.split(',')
data = data_content.split('\00')

# Write data to formatted file
file_name = args.infile.split('.')[0] + ".csv"
outfile = open(file_name, 'w', encoding='utf-8',errors='ignore')
for i in range(len(data) - (len(data) % 4)):
    outfile.write(data[i])
    if (i+1) % 4:
        outfile.write(",")
    else:
        outfile.write("\n")

outfile.close()

print("New file created:", file_name)
