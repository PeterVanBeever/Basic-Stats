import math

def zstderr(data):
    stddev = sum((x - sum(data) / len(data)) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(stddev) / math.sqrt(len(data))
