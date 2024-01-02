"""
使用前向算法计算序列AGTT出现的概率
状态: 0 1 2 3 4 5
观察: begin A C G T end
观察序列:[begin,A,G,T,T,end]
"""
import numpy as np
import decimal
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
              [0,0,0,0.4,0,0.6],[0,0,0,0,0.1,0.9],[0,0,0,0,0,0]])
# 发射矩阵：M*N
B = np.array([[1,0,0,0,0,0],[0,0.4,0.1,0.2,0.3,0],[0,0.4,0.1,0.1,0.4,0],
              [0,0.2,0.3,0.3,0.2,0],[0,0.1,0.4,0.4,0.1,0],[0,0,0,0,0,1]])
# 观察序列
obs_list = ['begin','A','G','T','T','end']

# 存储前向概率
for_pro = np.zeros((M,T),dtype=np.float)

# 前向算法
def forward():
    # 按时间走
    for t in range(T):
        # 初始值
        if t == 0:
            state_idx= state_option.index(s_begin)
            for_pro[state_idx,t] = 1
        else:
            # 目前观测值
            obs_idx = obs_option.index(obs_list[t])
            # t+1层的循环
            for s1 in range(M):
                # t+2层的循环
                for s2 in range(M):
                    for_pro[s1,t] = decimal.Decimal(str(for_pro[s1,t]))+decimal.Decimal(str(for_pro[s2,t-1]))*decimal.Decimal(str(A[s2,s1]))
                for_pro[s1,t] = decimal.Decimal(str(for_pro[s1,t])) *decimal.Decimal(str(B[s1,obs_idx]))  
    # 最后输出序列概率
    pro = np.sum(for_pro[:,T-1],axis=0)
    return pro,for_pro

if __name__ == '__main__':
    pro,for_pro = forward()
    print(for_pro)
    print(pro)
    



