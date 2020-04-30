import pandas as pd 
import numpy as np 


# 打印结果
# count      2779 ---   非空数
# unique      157 ---   去重后的数
# top       白饭/大碗 ---众数(若多个众数,只显示一个)
# freq         92 ---   众数出现的次数

df = pd.read_excel('C:/Users/ZC7/Desktop/数据分析/day04/meal_order_detail.xlsx')
# print(df.head())

# 删除表中所有为nan值的列
mask = (df.count()==0)

print(mask.index[mask])
labels_nan = mask.index[mask]
df1 = df.drop(labels_nan,axis=1)
print(df1)

# 删除所有值相同的列
# columns_drop=[]
# for i in df1.columns:
#     df1[i]=df1[i].astype('category')
#     freq = df1[i].describe()['freq']
#     if freq==df1.shape[0]:
#         columns_drop.append(i)
# print(columns_drop)
# df2 = df1.drop(labels=columns_drop,axis=1)
# print(df2.shape)

#**********************************************
#七.转换处理时间序列
#1.转换为标准时间格式
# df['place_order_time']=pd.to_datetime(df['place_order_time'])

#2.提取时间:
# print(df['place_order_time'][0].year)

#提取其中所有的的year
#方式一
# print([i.year for i in df['place_order_time']])
#.year   /.month    /.day   /.hour     /.minute    /.second   /.quarter ---季节    /.weekday_name---第几周   /.dayofyear---一年中第几天  /.date--日期

#方式二--- .dt.****
# print(type(df['place_order_time'].dt.date))

#3.时间运算
#(1) weeks  (2)days   (3)hours   (4)minutes
#将df 时间整体后移一天
# date1 = df['place_order_time']+pd.Timedelta(days=1)
# print(date1)
