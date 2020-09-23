import numpy as np
'''
integers = np.array([1,2,3]) #creates array

print(integers)
print(type(integers))
'''
integers = np.array([[1,2,3],[4,5,6]]) #creates 2d array, 2 rows, 3 columns
'''
print(integers.dtype) #type of elements in array
print(integers.ndim) #number of dimensions
print(integers.shape) #how many rows, columns
print(integers.size) #number of elements in array

for row in integers:
    print(row)
    print()

    for col in row:
        print(col, end = ' ') #space instead of new line
    print()

for i in integers.flat:
    print(i, end = ' ')

print(np.zeros(5)) #create an array of 5 zeros, float by default

print(np.ones(5)) #create an array of 5 ones

array1 = np.ones((2,4), dtype = int) #create array of ones with type int
print(array1)

array2 = np.full((3,5), 13) #create array with number 13
print(array2)

print(np.arange(5)) #index 0 to 4
print(np.arange(5,10)) #index 5 to 9
print(np.arange(10,1,-2)) #third argument is step value

print(np.linspace(0.0,1.0,num = 5)) #only works for float, creates 5 equally spaced numbers that includes lower and upper limits

array1 = np.arange(1,21)
print(array1)

array2 = array1.reshape(4,5) #new dimensions have to exactly equal product
print(array2)

array3 = np.arange(1,100001).reshape(4,25000) #will only show beginning and end of rows, but it all exists in memory
print(array3)

array4 = np.arange(1,100001).reshape(100,1000)
print(array4)
'''
numbers = np.arange(1,6)
print(numbers * 2)
print(numbers * [2,2,2,2,2])
print(numbers ** 3)
print(numbers) #original array is not affected
numbers += 10
print(numbers) #original array IS changed by augmented assignment

print(numbers >= 13) #returns true or false

numbers2 = np.arange(11,16)
print(numbers2 > numbers) #returns true or false, equal is false

print(numbers == numbers2)