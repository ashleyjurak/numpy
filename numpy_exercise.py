'''
Create 3 (student) by 4 (test) array of 12 random grades ranging 60 to 100
Calculate average of all grades, grades per test, grades per student
'''
import numpy as np

grades = np.random.randint(60,101,12).reshape(3,4) #101 b/c we want 100 included

print(grades)
print()
print('All grades:',grades.mean())
print()
print('Avg by test:',grades.mean(axis = 0))
print()
print('Avg by student:',grades.mean(axis = 1))