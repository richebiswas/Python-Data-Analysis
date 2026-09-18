import numpy as np
# scalar arithemtic

radii= np.array([1,2,3])

# print(array+1)
# print(array-1)
# print(array*2)
# print(array/4)
# print(array**2)  #power of / to the power


# #vectorized math function

# print(np.sqrt(array)) #sqaure root of each element
# print(np.round(array))  #round off the numbers
# print(np.floor(array))  # round down the numbers 
# print(np.ceil(array))   #round up the numbers
# print(np.pi)  #  3.141 of pi

#Exercise : mutltiply by pi  A= PI*radius^2

print(np.pi * radii**2)

#ELEMENT - WISE ARITHEMETIC


array1=np.array([1,2,3])
array2=np.array([4,5,6])

print(array1+array2) #output is [5,7,9]
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)
print(array1%array2)


#COMPARISON OPERATORS

scores= np.array([91,56,89,100,45,99,60])


print(scores==100) # returns [false false true false false]
print(scores>=60)  #returns [true false true true false true true]
print(scores<60)  #returns [False  True False False  True False False]

scores[scores<60] = 0
print(scores)   #[ 91   0  89 100   0  99  60] output



