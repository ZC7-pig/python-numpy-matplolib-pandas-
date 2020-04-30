from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
mpl.rcParams['axes.unicode_minus'] = False # 解决‘-’bug


#1.生成画布
plt.figure()

#2.给定坐标
x = [1,2,3,4,5,6]
y = [5,6,2,8,5,1]
y1 = [1,2,3,4,5,6]

#3.绘图  
#  label:图例名字
#  linestyle:-  \  -- \  -.
#  linewidth:粗细 
#  color:
#  marker:点的样式
#  markersizr:点的大小
#  markerfacecolor:点的颜色

plt.plot(x,y,label='三月',marker='x',markersize=25,markerfacecolor='yellow')
plt.plot(x,y1,label='四月')
plt.title('demo')

#刻度
plt.xticks([2,4,5,6,8])
plt.yticks(y)

#轴名称
plt.xlabel('x轴')
plt.ylabel('y轴')

#图例--有位置要求,必须画在绘图之后
plt.legend()

#保存图片p
# plt.savefig('demo.png')

plt.show()