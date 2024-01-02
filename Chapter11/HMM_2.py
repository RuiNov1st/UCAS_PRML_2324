"""
计算观测到TATA最可能的状态序列
状态: 0 1 2 3 4 5
观察: begin A C G T end
观察序列:[begin,T,A,T,A,end]
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
obs_list = ['begin','T','A','T','A','end']

# 存储概率值
pro_arr = np.zeros((M,T),dtype=np.float)
# 存储路径
path_arr = np.zeros((M,T),dtype=int) # 初始值为-1

# Viterbi算法
def viterbi():
    # 按时间走
    for t in range(T):
        # 目前观测值
        obs_idx = obs_option.index(obs_list[t])
        # 初始值
        if t == 0:
            state_idx= state_option.index(s_begin)
            pro_arr[state_idx,t] = B[state_idx,obs_idx]*1
        else:
            # t+1层的循环
            for s1 in range(M):
                # t+2层的循环
                pro_value = []
                for s2 in range(M):
                    pro_value.append(decimal.Decimal(str(pro_arr[s2,t-1]))*decimal.Decimal(str(A[s2,s1])))
                pro_arr[s1,t] = max(pro_value)*decimal.Decimal(str(B[s1,obs_idx]))  
                # 路径记录，概率不等于0才记录
                if pro_arr[s1,t]-0>1e-7:
                    max_idx = np.argmax(pro_value)
                    path_arr[s1,t] = max_idx
    
    # 最大可能状态对应的概率
    pro_max = np.max(pro_arr[s_end,T-1])

    # 路径回溯
    path_list = []
    path = s_end
    for t in range(T-1,-1,-1):
        path_list.append(path)
        path = path_arr[path,t]

    path_list = sorted(path_list,reverse=True)


    return pro_max,path_list,pro_arr,path_arr

if __name__ == '__main__':
    pro_max,path_list,pro_arr,path_arr = viterbi()
    print(pro_arr)
    print(path_list)
    print(pro_max)
    print(path_arr)
    



