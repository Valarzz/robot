from sklearn.preprocessing import normalize
import numpy as np
from robot import robot

# print(np.zeros([20, 20]))
for i in range(20):
    print("[1,", end=" ")
    for j in range(18):
        if i == 0 or i == 19:
            print("1,", end=" ")
        else:
            print("0,", end=" ")
    print("1]")

# rob1 = robot(512, 512, 30)
# rob2 = robot(256, 512, 10)
# i = 0
# while True:
#     rob1.move([1024, 1024])
#     print([round(rob1.x), round(rob1.y)])
#     print([round(rob2.x), round(rob2.y)])
#     i+=1
#     if i >3:
#         break

# r = 3
# pos = [0, 1]
# yaw = np.pi/4
# for x in range(-r, r + 1):
#     for y in range(-r, r + 1):
#         if x ** 2 + y ** 2 < r ** 2:
#             loc = np.array([x, y])
#             lx = pos[0] + x
#             ly = pos[1] + y
#             norm = normalize(loc[:, np.newaxis], axis=0).ravel()
#             d = np.dot(norm, np.array([np.cos(yaw), -np.sin(yaw)]))
#             print(d>0.5, end="")
#             print(str(x)+","+str(y)+"\t", end="")
#             print(norm, end="")
#             print(d)

# a = np.array([1, 1, 1])
# b = np.array([0, 0, 0.5])
# c = np.array([1, 0, 0])
# e = np.zeros([1, 3])
# print((c==e).any())
# print("a-b.all\t", (a-b).all())
# print("c-b.all\t", (c-b).all())
# print((a==b).all())

# img = np.array([[[1, 2, 1, 1], [1, 4, 1, 0]],
#                 [[1, 3, 1, 1], [1, 5, 1, 0]]])
# img1 = np.array([[[1, 1, 1, 0], [1, 1, 1, 0]],
#                 [[1, 1, 1, 0], [1, 1, 1, 0]]])
# m = img[:, :, -1] - img1[:, :, -1]
# print(m)
# print(img[:, :, :-1] * m[:, :, np.newaxis] + img1[:, :, :-1] * (1-m[:, :, np.newaxis]))

# a = 2*np.ones([2, 2, 1])
# # print(img.shape)
# # print(a.shape)
# # print(a)
# img = np.concatenate((img, a), axis=2)
# print(img.shape)
# print(img)
# img = img[:, :, :-1]
# print(img.shape)
# print(img)

# def f(x):
#     return -4 * x**3 - 6 * x**2 - 16 * x -5
#
# print(f(-2), f(1))








