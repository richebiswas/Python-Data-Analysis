import numpy as np

ages=np.array([[21,17,19,20,30,18,65],
              [30,22,15,99,18,20,21]
])

# teenegars=ages[ages<18]
# print(teenegars)

# adults= ages[(ages>=18) & (ages<65)]
# seniors=ages[ages>=65]

# evens=ages[ages%2==0]
# evens=ages[ages%2!=0]
# print(evens)


adults=np.where(ages>=18,ages,0) #here any condition not satisfying will be replaced by 0
print(adults)






