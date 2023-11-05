import numpy as np

# data:
w1 = np.array([[0,0,0],[1,0,0],[1,0,1],[1,1,0]])
w2 = np.array([[0,0,1],[0,1,0],[0,1,1],[1,1,1]])
w1 = w1.T
w2 = w2.T
d = w1.shape[0] # dim
n = w1.shape[1] # samples number
p1 = 0.5
p2 = 0.5

# E(x):
w1_mean = np.reshape(np.mean(w1,axis=1),(d,1))
w2_mean = np.reshape(np.mean(w2,axis=1),(d,1))
Ex_all = p1*w1_mean+p2*w2_mean

# offset：
w1_off = w1-Ex_all
w2_off = w2-Ex_all

# 自相关矩阵：
R1 = 1/n*(np.dot(w1_off,w1_off.T))
R2 = 1/n*(np.dot(w2_off,w2_off.T))
R = p1*R1+p2*R2

# 特征值：
eigenvalue, featurevector = np.linalg.eig(R)
print("特征值：",end=' ')
print(eigenvalue)
print("特征向量：")
print(featurevector)

# 变换：
d2x = np.dot(featurevector[:,:2].T,w1_off)
d2y = np.dot(featurevector[:,:2].T,w2_off)
print("降至二维：")
print("第一类")
print(d2x)
print("第二类")
print(d2y)
d1x = np.dot(featurevector[:,0].T,w1_off)
d1y = np.dot(featurevector[:,0].T,w2_off)
print("降至一维：")
print("第一类")
print(d1x)
print("第二类")
print(d1y)

# --------
# output: 
# 特征值： [0.25 0.25 0.25]
# 特征向量： 
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
# 降至二维：
# 第一类
# [[-0.5  0.5  0.5  0.5]
#  [-0.5 -0.5 -0.5  0.5]]
# 第二类
# [[-0.5 -0.5 -0.5  0.5]
#  [-0.5  0.5  0.5  0.5]]
# 降至一维：
# 第一类
# [-0.5  0.5  0.5  0.5]
# 第二类
# [-0.5 -0.5 -0.5  0.5]

