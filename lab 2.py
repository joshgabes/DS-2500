# LAB EXERCISE 02

# PROBLEM 01


# PROBLEM 02
fruits = ["apple", "pear", "grapes", "peach"]
letter2fruits = {}
for fruit in fruits:
    first_letter = fruit[0]
    if first_letter not in letter2fruits:
        letter2fruits[first_letter]= []
    letter2fruits[first_letter].append(fruit)

common_letters = []
for letter in fruits[0]:
    shared = True
    for fruit in fruits:
        if letter not in fruit:
            shared = False
        if shared and letter not in common_letters:
            common_letters.append(letter)

# PROBLEM 

#Part one
values = [6, 7, 8, 9, 10]
total_sum = 0
i = 0

while total_sum < 2500 and i < len(values):
    total_sum += values[i]
    i += 1

print(total_sum)

#Part two
value = [1, 2, 3, 4, 5, 6]
limited_sum = 0
i = 0

while i < len(value) and value[i] % 2 != 0:
    limited_sum += value[i]
    i += 1
    
print(limited_sum)

# PROBLEM 04


### SETUP BEGINS -- DO NOT MODIFY
course_description = "Offers intermediate to advanced Python programming for data
science. Covers object oriented design patterns using Python, including
encapsulation, composition, and inheritance. Advanced programming skills cover
software architecture, recursion, profiling, unit testing and debugging, lineage
and data provenance, using advanced integrated development environments, and
software control systems. Uses case studies to survey key concepts in data science
with an emphasis on machine learning (classification, clustering, deep learning);
data visualization; and natural language processing. Additional assigned readings
survey topics in Ethics, Model Bias, and Data Privacy pertinent to todays Big Data
world. Offers students an opportunity to prepare for more advanced courses in data
science and to enable practical contributions to software development and data
science projects in a commercial setting. "
### SETUP ENDS -- DO NOT MODIF
