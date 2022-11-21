"""
《Think Python》练习 4-5：用函数画阿基米德螺旋(蚊香线)

r = aθ
由于用乌龟画，从中间开始旋转比较好看，故没有考虑起点与坐标原点的距离
绘图精度（乌龟每次转过的微小角度）：Δθ = π/30 = 6°
绘制的阿基米德螺旋线圈数 (不可能让乌龟无限的画下去)：n

theta：阿基米德螺旋角度 θ，从0开始
m：短线条数，根据精度 Δθ 与圈数 n 计算
length：短线长度
angle：短线间的夹角，即精度 Δθ = π/30 = 6°
"""

# 引入数学模块、乌龟模块
# import math
# import turtle
#
# # 调用乌龟画图、提高画弧速度
# bob = turtle.Turtle()
# bob.delya = 0.01
#
#
# # 阿基米德螺旋
# def spiral(t, a, n):
#     theta = 0
#     m = int(n * 60)
#     for i in range(m):
#         length = math.sqrt((math.cos(math.pi / 30) * a * (theta + math.pi / 30) - a * theta) ** 2 + (
#                     math.sin(math.pi / 30) * a * (theta + math.pi / 30)) ** 2)
#         angle = 6
#         t.fd(length)
#         t.lt(angle)
#         theta = theta + math.pi / 30
#
#
# spiral(bob, 10, 3.25)
# turtle.mainloop()

import numpy as np
import matplotlib.pyplot as plt
import math
# d = 0.0001
# k = 0.2
# x = 0
# y = 0
#
# i = np.arange(0, 150, 1)
# x += d*i*np.cos(k*i)
# y += d*i*np.sin(k*i)
# plt.plot(x,y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title('Akimide')
# #使用show展示图像
# plt.show()
a = []
b = []
delta_d = 0
delta_fai = 0
x, y = 0, 0
for i in range(0, 5000):
    # delta_d += 0.0001
    # delta_fai += 0.4

    # delta_d += np.random.uniform(0.00001, 0.0001)
    # delta_fai += np.random.uniform(0.4, 0.5)

    # delta_d += 0.00005
    # delta_fai += 0.3
    delta_d += np.random.uniform(0.00001, 0.00005)
    delta_fai += np.random.uniform(0.2, 0.3)

    x += delta_d * np.cos(delta_fai)
    y += delta_d * np.sin(delta_fai)
    if math.sqrt(x**2+y**2) > 0.03:
        print('------------------------------',i)
        break
    print(x, '\n', y)
    a.append(x)
    b.append(y)
plt.plot(a, b)
plt.xlabel("x")
plt.ylabel("y")
plt.title('Akimide')
# 使用show展示图像
plt.show()
