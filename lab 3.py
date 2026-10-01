# LAB EXERCISE 03
# SET UP BEGINS - Do Not Modify
employees = [
{"name": "Alice", "department": "Engineering", "years_experience": 5},
{"name": "Ann", "department": "Marketing", "years_experience": 4},
{"name": "Ben", "department": "Engineering", "years_experience": 2},
{"name": "Bob", "department": "Engineering", "years_experience": 6},
{"name": "Eve", "department": "HR", "years_experience": 3},
]
pairs = [(5, 2), (1, 4), (3, 1), (2, 9)]
# SET UP ENDS - Do Not Modify
# PROBLEM 01
def count_ints(lst, num):
    """"
    takes a list of integers and an number num 
    and returns the number of times the number appears in list. 
    """
    
    count = 0

    for row in lst:
        for value in row:
            if value == num:
                count += 1
    return count

# PROBLEM 02
def remove_duplicates(lst):
    """
    returns a new list with duplicate values removed
    """
    new_list = []

    for value in lst:
        if value not in new_list:
            new_list.append(value)

    return new_list

# PROBLEM 03
def filter_employees(employee_list):
    """Returns the names of Engineering employees with more than 3 years of experience."""
    return [employee["name"]
            for employee in employee_list
            if employee["department"] == "Engineering"
            and employee["years_experience"] > 3]

# PROBLEM 04
def function_p4(pairs):
    """Take a list of tuples of two numbers and return a list of tuplescontaining the original two numbers and their product."""
    return [(a, b, a * b) for a, b in pairs]
print(function_p4(pairs))

# PROBLEM 05
def function_p5(tuples):
    """Return the tuples sorted ascending by their second element."""
    return sorted(tuples, key=lambda t: t[1])


# PROBLEM 06
def function_p6(tuples):
    """Return the tuples sorted descending by their sum."""
    return sorted(tuples, key=lambda t: sum(t), reverse=True)

def main():
pass
if __name__ == "__main__":
main()
