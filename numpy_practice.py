import numpy as np
my_array = np.array([1, 2, 3, 4])
#this prints a 1D array
print(my_array)

my_table = np.array([[1, 2], [3, 4]])
#this is a 2D array
print(my_table)
print(my_table[1][1])

nums = np.array([1, 20, 30])
print(nums + 5)

nums = np.array([[1, 2, 3], [4, 5, 6]])
print(nums.size) # 6 total elements
print(nums.shape) # (2, 3)

#Array Indexing
fruits = np.array(["apple", "banana", "cherry"])
print(fruits[0]) # picks the first fruit in the array
print(fruits[-1]) # picks the last fruit

#Array Slicing- getting parts
numbers = np.array([10, 20, 30, 40, 50])
print(numbers[1:4]) # from index 1 to 3

# Reshaping Arrays
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2,3) # rearranges the array in 2 rows and 3 columns
print(b)

#Creating quick arrays
print(np.zeros((2, 3))) # all zeros
print(np.ones((2, 2))) # all ones
print(np.arange(5)) # [0 1 2 3 4]
print(np.eye(3))    # identity matrix

print(np.arange(2))
array6 = np.empty(5)
print(array6)

arr2 = np.zeros((2,3))
print("2D Array: ")
print(arr2)

arr3 = np.zeros((2, 3, 4))
print("3D Array: ")
print(arr3)

#creating array with specified *values*
spe_val = np.full((2, 2), 7)
print("Array", spe_val)

mixed = np.array([1, 2.5, "hello"])
print(mixed)

#Randomly generated array
# Random floats between 0 and 1
random_float = np.random.rand(3) # 3 random numbers
print(random_float)

# 2D Array of random floats between 0 an 1
random_float = np.random.rand(2,3) # 2 rows 3 columns random numbers
print(random_float)

# Random Integers in a Range
random_ints = np.random.randint( 1, 10, size = (2,4)) # random whole numbers btw 1 and 10(exclusive), 2 rows, 4 columns)
print(random_ints)

choices = np.random.choice([10, 20, 30, 40], size = 5) #randomly picks from your list
print(choices)

#NumPy data types
arr = np.array([10, 20, 30])
print(arr.dtype)

# float array
arr = np.array([1.5, 2.3, 4.8])
print(arr.dtype)

#string array
arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)

#force a specific data type
arr = np.array([1, 2, 3], dtype = 'float32')
print(arr)
print(arr.dtype)

#Convert One Data Type to Another
arr = np.array([1.3, 2.5, 3.7])
new_arr = arr.astype('int32') # removes the decimal part and converts the numbers to integers

print(new_arr)
print(new_arr.dtype)

arr = np.array([[10, 20, 30], [40, 50, 60]])

print("Dimensions: ", arr.ndim)
print("Shape: ", arr.shape)
print("Size: ", arr.size)
print("Date type: ", arr.dtype)
print("Item size: ", arr.itemsize)
print("Total bytes: ", arr.nbytes)
print("Transpose: \n", arr.T)