# import numpy as np

# array=np.array('A')  0 dimensional array

# print(array.ndim)   #SHOWS NO OF DIMENSIONS

# import numpy as np

# array=np.array(['A','B','C','D'])   1 dimensional array


# print(array.ndim)


# import numpy as np

# array=np.array([['A','B','C','D'],
# ['E','F','G','H'],
# ['X','Y','Z','W']])     2 dimensional array


# print(array.ndim)


# import numpy as np

# array=np.array([[['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']],
#                [['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']],
#                [['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']]]       
# )     
#   #3 dimensional array

# print(array.shape) #returns a tuple of integers
# #shows layers/depth,no of rows and number of columns


# import numpy as np

# array=np.array([[['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']],
#    [['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']],
#    [['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']]]       
# )    

# print(array[0][0][0]) chain-indexing returns A


import numpy as np

array=np.array([[['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']],
   [['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']],
   [['A','B','C','D'],['E','F','G','H'],['X','Y','Z','W']]]       
)    

#print(array[1,0,3]) #multi-dimensional indexing

word=array[0,0,1]+array[0,1,0]+array[2,0,3]  #return BED
print(word)
