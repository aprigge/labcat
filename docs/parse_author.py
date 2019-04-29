import os
import csv
import sys

res = []
with open(sys.argv[1], mode='r') as input_file, open("output.csv", mode='w') as output_file:
    content = csv.reader(input_file, delimiter=',')
    for row in content:
        if (len(row) > 8):
            author = row[8]
            author = author.replace("&", "|")
            author = author.replace("and", "|")
            author = author.replace(";", "|")
            row[8] = author

        res.append(row)

    print("Writing to file")
    output = csv.writer(output_file, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for rows in res:
        output.writerow(rows)
