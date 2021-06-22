import numpy as n
from PIL import Image


# m1 = n.array([[1, 2, 3], [4, 5, 6]])
# print(m1)
#
# m2 = n.zeros((2,4,4))
# print(m2)
#
# m2 = n.ones((2,4,3))
# print(m2)

# m = n.full((2, 2), 10)
# print(m)

# m = n.eye((4))
# print(m)
# for i in range(4):
#     for j in range(4):
#         if m[i][j] == 1.0:
#             m[i][j] = 5.0
# print(m)

# r = int(input("Enter no of rows:"))
# c = int(input("Enter no of columns:"))
# m1 = n.zeros((r, c),dtype=int)
# print(m1)
# for i in range(r):
#     for j in range(c):
#         temp = int(input("enter matrix elements:"))
#         m1[i][j] = temp
# print(m1)
# print("Matrix 2")
# m2 = n.zeros((r, c))
# print(m2)
# for i in range(r):
#     for j in range(c):
#         temp = int(input("enter matrix elements:"))
#         m2[i][j] = temp
# print(m2)
#
# op = input("Enter operation(add|sub):")
# if op=="add":
#     result = m1+m2
# if op=="sub":
#     result = m1-m2
# print(result)


# operations
# m1 = n.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(m1)
# m1.sort()
# print(m1)
# m2 = m1.reshape(-1, 1)
# print(m2)
# m3 = m1.reshape(1, -1)
# print(m3)
# m4 = n.append(m1, 5)
# print(m4)
# m5 = n.insert(m1, 0, 0)
# print(m5)
# m6=n.delete(m1,0,axis=0)
# print(m6)
# m6=n.delete(m1,0,axis=1)
# print(m6)
# m7=n.array(n.split(m1,3))
# print(m7)
# m8 = n.random.rand(5, 5)
# print(m8)
# m=m8.max()
# print(m)
# temp = m8[[2], 0:3]
# print(temp)
# print(m8[[4],:])

data = Image.open("img.jpeg")
data1 = data.show(data)
b = n.array(data.resize((100, 200)))
Image.fromarray(b).save('img2.jpeg')
