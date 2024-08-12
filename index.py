import numpy as np
from timeit import timeit
# arr = np.array([1,2,3,4,5])
# print(arr)

# list_numbers = [1,2,3,4,5]
# print(list_numbers)
# print(type(arr))
# print(type(list_numbers))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return f"(Name: {self.name}, Age: {self.age})"
    

# p1 = Person('ahmed', 45)
# p2 = Person('mohamed', 40)

# people = np.array([p1, p2, 8], dtype=Person)

# print(people[0])
# print(timeit(lambda: [i**4 for i in range(1,9)], number=1000))
# x = timeit(lambda: np.arange(1, 8)**4, number=1000)
# print(x)\


# x = [1,2,3,4]
# y = np.array([1,2,3,4])

# print(y)
# print(type(y))

# l = []

# for i in range(5):
#     number = int(input("enter_: "))
#     l.append(number)

# print(np.array(l))

# ar2 = np.array([['ahmed', 'ali', 'mohamed'], ['aymen', 'imad', 'adil']])
# print(ar2.ndim)
# for i in ar2:
#     print(i)

# ar3 = np.array([[[1,2], [2,3]]])

# print(ar3.ndim)
# print(ar3)

# arn = np.array([1,2,3,4], ndmin=3)
# print(arn)

# a_zero = np.zeros(4)
# print(a_zero)

#[ [0,0], [0,0] ]

# a_zeros = np.zeros((2, 4))
# print(a_zeros)

# a_ones = np.ones((3,5))
# print(a_ones)

#empty
# ar = np.empty(4)
# ar[0] = 1
# ar[1] = 1
# ar[2] = 1
# ar[3] = 1
# print(ar)

# range_arr = np.arange(1,10)
# print(range_arr)

# arr_diagonal = np.eye(3,5)
# print(arr_diagonal)
# lin = np.linspace(0, 10, num=7)
# print(lin)

# print(np.random.randint(0, 10))
# print(np.random.rand())
# print(np.random.random_integers(10, 20))
# print(np.random.choice(np.array(['ahmed', 'mohamed'])))
# print(np.random.ranf(10))
# print(np.random.rand(4))
# print(np.random.randn(5,2))                       

# l = np.array([1,2,3,4,5,0], dtype=np.bool_)
# print(l)
# print(l.dtype)

# name = np.str_('ahmed')


# print(type(name))

# l = np.array([1,2,3,4])
# l2 = l.astype(np.bool_)
# l3 = np.bool_(l)

# print(l2.dtype)
# print(l2)

# print(np.add(1,2))
# print(np.subtract(10,2))
# print(np.multiply(1,2))
# print(np.divide(1,2))
# print(np.mod(10,3))
# print(np.power(10,3))

#  

# l = np.array([25, 36, 12, 80, 7, 9])
# print(np.min(l), 'index', np.argmin(l))
# print(np.max(l), 'index', np.argmax(l))

# print(np.sqrt(l))

# l2 = np.arange(0, 10)
# print(timeit(lambda: np.add(l2, 3)))

# arr = np.array([
#     [1,2,3,4, 9],
#     [30,50,99,100,4],
#     [10, 5, 60, 88, 200]
# ])

# print(np.max(arr, axis=0))
#30 50 99 100 200

# l = [1,3,6,8]
# print(np.cumsum(l))
# np.average(l)
# 1 4 10 18

# l = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(l.shape)

# l = np.array(
#     [
#         [
#             [
#                 [1,2,3,4]
#             ]
#         ]
#     ]
# )

# print(l.shape) # rows: 3 1,2 ,3 cols: 4

# l = np.array([1,2,3,4,5,6])
# l2 = np.reshape(l, (3,2))
# print(l2)
# print(l2.shape)
# print(l2.ndim)

# l = np.array([[1,2], [3,4], [5,6]])

# print(np.reshape(l, (3,2)))

# l = np.array([1,2,3, 5])
# l2 = np.array([4,5,6, 5])

# l3 = np.add(l ,l2)
# print(l3) 
# print("cols:", l3.shape)
# print(l3.ndim)

# l = np.array([[1,2,3], [4,5,6]])

# print(l[0, -1])

# l = np.array([1,2,3,4])

# print(l[0:3:2])

# l = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# print(l[0:2])

# l = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# for index, items in enumerate(l):
#     print(f"Array {index+1} Elements:", items)

#     print("-------------------------------------")

# l = [
#     [
#         [1,2,3],
#         [4,5,6]
#     ]
# ]

# for index, number in np.ndenumerate(l):
#     print('index', index, 'number', number)

# print(l[0][1][2])
#copy vs view
# arr1 = np.array([1,2,3,4])
# arr2 = arr1.view()

# arr1[0] = 30

# print(arr1)
# print(arr2)

# arr = np.array([1,2,3,4])
# arr2 = np.array([5,6,7])

# arr3 = np.concatenate((arr, arr2))
# print(arr3)
# print(arr3.shape)
# print(arr3.ndim)

# var = np.array([[1,2], [3,4]])
# var2 = np.array([[7,8], [9,10]])

# var3 = np.concatenate((var, var2), axis=1)

# print(var3)

# var = np.array([1,2, 3,4])
# var2 = np.array([7,8, 9,10])

# var3 = np.stack((var, var2), axis=1)

# print(var3)
# print(var3.ndim)

# var = np.array([[1,2], [3,4], [5,6]])
# ar = np.array_split(var, 2, axis=1)

# print(ar)
# print(type(ar))

# names = np.array(['ahmed', "ali", "mohamed"], dtype=np.str_)
# ages = np.array([23, 24, 30], dtype=np.int16)
# cities = np.array(['agadir', "tanger", "taroudant"], dtype=np.str_)

# data = np.stack((names, ages, cities), axis=1)
# print(type(data))
# for name, age, city in data:
#     print(f'Name: {name}, Age: {age}, City: {city}')


# var = np.array([
#     [1,30],
#     [440,75],
#     [700, 89]
# ])
# chars = np.array(['z', 'b', 'c'])

# # f = np.where((var % 2) != 0)
# # f = np.where((var >= 1) & (var <= 3), var, None)

# # f = np.searchsorted(var, [2,6,10], side="left")
# # f = np.sort(var, axis=1)

# # print(f)
# filters = [True, False, True]
# f = chars[filters]

# print(f)

# var = np.array([[1,2], [3,4],[2,2],[4,3]])

# # np.random.shuffle(var)
# # print(var)

# # f = np.unique(var, return_index=True)
# # print(f)

# # var = np.resize(var, (3, 4))
# # d = var.flatten(order='K')
# d = var.ravel(order='F')
# print(d)

# var = np.array([[1,2],[3,4]])
# # var2 = np.insert(var, 2, [5,6], axis=0)
# # var2 = np.append(var, [12,23])

# var2 = np.delete(var, 0, axis=0)

# print(var2)

# m = np.matrix([
#     [1,2,3],
#     [1,2,3]
# ])
# #[2, 4, 6]
# print(m)
# print(type(m))
# print(m.ndim)
# print(m.shape)

# print(np.sum(m, axis=1))

# m = np.matrix([ 
#     [1,2],
#     [4,5]
# ])

# m2 = np.matrix([
#     [7,8],
#     [9,10]
# ])

# r = m * m2
# r2 = m.dot(m2)
# print(r)

# print(r2)

# var = np.matrix([[1,2, 3], [4, 5,6]])

# print(var)

# print(np.transpose(var))
#three dimensional array (masfofa tolatiyat al ab3ad)
# nums = np.array([
#     [
#         [1,2,3,4],
#         [1,2,3,4],
#         [1,2,3,4],
#     ],
#     [        
#         [1,2,3,4],
#         [1,2,3,4],
#         [1,2,3,4],
#     ]
# ])
# print(nums)
# print(type(nums))
# print(nums.shape)
# print(nums.ndim)
# print(nums.size)
# print(nums.dtype)

# arr = np.array([
#     [
#         [10,15,25,35],
#         [48,23,90,300]
#     ],
#     [
#         [10,15,25,35],
#         [48,23,90,300]
#     ],
# ])

# print(arr[1, 1, 3] / 2)
# data = {
#     "name":"ahmed", 
#     "age": 34
# }
# numbers = np.array([10,30,340, data])
# print(numbers[3]['name'])
# print(numbers.dtype)
# print(type(numbers))

# a = np.full((3, 2, 3), 10)
# z = np.zeros((2, 3, 10))

# print(z)

# arr1 = np.array([1,2,3,4,5,6])
# arr2 = np.array([[1], [2]])
# print(np.add(arr1, arr2))


# a1 = np.array([10, 33, 40, 22])
# a2 = np.array([10, 33, 40, 22])

# print(np.array_equal(a1, a2))

# a = np.array([[1,2,3,4], [11,22,33,44]])

# # a2 = np.append(a, (5,6,7,8))
# # a2 = np.insert(a, 1, (5,6,7,8))
# a2 = np.delete(a, 0, axis=1)

# print(a2)

# a = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
# ])

# # print(a.reshape((5, 4)))
# print(a.transpose())
# print(a.T)

# a1 = np.array([
#     [1,2,3],
#     [5,6,7],
#     [52,62,72],
#     [8,9,100]
# ])

# a2 = np.array([
#     [52,62,72],
#     [8,9,100]
# ])

# # a = np.concatenate((a1,a2), axis=1)
# # print(a)
# max_n = np.median(a1)
# print(max_n)

# rnd = np.random.randint(10, 100, size=(4, 5))
# a1 = np.array(rnd)
# np.save(file='numbers.npy', arr=a1)

# a = np.load('numbers.npy')
# print(a)

# np_version = np.__version__
# print(np_version)
# np.show_config()

# v = np.zeros((2, 3, 10))
# print(v)

# print(np.info(np.where))

# print(np.arange(10))

# a = [100, 27, 90, 1000,3, 1]

# arr_s = np.sort(a)[::-1]
# print(type(arr_s))
# print(arr_s)

# v = np.arange(9).reshape((3, 3))
# print(v)

# arr = np.array([1,2,3,3,4,5,6,7,90,100,100,788,656])

# # grather = np.extract(arr > 100, arr)
# grather = np.extract(arr <= 100, arr)

# print(type(grather))

# arr = [1,0,0,0,0,8,9]

# print(np.nonzero(arr))

# v = np.eye(10)
# print(v)

#exercices
# arr = np.random.randint(10, 50, size=(5, 4))
# mean = arr.mean(axis=0)
# median = np.median(arr, axis=0)
# std = np.std(arr, axis=0)
# print(f"Mean: {mean}")
# print(f"Median: {median}")
# print(f"standard deviation: {std}")

