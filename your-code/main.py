#1. Import the NUMPY package under the name np.
from contextlib import nullcontext
from tkinter import N
import numpy as np


#2. Print the NUMPY version and the configuration.
print("\n-------------------------------- 2 --------------------------------")
print("Version: ", np.version.version)
print("Config: ")
print(np.show_config())


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a1 = np.random.random((2, 3, 5))
a2 = np.random.random(size = (2, 3, 5))
a3 = np.random.randint(0, 10, size = (2,3,5))


#4. Print a.
print("\n-------------------------------- 4 --------------------------------")
print("A1: ")
print(a1)
print("A2: ")
print(a2)
print("A3: ")
print(a3)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))

#6. Print b.
print("\n-------------------------------- 6 --------------------------------")
print("B: ")
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
print("\n-------------------------------- 7 --------------------------------")
print("Does A and B have the same size? ", a1.size == b.size)


#8. Are you able to add a and b? Why or why not?
try:
        new = np.add(a1, b)
        print("\n-------------------------------- 8 --------------------------------")
        print(new)
except ValueError as ve:
        print("\n-------------------------------- 8 --------------------------------")
        print("ValueError:", ve)
        print("The shapes of the 3D arrays are not the same, and because of that we cannot add them together as they are.")


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = np.ndarray.transpose(b, (1,2,0))
print("\n-------------------------------- 9 --------------------------------")
print(c)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
try:
        d = np.add(a1, c)
        print("\n-------------------------------- 10 --------------------------------")
        print("D: ")
        print(d)
except ValueError as ve:
        print("\n-------------------------------- 10 --------------------------------")
        print("ValueError:", ve)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("\n-------------------------------- 11 --------------------------------")
print("A: ")
print(a1)
print("D: ")
print(d)
print("\nThe values of D are the values on A plus 1.")


#12. Multiply a and c. Assign the result to e.
e = np.multiply(a1, c)


#13. Does e equal to a? Why or why not?
print("\n-------------------------------- 13 --------------------------------")
print("Does E equal A? ", np.array_equal(e, a1))
print("They are equal because C is B transposed, and B is a matrix of all 1s. As such, when multiplying A with C to obtain E, we are multiplying the values on A by 1.")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2,3,5))
f2 = np.empty((2,3,5))


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
k = ([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])


def assign_with_thresholds_using_where(array):
        new_array = np.empty((2,3,5))
        d_max = np.max(array)
        d_min = np.min(array)
        d_mean = np.mean(array)

        new_array = np.where((array>d_min) & (array<d_mean),25, array)
        new_array = np.where((array>d_mean) & (array<d_max), 75, new_array)
        new_array = np.where(array==d_mean, 50, new_array)
        new_array = np.where(array==d_min, 0, new_array)
        new_array = np.where(array==d_max, 100, new_array)
        
        return new_array
f2 = assign_with_thresholds_using_where(d)


def assign_with_thresholds(array):
        new_array = np.empty((2,3,5))
        d_max = np.max(array)
        d_min = np.min(array)
        d_mean = np.mean(array)

        for index_bloc in range(len(array)):
                bloc = range(len(array[index_bloc]))
                for index_line in bloc:
                        line = range(len(array[index_bloc][index_line]))
                        for index_number in line:
                                number = array[index_bloc][index_line][index_number]
                                if (number>d_min and number<d_mean):
                                        # value of 25
                                        new_array[index_bloc][index_line][index_number] = 25
                                elif (number>d_mean and number<d_max):
                                        # value of 75
                                        new_array[index_bloc][index_line][index_number] = 75
                                elif (number==d_mean):
                                        # value of 50
                                        new_array[index_bloc][index_line][index_number] = 50
                                elif (number==d_min):
                                        # value of 0
                                        new_array[index_bloc][index_line][index_number] = 0
                                elif (number==d_max):
                                        # value of 100
                                        new_array[index_bloc][index_line][index_number] = 100
        return new_array
f = assign_with_thresholds(d)


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print("\n-------------------------------- 17 --------------------------------")
print("D: ")
print(d)
print("F: ")
print(f)
print("F generated using np.wheres: ")
print(f2)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
def assign_with_thresholds_chars(array):
        new_array = np.chararray((2,3,5))
        d_max = np.max(array)
        d_min = np.min(array)
        d_mean = np.mean(array)
        for index_bloc in range(len(array)):
                bloc = range(len(array[index_bloc]))
                for index_line in bloc:
                        line = range(len(array[index_bloc][index_line]))
                        for index_number in line:
                                number = array[index_bloc][index_line][index_number]
                                if (number>d_min and number<d_mean):
                                        # value of 25
                                        new_array[index_bloc][index_line][index_number] = 'B'
                                elif (number>d_mean and number<d_max):
                                        # value of 75
                                        new_array[index_bloc][index_line][index_number] = 'D'
                                elif (number==d_mean):
                                        # value of 50
                                        new_array[index_bloc][index_line][index_number] = 'C'
                                elif (number==d_min):
                                        # value of 0
                                        new_array[index_bloc][index_line][index_number] = 'A'
                                elif (number==d_max):
                                        # value of 100
                                        new_array[index_bloc][index_line][index_number] = 'E'
        return new_array
char_array = assign_with_thresholds_chars(k)
print("\n-------------------------------- 18 --------------------------------")
print("Char Array: ")
print(char_array)
