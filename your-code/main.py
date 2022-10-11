#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print("numpy version is:", np.__version__)
print("configuration:", np.show_config())



#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random((2,3,5))
#a_1 = np.random.randint(10,size=(2,3,5))



#4. Print a.
print(a)
#print(a_1)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b=np.full((5,2,3), 1)
#b=np.random.randint(1,2, size=(5,2,3))


#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
print(a.size)
print(b.size)
print(a.size == b.size) #True, same size


#8. Are you able to add a and b? Why or why not?
try:
        a_b = a + b #this is adding them
        #a_b=np.concatenate([a,b]) #this is not adding them
        print(a_b)

except ValueError:
        print("ValueError: Not able to add 'a' and 'b'. Operands have different shapes")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
#a=2,3,5
#b=5,2,3
c = np.transpose(b, (1,2,0))
print(c)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
print(d)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("")
print("")
print(a)
print("")
print(d)

#The "1" from the unitary matrix was added to each element of the random array

#12. Multiply a and c. Assign the result to e.
e = a * c
print("")
print("")

print(e)


#13. Does e equal to a? Why or why not?
print(e == a)
# Yes since c is an array where all elements = 1, we're multiplying each element in 'a' by 1.


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print("MAX: ",d_max," MIN: ", d_min," MEAN: ", d_mean)



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2,3,5))
print(f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""



# DOESNT WORK FOR NOW
# for element in range(len(d)):
#         for element_2 in range(len(element)):
#                 for value in range(len(element_2)):

#                         if value > d_min and value < d_mean:
#                                 for i in range(len(f)):
#                                         for x in range(len(i)):
#                                                 for n in range(len(x)):
#                                                         n = 25
#                         elif value > d_mean and value < d_max:
#                                 for i in range(len(f)):
#                                         for x in range(len(i)):
#                                                 for n in range(len(x)):
#                                                         n = 75
#                         elif value == d_mean:
#                                 for i in range(len(f)):
#                                         for x in range(len(i)):
#                                                 for n in range(len(x)):
#                                                         n = 50
#                         elif value == d_min:
#                                 for i in range(len(f)):
#                                         for x in range(len(i)):
#                                                 for n in range(len(x)):
#                                                         n = 0
#                         elif value == d_max:
#                                 for i in range(len(f)):
#                                         for x in range(len(i)):
#                                                 for n in range(len(x)):
#                                                         n = 100

# print(f)
# print(f[0][0])

print(d)
print("")
print(d[0][0])


for d_1 in range(len(d)):
        for d_2 in range(len(d[0])):
                for d_3 in range(len(d[0][0])):

                        if d[d_1][d_2][d_3] > d_min and d[d_1][d_2][d_3] < d_mean:
                                f[d_1][d_2][d_3] = 25

                        elif d[d_1][d_2][d_3] > d_mean and d[d_1][d_2][d_3] < d_max:
                                f[d_1][d_2][d_3] = 75

                        elif d[d_1][d_2][d_3] == d_mean:
                                f[d_1][d_2][d_3] = 50

                        elif d[d_1][d_2][d_3] == d_min:
                                f[d_1][d_2][d_3] = 0

                        elif d[d_1][d_2][d_3] == d_max:
                                f[d_1][d_2][d_3] = 100

print("")

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
print(d)
print("")
print(f)


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

g = np.empty((2,3,5),dtype="object")

for d_1 in range(len(d)):
        for d_2 in range(len(d[0])):
                for d_3 in range(len(d[0][0])):

                        if d[d_1][d_2][d_3] > d_min and d[d_1][d_2][d_3] < d_mean:
                                g[d_1][d_2][d_3] = "A"

                        elif d[d_1][d_2][d_3] > d_mean and d[d_1][d_2][d_3] < d_max:
                                g[d_1][d_2][d_3] = "B"

                        elif d[d_1][d_2][d_3] == d_mean:
                                g[d_1][d_2][d_3] = "C"

                        elif d[d_1][d_2][d_3] == d_min:
                                g[d_1][d_2][d_3] = "D"

                        elif d[d_1][d_2][d_3] == d_max:
                                g[d_1][d_2][d_3] = "E"
print(g)