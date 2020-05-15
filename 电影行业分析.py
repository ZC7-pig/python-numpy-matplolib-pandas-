
"""
1.案例背景
电影公司制作一部新电影推向市场时，要想获得成功，通常要了解电影市场趋势，
观众喜好的电影类型，电影的发行情况，改编电影和原创电影的收益情况，以及观众喜欢什么样的内容。

本案例来源于kaggle上的TMDB 5000 Movie Dataset数据集，为了探讨电影数据可视化，
为电影的制作提供数据支持，主要研究以下几个问题：

电影类型如何随着时间的推移发生变化的？
电影类型与利润的关系？
Universal和Paramount两家影视公司的对比情况如何？
改编电影和原创电影的对比情况如何？
电影时长与电影票房及评分的关系？
分析电影关键字
"""
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

credits_ = pd.read_csv(r'tmdb-movie-metadata\tmdb_5000_credits.csv',encoding='utf-8',engine='python')
# print(credits_.info())
movies = pd.read_csv(r'tmdb-movie-metadata\tmdb_5000_movies.csv',encoding='utf-8',engine='python')
# print(movies.info())

#根据sum确定title是否对应
# print((credits_['title']==movies['title']).sum())

#一.数据合并

# #修改表的名称
credits_.rename(columns={'movie_id':'id'},inplace=True)

#主键合并
data = pd.merge(credits_, movies, on=['title','id'], how='outer')
# print(data.info())


#二.数据分析
# 电影类型如何随着时间的推移发生变化的？*************************************************************************************************************************************

#(1)找到空值的电影；# 2014-06-01
# print(data.loc[data['release_date'].isnull(), 'title'])

#(2)填充空值：
data['release_date'].fillna('2014/06/01', inplace=True)

#(3求一共有多少种类型的电影类型
#a.将json转为python类型
data["genres"]=data["genres"].transform(json.loads)
# print(data["genres"].head())

#b.提取电影类型

type_set=set()  #得到电影类型的集合
def get_movie_type(element):
    type_list=[]
    if element:
        for valus in element:
            name=valus['name']
            type_list.append(name)
            type_set.add(name)
    return ' '.join(type_list)  #将列表转换为字符串

data['genres']=data['genres'].transform(get_movie_type)
# print(data['genres'])
# print(type_set)

#(4).字符串操作里的方法----判断genres中是否包含电影类型的字符串,包含返回true,之后根据 true为1.flase为零,
for movie_genres_type in list(type_set):
   data[movie_genres_type]= data['genres'].str.contains(movie_genres_type).transform(lambda  x:1 if x else 0)
# print(data.shape)

#(5).电影上映时间处理
data['release_year']=pd.to_datetime(data['release_date']).dt.year
# print(data['release_year'].min())
# print(data['release_year'].max())

#(6)年份分组
groupby_year=data.groupby("release_year")[list(type_set)].sum()

#(7)画折线图

# plt.figure()

# x=groupby_year.index
# for movie_type in list(type_set):
#     y=groupby_year[movie_type]
#     plt.plot(x,y)
# plt.legend(list(type_set))
# plt.show()

#所有类型电影总数占比****
""" movie_type_num=[]
for type_num in list(type_set):
    movie_type_num.append(data[type_num].sum())
 """

# plt.figure()
# movie_type_num=data[list(type_set)].sum(axis=0).sort_values()
# x=movie_type_num

# label=movie_type_num.index
# plt.pie(x,labels=label,autopct='%1.1f%%')
# plt.show()

#二.电影类型与利润的关系******************************************************************************************************************************************************
#(1)计算利润
data['profit']=data['revenue']-data['budget']
#(2)每种类型电影的平均利润
type_mean_profit_list=[]
for movie_type in list(type_set):
    type_mean_profit=(data.loc[data[movie_type]==1,'profit'].mean())/10000
    type_mean_profit_list.append(type_mean_profit)
# print(type_mean_profit_list)

finally_movie_type_mean_profit=pd.DataFrame({"movie_type":list(type_set),"profit_mean":type_mean_profit_list})
mean_sort=finally_movie_type_mean_profit.sort_values(by="profit_mean")

# # 绘图
# plt.figure()
# x = np.arange(len(list(type_set)))
# plt.barh(x,mean_sort['profit_mean'])
# plt.yticks(x,mean_sort['movie_type'])
# plt.xlabel("profit (W $)")
# plt.ylabel("movie type")
# plt.show()

#三.Universal和Paramount两家影视公司的对比情况如何？**********************************************************************************************
#(1)找到这两家公司发行的电影
data['Paramount Pictures']=data['production_companies'].str.contains("Paramount Pictures")
data['Universal Pictures']=data['production_companies'].str.contains("Universal Pictures")

#(2) 发行影片盈利分析
#a.平均利润
ParamountPictures_meanprofit=data.loc[data['Paramount Pictures'],'profit'].mean()
UniversalPictures_meanprofit=data.loc[data['Universal Pictures'],'profit'].mean()

#b.发行影片数量
ParamountPictures_num=data['Paramount Pictures'].sum()
UniversalPictures_num=data['Universal Pictures'].sum()

#画图
p1=plt.figure()
x=[1,2]
y1=[ParamountPictures_meanprofit,UniversalPictures_meanprofit]
y2=[ParamountPictures_num,UniversalPictures_num]
#电影利润对比
p1.add_subplot(1,2,1)
plt.bar(x,y1)
labels=['Paramount','Universal']
plt.xticks(x,labels)
#电影发片量对比
p1.add_subplot(1,2,2)
plt.bar(x,y2)
plt.xticks(x,labels)
plt.show()