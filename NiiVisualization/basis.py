import numpy as np
# ===========================
## isin
# def isin(element, test_elements, assume_unique=False, invert=False):
#   element = np.asarray(element)
#   return in1d(element, test_elements, assume_unique=assume_unique, invert=invert).reshape(element.shape)


# element = 2*np.arange(4).reshape((2, 2))
# print(element)

# test_elements = [1, 2, 4, 8]

# mask = np.isin(element, test_elements)
# print(mask)

# # print(elements[0][1])
# print(element[mask])

# mask = np.isin(element, test_elements, invert=True)
# print(mask)
# print(element[mask])

# ===================================

##seed():np.random.RandomState
# rng = np.random.RandomState(1) #the starting point for a sequence of pseudorandom number
# arrayA = rng.uniform(0, 1, (2,3))
# print(arrayA)
#
# rgen = np.random.RandomState(1)
# w = rgen.normal(0.0, 0.01, (4,2))
# print(w)
#
# print(np.random.RandomState(0).rand(3))
# print(np.random.RandomState(0).rand(2))
# print(np.random.RandomState(None).rand(2))
# print(np.random.RandomState(None).rand(3))

#==========================================


##zip
arrayB = np.zeros((3,4))
b = [1, 2, 3, 4]
a = zip(arrayB,b)
x, y, z = a
print(x, y, z)

test1 = np.random.random((3,4))
test2 = np.random.rand(3,4)
pak1 = zip(test1, test2)
result1, result2, result3 = pak1
print(result1, result2, result3)
