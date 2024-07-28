import sys
import os
from collections import Counter

# Add the parent directory containing statzcw to the path
module_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(module_path)
sys.path.append(parent_path)
print("Module path:", module_path)  # Debug: print the module path
print("Parent path:", parent_path)  # Debug: print the parent path
print("sys.path:", sys.path)  # Debug: print the sys.path

from statzcw.stats import readDataSets, zcount, zmean, zvariance, zcorr, zmedian, zstddev, zstderr

def zmode(data):
    counter = Counter(data)
    modes = counter.most_common()
    max_count = modes[0][1]

    # If the highest frequency is 1, it means all values are unique
    if max_count == 1:
        return None
    
    # Filter all items with the highest frequency
    mode_list = [item for item, count in modes if count == max_count]
    
    # If there's only one mode, return it. Otherwise, return the list of modes.
    if len(mode_list) == 1:
        return mode_list[0]
    else:
        return mode_list

def print_statistics(datasets):
    for name, (x, y) in datasets.items():
        print(f"Dataset: {name}")
        print(f"Count of X: {zcount(x)}")
        print(f"Count of Y: {zcount(y)}")
        print(f"Mean of X: {zmean(x):.2f}")
        print(f"Sample Variance of X: {zvariance(x):.2f}")
        print(f"Mean of Y: {zmean(y):.2f}")
        print(f"Sample Variance of Y: {zvariance(y):.2f}")
        print(f"Correlation between X and Y: {zcorr(x, y):.2f}")
        print(f"Median of X: {zmedian(x):.2f}")
        print(f"Median of Y: {zmedian(y):.2f}")

        mode_x = zmode(x)
        mode_y = zmode(y)
        
        print(f"Mode of X: {mode_x if mode_x else 'No mode'}")
        print(f"Mode of Y: {mode_y if mode_y else 'No mode'}")

        print(f"Sample Std deviation of X: {zstddev(x):.2f}")
        print(f"Sample Std deviation of Y: {zstddev(y):.2f}")
        print(f"Standard Error of the Mean of X: {zstderr(x):.2f}")
        print(f"Standard Error of the Mean of Y: {zstderr(y):.2f}")
        print()

if __name__ == "__main__":
    # Default file paths if no arguments are provided
    default_files = [
        "/Users/peter/Dev/Basic-Stats/dataOne.csv",
        "/Users/peter/Dev/Basic-Stats/dataTwo.csv",
        "/Users/peter/Dev/Basic-Stats/dataThree.csv",
        "/Users/peter/Dev/Basic-Stats/dataZero.csv"
    ]
    
    filenames = sys.argv[1:] if len(sys.argv) > 1 else default_files
    
    # Debug: print the filenames being read
    print("Filenames:", filenames)
    
    if not filenames:
        print("No files provided. Please provide file paths as command line arguments.")
        sys.exit(1)
    
    try:
        datasets = readDataSets(filenames)
        print_statistics(datasets)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
