# LAB EXERCISE 06

### SET UP BEGINS Do not modify
section_A = [85, 88, 90, 92, 87, 91, 89, 84, 86, 90]
section_B = [78, 95, 82, 88, 91, 73, 99, 85, 77, 94]
### SET UP ENDS Do not modify

# PROBLEM 01
def find_average(numbers):
    """Return the mean of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

# PROBLEM 02
def find_median(numbers):
    """Return the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 1:
        return sorted_numbers[middle]
    else:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

# PROBLEM 03
def find_mode(numbers):
    """Return all modes in a list, or the original list if no mode exists."""
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    highest_count = 0
    for number in counts:
        if counts[number] > highest_count:
            highest_count = counts[number]
    if highest_count == 1:
        return numbers
        
    modes = []
    for number in counts:
        if counts[number] == highest_count:
            modes.append(number)
    return modes
    
# PROBLEM 04
def find_variance(numbers):
    """Return the population variance of a list of numbers."""
    n = len(numbers)
    mean = sum(numbers) / n
    return sum((x - mean) ** 2 for x in numbers) / n


def find_sd(variance):
    """Return the standard deviation given a variance."""
    return variance ** 0.5

# PROBLEM 05
def print_stats(name, scores):
    """Calculate and print summary statistics for one section's scores."""
    mean = find_average(scores)
    median = find_median(scores)
    modes = find_mode(scores)
    variance = find_variance(scores)
    sd = find_sd(variance)

    print(name)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    if modes == scores:
        print("Mode(s): No mode")
    else:
        print("Mode(s):", modes)
    print("Population variance:", round(variance, 2))
    print("Standard deviation:", round(sd, 2))
    print()


def main():
    print_stats("Section A", section_A)
    print_stats("Section B", section_B)

def main():
    pass
if __name__ == '__main__':
    main()
