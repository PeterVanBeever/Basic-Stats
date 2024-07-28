import math

def zstddev(data):
    variance = sum((x - sum(data) / len(data)) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)