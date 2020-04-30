import numpy as np 
import random
#一.数值统计
#1.1排序sort() 此方法无返回
# arr1 = np.array([1,5,2,5,7])
# arr1.sort()
# print(arr1)
# arr2 = np.random.randint(1,11,size=[2,5])
# arr2.sort()#默认时横向排列
# arr2.sort(axis=0)#纵向排列
# print(arr2)

#1.2排序argsort()  返回排序后的索引
# print(arr2.argsort())
# print(arr2.argsort(axis=0))

#2.去重
# name = np.array(['a','a','b','b','b','c'])
# print(np.unique(name))

#3.1 tile重复
# arr3= np.array([1,2,3,4]).reshape(2,2)
# print(np.tile(arr3,2))

#3.2repeat:按照元素重复
# print(arr3.repeat(2,axis=1))

#4统计函数
#4.1求和
arr4 = np.array([2,1,3,4]).reshape(2,2)
# print(np.sum(arr4))
# print(np.sum(arr4,axis=0))
# print(np.sum(arr4,axis=1))

#4.2 mean
# print(np.mean(arr4))
# print(np.mean(arr4,axis=0))
# print(np.mean(arr4,axis=1))

#4.3 std 以下统计函数用法同上
#4.4 var
#4.5 min
#4.6 max
#4.7 min/max 索引 argmin()/argmax()
#cumsum 累乘
#******************************************************
#一.矩阵创建
#1.
# mat1 = np.mat('1 2 3;4 5 6;7 8 9')
# print(mat1.dtype)
#2.数据拼接转换
# arr1 = np.eye(3)
# arr2 = 2*arr1
# mat2 = np.bmat('arr1 arr1;arr2 arr2')
# mat3 = np.bmat('arr2 arr2;arr1 arr1')

#3.矩阵加加减乘除
# print(mat2+mat3)
# print(mat2*mat3)

#4.对应元素相乘
mat1 = np.mat('1 2 3;4 5 6;7 8 9')
mat2 = np.mat('1 2 3;4 5 6;7 8 9')
# print(np.multiply(mat1,mat2))
#*******************************************
#四.文件读取
#1.二进制文件存储与读取
#1.1   .npy .npz 二进制文件后缀


arr1 = np.array([1,1,1])
arr2 = np.array([2,2,2])
#生成 npy文件 -----存储单个数组
# np.save('save_arr',arr1)
#生成 npz ---存储多个数组 npz文件中包含多个npy文件
# np.savez('savez_arr',arr1,arr2)

#读取npy
# data = np.load('save_arr.npy')
# print(data)
# #读取npz
# data1 = np.load('savez_arr.npz')
# list1 = list(data1)--其中包含[arr_0,arr_1]
# print(data1['arr_0'])

#2.文本文件
#生成
# np.savetxt("arr1.txt",arr2,fmt='%d',delimiter=',')#%d表示整形 delimiter 分隔符
#读取
data = np.loadtxt('arr1.txt',delimiter=',',dtype='str')
print(data)