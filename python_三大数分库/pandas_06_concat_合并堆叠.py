import pandas as pd 

data1={"姓名":["张三","李四","王五","赵六"],
                "年龄":[18,19,20,19],
                "班级":[141,142,141,142],
                "成绩":[87,90,87,92],
                "学号":[20140214029,1444328,20110360,201123233],
                "性别":["男","女","女","女"]}
df1=pd.DataFrame(data1)


# data2={"姓名":["张","李","王","赵"],
#                 "年龄":[18,19,20,19],
#                 "班级":[141,142,141,142],
#                 "成绩":[87,78,87,92],
#                 "学号":[20140214029,14121328,20110360,201123233],
#                 "性别":["女","女","男","女"]}
# df2=pd.DataFrame(data2)
# print(df1)
# print(df2)


# print(pd.concat([df1,df2]))
# 横向拼接
# print(pd.concat([df1,df2],axis=1))
# 纵向拼接
# print(pd.concat([df1,df2],axis=0,join="inner"))
# inner 是两个表的交集,outer是两个表的并集

#*************************************************************
# 主键拼接合并

database1={"A":["A0","A1","A2","A3"],
                "B":["B0","B1","B2","B3"],
                "Key1":["K0","K0","K1","K3"],
                "Key2":["K0","K1","K0","K1"],
                }
left=pd.DataFrame(database1)
database2={"C":["C0","C1","C2","C3"],
                "D":["D0","D1","D2","D3"],
                "Key1":["K0","K1","K1","K2"],
                "Key2":["K0","K0","K0","K0"],
                }
right=pd.DataFrame(database2)
print(left)
print(right)
print(pd.merge(left,right,on="Key1"))
#默认是inner
#how="inner"  : 内连接 :只保留公共的主键
#how = "outer":外连接 : 保留所有数据
#how = "left" : 左连接 : 以左表中的键为主
#how = "right" : 右连接 : 以右表中的键为主

"""
    A   B Key1 Key2
0  A0  B0   K0   K0
1  A1  B1   K0   K1
2  A2  B2   K1   K0
3  A3  B3   K2   K1
    C   D Key1 Key2
0  C0  D0   K0   K0
1  C1  D1   K1   K0
2  C2  D2   K1   K0
3  C3  D3   K2   K0
    A   B Key1 Key2_x   C   D Key2_y
0  A0  B0   K0     K0  C0  D0     K0
1  A1  B1   K0     K1  C0  D0     K0
2  A2  B2   K1     K0  C1  D1     K0
3  A2  B2   K1     K0  C2  D2     K0
4  A3  B3   K2     K1  C3  D3     K0
"""
# print(pd.merge(left,right,on="Key1",how="outer"))
# print(pd.merge(left,right,on="Key1",how="left"))
# print(pd.merge(left,right,on="Key1",how="right"))

#多个主键
# print(pd.merge(left,right,on=["Key1","Key2"]))
"""
    A   B Key1 Key2
0  A0  B0   K0   K0
1  A1  B1   K0   K1
2  A2  B2   K1   K0
3  A3  B3   K3   K1
    C   D Key1 Key2
0  C0  D0   K0   K0
1  C1  D1   K1   K0
2  C2  D2   K1   K0
3  C3  D3   K2   K0
    A   B Key1 Key2   C   D
0  A0  B0   K0   K0  C0  D0
1  A2  B2   K1   K0  C1  D1
2  A2  B2   K1   K0  C2  D2
"""
# print(pd.merge(left,right,left_on="Key1",right_on="Key2"))
#当左右表的主键名称不一致时,通过分别声明各自表的主键进行比较
"""
   A   B Key1 Key2
0  A0  B0   K0   K0
1  A1  B1   K0   K1
2  A2  B2   K1   K0
3  A3  B3   K3   K1
    C   D Key1 Key2
0  C0  D0   K0   K0
1  C1  D1   K1   K0
2  C2  D2   K1   K0
3  C3  D3   K2   K0
    A   B Key1_x Key2_x   C   D Key1_y Key2_y
0  A0  B0     K0     K0  C0  D0     K0     K0
1  A0  B0     K0     K0  C1  D1     K1     K0
2  A0  B0     K0     K0  C2  D2     K1     K0
3  A0  B0     K0     K0  C3  D3     K2     K0
4  A1  B1     K0     K1  C0  D0     K0     K0
5  A1  B1     K0     K1  C1  D1     K1     K0
6  A1  B1     K0     K1  C2  D2     K1     K0
7  A1  B1     K0     K1  C3  D3     K2     K0
"""
#重叠合并--补全操作
# 以第一张表数据为主,用第二张表的数据补齐前者缺失内容
print(left.combine_first(right))