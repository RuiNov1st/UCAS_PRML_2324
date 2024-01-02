import numpy as np
from hmmlearn import hmm 

# params:
M = 6
state_option = [0,1,2,3,4,5]
N = 6
obs_option = ['begin','A','C','G','T','end']
T = 6
s_begin = 0
s_end = 5
# 状态转移矩阵: M*M
A = np.array([[0,0.5,0.5,0,0,0],[0,0.2,0,0.8,0,0],[0,0,0.8,0,0.2,0],
              [0,0,0,0.4,0,0.6],[0,0,0,0,0.1,0.9],[0,0,0,0,0,1]])
# 发射矩阵：M*N
B = np.array([[1,0,0,0,0,0],[0,0.4,0.1,0.2,0.3,0],[0,0.4,0.1,0.1,0.4,0],
              [0,0.2,0.3,0.3,0.2,0],[0,0.1,0.4,0.4,0.1,0],[0,0,0,0,0,1]])


model = hmm.CategoricalHMM(n_components = M)
model.startprob_ = np.array([1,0,0,0,0,0])
model.transmat_ = A
model.emissionprob_ = B

# 计算观测序列的概率：AGTT
pro1 = model.predict(np.array([[0,1,3,4,4,5]]).T)
print(np.power(np.e, model.score(np.array([[0,1,3,4,4,5]]).T)))

# 计算观测序列TATA的状态：
prob2,state2 = model.decode(np.array([[0,4,1,4,1,5]]).T)
print(state2)
print(np.power(np.e,prob2))
