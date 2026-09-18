import numpy as np


#AGGREGATE FUNCTION =SUMMARIZE DATA AND TYPICALLY
#                     RETURNS A SINGLE VALUE

array=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
# print(np.mean(array))
# print(np.sum(array))
# print(np.std(array))  #STANDARD DEVIATION ,SPREAD WITHIN DATA
# print(np.var(array))  #variance -sqaure of std
# print(np.min(array))
# print(np.argmin(array)) #position of min value
# print(np.argmax(array)) #position of max value
# print(np.argmin(array))

print(np.sum(array, axis=1)) #axis 0 sum of column, 1 is sum of rows.
 



