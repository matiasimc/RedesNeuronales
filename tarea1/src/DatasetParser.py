import csv

def parse_dataset(filename):
    ret = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            d = {}
            inp = []
            outl = [0,0]
            for s in row[1:-1]:
                inp.append(float(s))
            out = str(row[-1])
            if out == "N":
                outl[0] = 1
            else:
                outl[1] = 1
            d["input"] = inp
            d["output"] = outl
            ret.append(d)
    return ret
