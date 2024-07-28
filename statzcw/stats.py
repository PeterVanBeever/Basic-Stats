from statzcw.count import zcount
from statzcw.mean import zmean
from statzcw.mode import zmode
from statzcw.median import zmedian
from statzcw.variance import zvariance
from statzcw.stddev import zstddev
from statzcw.stderr import zstderr
from statzcw.corr import zcorr

def readDataFile(file):
    print(f"Attempting to read file: {file}")  # Debug: print the file being read
    x, y = [], []
    with open(file) as f:
        f.readline()  # consume headers
        for l in f:
            row = l.strip().split(',')
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x, y)

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data
