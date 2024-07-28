import pytest
from statzcw.stats import zcount, zmean, zmode, zmedian, zvariance, readDataSets

def test_zcount():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert zcount(data) == 5

def test_zmean():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert zmean(data) == 3.0

def test_zmode():
    data = [1.0, 2.0, 2.0, 4.0, 5.0]
    assert zmode(data) == 2.0

def test_zmedian():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert zmedian(data) == 3.0
    data = [1.0, 2.0, 2.0, 4.0, 5.0]
    assert zmedian(data) == 2.0

def test_zvariance():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert round(zvariance(data), 2) == 2.5

def test_readDataSets():
    # Assuming you have sample CSV files in the root directory.
    filenames = ["dataOne.csv", "dataThree.csv"]
    datasets = readDataSets(filenames)
    assert "dataOne.csv" in datasets
    assert "dataThree.csv" in datasets
