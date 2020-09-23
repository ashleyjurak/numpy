import numpy as np

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]]) #row is student and column is test
'''
print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())

print(grades.mean(axis = 0)) #axis = 0 calculates mean by column (test)
print(grades.mean(axis = 1)) #axis = 1 calculates mean by row (student)

numbers = np.array([1,4,9,16,25,36])
print(np.sqrt(numbers))
'''
print(grades[0,1]) #row 1, column 2
print(grades[1]) #entire second row
print(grades[0:2]) #first two rows
print(grades[[1,3]]) #second row and fourth row
print(grades[:,0]) #all rows, but only first column
print(grades[:,1:3]) #all rows, second and third column