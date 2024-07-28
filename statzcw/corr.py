import math

def zcorr(listx, listy):
    mean_x = sum(listx) / len(listx)
    mean_y = sum(listy) / len(listy)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(listx, listy))
    denominator = math.sqrt(sum((x - mean_x) ** 2 for x in listx) * sum((y - mean_y) ** 2 for y in listy))
    return numerator / denominator
