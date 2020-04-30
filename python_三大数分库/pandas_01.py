import pandas as pd 
import numpy as np 

#一.构建dataframe
#方式一
# columns=['时间','第一产业','第二产业']
# values=[[2017,111,222],[2018,333,444],[2019,555,666]]
# index=[0,1,2]
# df=pd.DataFrame(columns=columns,data=values,index=index)
# print(df)

#方式二---构建字典传值
# data={'时间':[2017,2018,2019],
#       '第一产业':[111,333,555],
#       '第二产业':[222,444,555]
#       }
# df1=pd.DataFrame(data)
# print(df1)

#二.dataframe属性
# print('列索引:\n',df1.columns)
# print('行索引:\n',df1.index)
# print('元素:\n',df1.values)
# print('元素类型:\n',df1.dtypes)
# print('表结构(形状):\n',df1.shape)
# print('元素个数:\n',df1.size)

#创建Series
# data1=[2017,111,222]
# index=['a','b','c']
# se1=pd.Series(data1,index=index)
# print(se1)

#四.文件操作
#1.文本文件读取;  .csv / .txt
# df3=pd.read_csv('C:/Users/ZC7/Desktop/数据分析/day04/meal_order_info.csv',encoding='gbk',sep=',')
# print(df3.columns)
#a.通过文本的通用方式读取
# da4 = pd.read_table('C:/Users/ZC7/Desktop/数据分析/day04/meal_order_info.csv',encoding='gbk',sep=',')
# print(da4)
#excel文件
# 读取全部sheet内容:sheetname=None
# header:默认将第一行作为列索引,即  header=0
# skiprows=[0,1] 意思时跳过第一行第二行的数据,这时候header=0会将第三行当作新的索引
#更改excel里的列名 names=["替换的名字"]
df4 = pd.read_excel('C:/Users/ZC7/Desktop/数据分析/day04/meal_order_detail.xlsx')
print(df4.columns)
# #a.查看sheet名称
# print(list(df4.keys()))
# #b.获取某一张sheet的内容
# print(df4[list(df4.keys())[1]])
#*******************************************88
#文件存储
# df4.to_csv()#存为.csv
df4.to_excel()

