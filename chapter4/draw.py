import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist

# 字体设置
plt.rc('font',family='Times New Roman')

# 降至二维
X1 = np.array([[-0.5,-0.5],[0.5,-0.5],[0.5,-0.5],[0.5,0.5]])
Y1 = np.array([[-0.5,-0.5],[-0.5,0.5],[-0.5,0.5],[0.5,0.5]])

fig = plt.figure()

# 坐标轴设置
ax = axisartist.Subplot(fig, 111)  
#将绘图区对象添加到画布中
fig.add_axes(ax)
#通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
#ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0,0)
#给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("->", size = 1.0)
#添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
#设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

# 散点图
plt.scatter(X1[:,0],X1[:,1],marker='o',c='b',label='$\omega_1$')
plt.scatter(Y1[:,0],Y1[:,1],marker='*',c='r',label='$\omega_2$')
# 坐标轴刻度
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.xticks([-1,-0.5,0,0.5,1])
plt.yticks([-1,-0.5,0.5,1])
# 坐标标注
plt.annotate('(1/2,1/2)',xy=(0.5,0.5),xytext=(0.5+0.1,0.5+0.1))
plt.annotate('(1/2,-1/2)',xy=(0.5,-0.5),xytext=(0.5+0.1,-0.5+0.1))
plt.annotate('(-1/2,-1/2)',xy=(-0.5,-0.5),xytext=(-0.5+0.1,-0.5+0.1))
plt.annotate('(-1/2,1/2)',xy=(-0.5,0.5),xytext=(-0.5+0.1,0.5+0.1))

plt.legend()
plt.title('3Dimension to 2Dimension',y=1.05)
plt.savefig('2dim.png')
plt.close(fig)

# ---------------
# 降至一维
X2 = np.array([-0.5,0.5,0.5,0.5])
Y2 = np.array([-0.5,-0.5,-0.5,0.5])

fig = plt.figure(figsize=(5,3))
ax = axisartist.Subplot(fig, 111)  
#将绘图区对象添加到画布中
fig.add_axes(ax)
#通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
#ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0,0)
#给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("->", size = 1.0)
#设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")

plt.scatter(X2,[0]*len(X2),marker='o',c='b',label='$\omega_1$')
plt.scatter(Y2,[0]*len(Y2),marker='*',c='r',label='$\omega_2$')
plt.xlim(-1,1)
plt.xticks([-1,-0.5,0,0.5,1])
plt.annotate('1/2',xy=(0.5,0),xytext=(0.5+0.1,0.5))
plt.annotate('-1/2',xy=(-0.5,0),xytext=(-0.5+0.1,0.5))
plt.legend()
plt.title('3Dimension to 1Dimension',y=1.05)
plt.savefig('1dim.png')
plt.close(fig)

