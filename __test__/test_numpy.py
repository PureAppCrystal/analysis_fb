import numpy as np
import matplotlib.pyplot as plt


arr = np.arange(10)
print(type(arr))
print(arr)

# arr = np.random.rand(10000)
arr = np.random.normal(5, 3, 10000)
print(arr)

# 평균
print(arr.mean())
print(arr.sum())

# 표준편차
print(arr.std())

# 분산
print(arr.var())

# 최대값
print(arr.max())

# 최대값 위치
print(arr.argmax())

# 최소값
print(arr.min())

#최소값 위치
print(arr.argmin())

fig, subplots = plt.subplots(2, 1)

subplots[0].plot(arr)
subplots[1].hist(arr, bins=20, edgecolor='black', linewidth=1.2)

plt.show()

# plt.plot(arr)
# plt.show()