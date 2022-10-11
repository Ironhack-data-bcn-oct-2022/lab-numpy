#1. Import the NUMPY package under the name np.
import numpy as np
#2. Print the NUMPY version and the configuration.


print(np.__version__)



#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(10, size = (2, 3, 5))





#4. Print a.
print(a)



#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))
print(b)



#6. Print b.
print(b)



#7. Do a and b have the same size? How do you prove that in Python code?

if b.size == a.size:
        print("yes")



#8. Are you able to add a and b? Why or why not?
 
 #np.add(a,b) you cant because they have different shapes

# In Python syntax, a+b is translated to a.__add__(b). a.__add__ is a method that implements addition for objects of type a. A number has such a method, a list does as well ([1,3]+[4]) and so does a string ('abc'+'d').



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = b.transpose(1,2,0)
print(c)



#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)
print(d)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)




#12. Multiply a and c. Assign the result to e.
e=a*c
print(e)

# Other formula
e=np.multiply(a,c)
print(e)


#13. Does e equal to a? Why or why not?

print("a",a)
print("e",e)

if a.shape == e.shape:
        print("yes")

# because they same numbers shapes and size


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_min=np.amin(d)
d_max=np.amax(d)
d_mean=np.mean(d)
print(d_min)
print(d_max)
print(d_mean)



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f=np.empty([2,3,5])
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

aux1 = len(f)
aux2 = len(f[0])
aux3 =len(f[0][0])
print(aux1,aux2,aux3)

for i in range(aux1):
        for j in range(aux2):
                for k in range(aux3):
                        if d_mean < d[i][j][k] < d_max:
                                f[i][j][k]=75
                        elif d_min < d[i][j][k] < d_mean:
                                f[i][j][k]=25
                        elif d[i][j][k] == d_mean:
                                f[i][j][k]=50
                        elif d[i][j][k] == d_min:
                                f[i][j][k]=0
                        elif d[i][j][k] == d_max:
                                f[i][j][k]=100


print(f)

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
for block in range(d.shape[0]):
        for line in range(d.shape[1]):
                for item in range(d.shape[2]):
                        if d[block][line][item] > d_min and d[block][line][item] < d_mean:
                                g[block][line][item] = "B"
                        elif d[block][line][item] > d_mean and d[block][line][item] < d_max:
                                g[block][line][item] = "D"
                        elif d[block][line][item] == d_mean:
                                g[block][line][item] = "C"
                        elif d[block][line][item] == d_min:
                                g[block][line][item] = "A"
                        elif d[block][line][item] == d_max:
                                g[block][line][item] = "E"
print(g)