import numpy as np
'''
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]]) #row is student and column is test

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

print(grades[0,1]) #row 1, column 2
print(grades[1]) #entire second row
print(grades[0:2]) #first two rows
print(grades[[1,3]]) #second row and fourth row
print(grades[:,0]) #all rows, but only first column
print(grades[:,1:3]) #all rows, second and third column
'''
'''
#SHALLOW COPIES
numbers = np.arange(1,6)
number2 = numbers.view() 
print(number2)

numbers[1] *= 10 #change on original will show up on shallow copy, deep copy would not
print(number2)

number2[1] /= 10 #change on shallow copy will show up on original, deep copy would not
print(number2)

number2 = numbers[0:3] #slice
print(number2)

numbers[1] *= 20 #change on original shows on slice
print(number2)

#DEEP COPIES
number2 = numbers.copy() #arrays do not affect one another

grades = np.array([[87,96,70],[100,87,90]])
print(grades.reshape(1,6)) #usually save into other variable and use for calculation, doesn't change OG array. creates shallow copy / view
print(grades)

grades.resize(1,6)
print(grades)
flattened = grades.flatten() #all on one row
print(flattened)
print(grades)
raveled = grades.ravel()
print(raveled)
raveled[5] = 99
print(grades)
'''
grades = np.array([[87,96,70],[100,87,90]])
grad = grades.T #transpose from rows to columns or vv
print(grad)

grades2 = ([[94,77,90],[100,81,82]])
h_grades = np.hstack((grades,grades2)) #keeps 2 students, but gives each student 3 additional grades
print(h_grades)
v_grades = np.vstack((grades,grades2)) #keeps 3 tests, but adds 2 additional students
print(v_grades)