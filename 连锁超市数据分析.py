import pandas as pd 


#2.哪些商品比较畅销
df = pd.read_csv('C:/Users/ZC7/Desktop/数据分析/day07/order-14.3.csv',encoding='gbk')
# print(df.info())
# print(df.head())

# #1.哪类的商品比较畅销   (访问dataframe)
# idsales=df.groupby(by="类别ID")[['销量']].sum().sort_values(by="销量",ascending=False)
# print(idsales[:5].index)
# """ 类别ID
# 922000003  425.328
# 922000002  206.424
# 923000006  190.294
# 915030104  175.059
# # 922000001  121.355 """

# print(df.head())

# #2.哪些商品比较畅销    (访问Series)
# goodssales = df.groupby(by='商品ID')['销量'].sum().sort_values(ascending=False)
# print(goodssales[:5].index)
# """ 商品ID
# 29989059    391.549
# 29989072    102.876
# 30022232    101.000
# 30031960     99.998
# 29989157     72.453 """

#3.求不同门店的销量占比--饼图

# df[["销售额"]]=pd.DataFrame(df['销量']*df['单价'])
# sales = df.groupby(by="门店编号")[['销售额']].sum().sort_values(by="销售额",ascending=False)
# sales[['销售额占比']]=pd.DataFrame(sales['销售额']/sales['销售额'].sum())
# print(sales)


# from matplotlib import pyplot as plt
# import matplotlib as mpl
# mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决‘-’bug

# plt.figure()
# plt.pie(sales['销售额占比'],autopct='%1.1f%%',labels=sales.index)
# plt.show()


#4.哪个时间段是超市的客流高峰期
#(1去重)
dfdemo = df.drop_duplicates(subset='订单ID')
#(1)格式化时间
dfdemo["小时"]=pd.to_datetime(dfdemo['成交时间']).dt.hour
print(dfdemo.groupby(by='小时')['订单ID'].count().sort_values(ascending=False))
