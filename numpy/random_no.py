import numpy as np

# rng=np.random.default_rng(seed=101) #means create a random number generator object and store it in the variable rng
# #seed is like mc seed can be used for same random no

# print(rng.integers(low=1,high=7,size=(2,2)))#second no is exclusive so it become 1 to 6
# #size=(4,2) genrate 4*2 matrix

# print(np.random.uniform())#equal chance of selection
# print(np.random.uniform(low=-1,high=1,size=3))

# #TO SET THE SEED 
# np.random.seed(seed=1)

rng=np.random.default_rng()

# array=np.array([1,2,3,4,5])
# rng.shuffle(array) #will shuffle the array
# print(array)

fruits=np.array(["apple","orange","banana","coconut"])

fruits=rng.choice(fruits) #
print(fruits)

