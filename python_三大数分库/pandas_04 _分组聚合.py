import pandas as pd 
import numpy as np 
data={"姓名":["张三","李四","王五","赵六"],
                "年龄":[18,19,20,19],
                "班级":[141,142,141,142],
                "成绩":[87,90,87,92],
                "学号":[20140214029,1444328,20110360,201123233]}
df=pd.DataFrame(data)
score_data = df.loc[:,["班级","成绩","年龄"]]
#一.分组聚合方式
#1.groupby()方法--对表格进行拆分,返回的是分组对象
#2.对分组结果进行聚合操作,查看结果
grou = score_data.groupby(by="班级")
grou_mean=grou.mean()
# print(grou_mean.reset_index())
#3.辅助操作--变更作为索引的分组键,将分组键变成一列正常值
"""
     成绩
班级
141  87
142  91
"""
#使用reset_index()之后
"""
    班级  成绩
0  141  87
1  142  91
"""

#二.agg聚合方法 ---重点
#1.对不同的列应用相同的统计方法
# print(grou.agg([np.sum,np.mean]))
#2.对不同的列用不同的方法
# print(grou.agg({"成绩":[np.mean,np.sum],"年龄":np.mean}))

#三.apply 聚合
print(grou.apply(np.mean))

#四.transform
print(grou["成绩"].transform(lambda x: x**2))