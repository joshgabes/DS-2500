# LAB EXERCISE 07
import pandas as pd
import math


# PROBLEM 1
def compute_zscore(numbers):
    """Return z-scores using the sample standard deviation."""
    mean = sum(numbers) / len(numbers)

    squared_diff = 0
    for number in numbers:
        squared_diff += (number - mean) ** 2

    std = math.sqrt(squared_diff / (len(numbers) - 1))

    zscores = []
    for number in numbers:
        zscores.append((number - mean) / std)

    return zscores


# PROBLEM 2
def compute_mms(numbers):
    """Return the numbers scaled to the range from 0 to 1."""
    minimum = min(numbers)
    maximum = max(numbers)

    scaled = []
    for number in numbers:
        scaled.append((number - minimum) / (maximum - minimum))

    return scaled


# PROBLEM 3
def remove_cols_with_missing(df):
    """Return a new dataframe without columns containing missing values."""
    return df.dropna(axis=1)


def remove_rows_with_missing(df):
    """Return a new dataframe without rows containing missing values."""
    return df.dropna(axis=0)


def main():
    pass


if __name__ == '__main__':
    main()