# from collections import Counter

# def zmode(data):
#     frequency = Counter(data)
#     max_freq = max(frequency.values())
    

#     if max_freq == 1:
#         return None
    
#     modes = [key for key, value in frequency.items() if value == max_freq]
#     return modes[0] if len(modes) == 1 else modes1
def zcount(data):
    count = 0
    for _ in data:
        count += 1
    return count

def zmean(data):
    total = 0
    count = zcount(data)
    for value in data:
        total += value
    return total / count

def zmode(data):
    # Step 1: Create a list of unique elements and their frequencies
    unique_elements = []
    frequencies = []
    
    i = 0
    while i < zcount(data):
        found = False
        j = 0
        while j < zcount(unique_elements):
            if data[i] == unique_elements[j]:
                frequencies[j] += 1
                found = True
                break
            j += 1
        if not found:
            unique_elements.append(data[i])
            frequencies.append(1)
        i += 1
    
    # Step 2: Find the maximum frequency manually
    max_freq = -1
    i = 0
    while i < zcount(frequencies):
        if frequencies[i] > max_freq:
            max_freq = frequencies[i]
        i += 1
    
    # Step 3: Find the mode(s) manually
    modes = []
    i = 0
    while i < zcount(unique_elements):
        if frequencies[i] == max_freq:
            modes.append(unique_elements[i])
        i += 1
    
    # Step 4: Return the mode or modes
    if max_freq == 1:
        return None
    return modes[0] if zcount(modes) == 1 else modes