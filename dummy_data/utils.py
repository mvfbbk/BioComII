import csv


def read_enzymes(filename):
    d = {}

    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        rows = [row for row in reader]

        if len(rows[0]) is not len(rows[1]):
            print("ERROR")
            exit(-1)
        
        for i in range(len(rows[0])):
            k = rows[1][i]
            v = rows[0][i]
            d[k] = v

        return d
                