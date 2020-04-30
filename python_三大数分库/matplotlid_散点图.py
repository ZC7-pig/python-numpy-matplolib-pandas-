from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np 
import random
mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
mpl.rcParams['axes.unicode_minus'] = False # 解决‘-’bug

#一.散点图
# plt.figure()

# x = np.arange(0,2*np.pi,0.1)
# y= np.sin(x)

# plt.scatter(x,y)

# plt.show()

#***********************************************
#子图
# p1=plt.figure()

# x = np.arange(0,2*np.pi,0.1)
# y= np.sin(x)
# #添加第一个子图
# p1.add_subplot(2,1,1)
# plt.scatter(x,y)

# #第二个子图
# p1.add_subplot(2,3,4)
# plt.plot(x,y,label='折线',color='red')
# plt.legend()
# plt.show()

#***********************************************
# #直方图
# plt.figure()
# salary = np.random.randn(100000)
# group = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
# plt.hist(salary,group)
# plt.show()
