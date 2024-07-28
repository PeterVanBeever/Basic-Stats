def zmedian(data):
    sorted_data = sorted(data)
    n = len(data)
    midpoint = n // 2
    if n % 2 == 0:
        return (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2
    else:
        return sorted_data[midpoint]
