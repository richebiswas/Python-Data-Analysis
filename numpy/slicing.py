import numpy as np
array=np.array([[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
)
#array[start:end:step]

#print(array[-2]) #prints the array like 0,1,2,3 postion
#-1,-2 giving ending arrays


#print(array[0:3]) #returns [1,2,3,4],[5,6,7,8],[9,10,11,12] last indexis exclusive

#Q1) GIVE ME 2n2 ROW starting from row 0 and row 2

#print(array[::2])  


#COLUMN SELECTION:
#array[ something , something ]
 #        ↑              ↑
 #      rows          columns

#print(array[:,0])  #returns 1,5,9,13 the first column

# array[  :  ,  0:3  ]
#        ↑       ↑
#       rows   columns

#print(array[:,-1]) #returns last columns 4,8,12,16


#q2 NEED FIRSTT THREE COLUMN

# print(array[:,0:3])  read copy

# print(array[:,::2])  #Take every 2nd column. so it means skip column 0,2


#print(array[:,::-1])   #reverse the column

#print(array[0:2,0:2])  #gives first two column of the first two rows

# print(array[2:,0:2])   

# 2: → start from row index 2 and take all remaining rows
# 0:2 → take columns 0 and 1 (stop before column 2)