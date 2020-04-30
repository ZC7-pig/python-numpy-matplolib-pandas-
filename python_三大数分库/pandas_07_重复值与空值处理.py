import pandas as pd 
import numpy as np

#数据清洗
#一.检测处理重复值
#1.记录去重
df= pd.read_excel('C:/Users/ZC7/Desktop/数据分析/day04/meal_order_detail.xlsx')
#
#a.针对Series的去重
# print(df["dishes_name"].drop_duplicates())
# print(df["dishes_name"].shape)

#b.针对Dataframe去重
# print(df.drop_duplicates(subset="dishes_name"))

#2.特征重复
#元素类型:数值型
#方法:求相似度{spearman,kedall}

# corrdet = df[["counts","amounts"]].corr(method="kendall")
# print(corrdet)

#二.检测处理缺失值:
#1.判断空值
#isnull() ---判断是否为空
# print(df["年龄"].isnull())#返回true和false

#notnull() ---判断不是空值

#2.删除:dropna()
#a.删除空值所在行
#(1)当一行全部为空时,才删除
# print(df.dropna(axis=0,how="all"))
#(2)当一行有一个值为空值时,删除
# print(df.dropna(axis=0,how="any"))

#b.删除空值所在列
# print(df.dropna(axis=1,how="any"))

#3.填充空值
# print(df.fillna(11111))

#4.插值:
# a.线性关系插值(需数据服从完全线性分布--如:1,3,5,Nan,7)

# from scipy.interpolate import interp1d

# x = np.array([1,2,3,4,5,8,9])
# y = np.array([3,5,7,9,11,17,19])
# y1 = np.array([2,8,18,32,50,128,162])

# line1 = interp1d(x,y,kind="linear")
# print(line1([6,7]))

# #b.多项式插值: lagrange,牛顿插值

# from scipy.interpolate import lagrange
# larg1 = lagrange(x,y1)
# print(larg1([6,7]))

#检测处理异常值
#运用3σ 经验法则
ser1=df["counts"]

sermin=(ser1.mean()-3*ser1.std())
sermax=(ser1.mean()+3*ser1.std())
mas1=ser1<sermin
mask2=ser1>sermax
print(ser1[mask2|mas1])