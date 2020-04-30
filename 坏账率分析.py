#1.是否收入越高的人坏账率越高
#2.计算年龄与坏账率有什么关系
#3.计算家庭人口数量与坏账率的关系
import pandas as pd 
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np 


mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
mpl.rcParams['axes.unicode_minus'] = False # 解决‘-’bug

df = pd.read_csv('C:/Users/ZC7/Desktop/数据分析/day07/loan.csv',encoding='gbk')
# print(df.head())
# print(df.info())
"""  用户ID  好坏客户年龄 负债率   月收入   家属数量
    0     1     1  45  0.802982   9120.0   2.0
    1     2     0  40  0.121876   2600.0   1.0
    2     3     0  38  0.085113   3042.0   0.0
    3     4     0  30  0.036050   3300.0   0.0
    4     5     0  49  0.024926  63588.0   0.0 """


# sermin=(ser1.mean()-3*ser1.std())
# sermax=(ser1.mean()+3*ser1.std())
# mas1=ser1<sermin
# mask2=ser1>sermax
# print(ser1[mask2|mas1].sort_values(ascending=False))

#清洗数据
#填补删除缺失数据
data = df.fillna({'月收入':df['月收入'].mean()})
data = data.dropna(axis=0,how='any')

#删除异常值
ser=data['月收入']
sermin=ser.mean()-3*ser.std()
sermax=ser.mean()+3*ser.std()
mask1=ser<sermin
mask2=ser>sermax
mask=mask1|mask2
drop_list=mask.index[mask]

datafinal = data.drop(labels=drop_list,axis=0)
# print(datafinal.loc[:10][:])



#切割分组
cut_income=np.arange(0,sermax,1000)
income = pd.cut(datafinal['月收入'],cut_income)
# print(income)

income_count = datafinal['好坏客户'].groupby(income).count()
bad_count = datafinal['好坏客户'].groupby(income).sum()
bar_per = bad_count/income_count
print(bad_count.values)
# print(len(cut_income[1:]))

plt.figure()
plt.plot(cut_income[1:],bad_count.values)
plt.xlabel("与月收入")
plt.ylabel("坏账人数")
plt.show()


# #
