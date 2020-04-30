
import pandas as pd 
import numpy as np 
df = pd.read_excel('C:/Users/ZC7/Desktop/数据分析/day04/meal_order_detail.xlsx')
df['place_order_time']=pd.to_datetime(df['place_order_time'])
df["date"]=df['place_order_time'].dt.date
# print(df["date"])
df["order_id"]=df["order_id"].astype("category")
dd = df[["date","order_id"]].groupby(by="date").describe()
print(dd['order_id']['unique'])