def readDataSets(filenames):
    datasets = {}
    for filename in filenames:
        with open(filename, 'r') as file:
            lines = file.readlines()
            x_data = []
            y_data = []
            for line in lines:
                x, y = map(float, line.strip().split(','))
                x_data.append(x)
                y_data.append(y)
            datasets[filename] = (x_data, y_data)
    return datasets
