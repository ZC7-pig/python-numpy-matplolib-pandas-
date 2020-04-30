import pandas as pd 
import numpy as np 

data={"姓名":["张三","李四","王五","赵六"],
                "年龄":[18,19,20,19],
                "班级":[141,142,141,142],
                "成绩":[87,90,87,92],
                "学号":[20140214029,1444328,20110360,201123233],
                "性别":["男","女","女","女"]}
df=pd.DataFrame(data)

#透视表
# print(pd.pivot_table(df[["班级","年龄","成绩"]],columns="班级",aggfunc='mean'))
"""
#行分组索引    
班级  141  142
年龄   19   19
成绩   87   91
"""
# print(pd.pivot_table(df[["班级","年龄","成绩"]],index="班级",aggfunc='mean'))
"""
#列分组索引
     年龄  成绩
班级
141  19  87
142  19  91
"""
# print(pd.pivot_table(df[["班级","性别","年龄","成绩"]],index=["班级","性别"],aggfunc='mean'))
"""
行多重分组
        年龄  成绩
班级  性别
141 女   20  87index
    男   18  87
142 女   19  91
"""
# print(pd.pivot_table(df[["班级","性别","年龄","成绩"]],index="班级",columns="性别",aggfunc='mean'))
"""
#行列双重索引
       年龄          成绩
性别      女     男     女     男
班级
141  20.0  18.0  87.0  87.0
142  19.0   NaN  91.0   NaN
"""
print(pd.pivot_table(df,index="班级",values="成绩",aggfunc='mean'))
#Values=   指定想要看的一列

# print(pd.pivot_table(df,index="班级",columns="性别",aggfunc='mean',fill_value="空"))
# fill_value=   缺失值填充
"""
              学号                 年龄        成绩
性别             女            男     女   男     女   男
班级
141   20110360.0  2.01402e+10  20.0  18  87.0  87
142  101283780.5            空  19.0   空  91.0   空
"""
# print(pd.pivot_table(df,index="班级",values="成绩",aggfunc='mean',margins=True))
#margins=True  汇总开关
# margins_name="All"
"""
     成绩
班级
141  87
142  91
All  89
"""
#**********************************************
#交叉表
crossdata = pd.crosstab(index=df["班级"],values=df["成绩"],columns=df["性别"],aggfunc=np.sum)
print(crossdata)