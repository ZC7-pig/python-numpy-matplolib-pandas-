import pandas as pd 
import numpy as np 
data={"姓名":["张三","李四","王五"],
                "年龄":[18,19,20],
                "班级":[141,142,141],
                "tel":[17865164331,17865164332,17865164313],
                "学号":[20140214029,1444328,20110360]}
df=pd.DataFrame(data)
# print(df)

#1.查询--数据切片
#a.索引切片方式
# print(df["姓名"])#注意这里时Series类型
# print(df[["姓名"]])#这里是二维的是dataframe类型
# print(df[["姓名","年龄"]])#切片多列
# print(df[["姓名","年龄"][:2]])#切片多列的前N行

#b.灵活切片:
#loc / iloc
# df.loc[行索引名称or条件,列索引名称or条件]
# df.iloc[行索引位置,列索引位置]
# print(df.loc[:2,["姓名","tel"]])#注意这里的":2"是前后闭区间
# print(df.iloc[:2,:2])#这里":2"是左闭右开区间
# #loc条件切片 例题
# mask1=df["年龄"]>19
# mask2=df["班级"]==141
# mask=mask1 & mask2
# print(df.loc[mask,["姓名","tel"]])


#2.更改数据
# df.loc[df["姓名"]=="张三","年龄"] =88
# print(df)

#3 增加数据
#新增新列
df["性别"]=pd.Series(["男","女","男"])
# #新增行
# #a.  append直接追加字典
# df=df.append([{"姓名":"赵六","年龄":22,"班级":143,"tel":146848954,"学号":12231,"性别":"女"}],ignore_index=True)
# #ignore_index=True---为了确保index索引是追加的,若为false 追加行的索引显示为0
# print(df)

#4 删除数据
#删除一列  注意:axis=1 必须有
# print(df.drop(labels=["tel","性别"],axis=1))

#删除一行
# print(df.drop(labels=0,axis=0))

#以上删除操作drop是有返回的,要对原表操作,  如下,此方法无返回
# df.drop(labels=0,axis=0,inplace=True)
# print(df)

#5.统计分析
#a.运用numpy的方法
# print(np.mean(df["年龄"]))

#b.pandas 统计方法
# print(df["年龄"].mean())

#count()
# print(df["姓名"].count())#返回""姓名"里非空(none)值的数量
# print(df[["年龄","班级"]].count())

#频数统计
# print(df["性别"].value_counts())

#众数
# print(df)
# print(df["年龄"].mode())
#*********************************************************
#describe()
print(df[["年龄","班级"]].describe())
print(df[["年龄","班级"]].describe().iloc[:3,0])
# print(df["姓名"].describe())