import numpy as np 
#三.通过函数创建数组
#1.arange()
# arr1 = np.arange(1,10,2)
# print(arr1)

#2.等差数列
# arr2 = np.linspace(3,12,5)
# # np.linspace(1,10,5) 1为起始值,10为最终值,5为想要的数列的个数
# print(arr2)

#3.等比数列
# arr3 = np.logspace(1,4,4 ,base=2)
# #np.logspace(0,2,3) np
# print(arr3)

#4.全零数组
# arr4 = np.zeros((3,4))
# print(arr4.dtype)

#5.全1数组
# arr5 = np.ones((2,3))
# print(arr5)

#6.单位数组 (3X3数组)
# print(np.eye(3))

#7.对角数组
# print(np.diag([1,2,3,2]))
#***************************************************
#生成随机数
import random
#1.生成0-1的随机数
# arr5 = np.random.random(10)
# print(arr5)

#2.生成均匀分布 (十行五列)
# print(np.random.rand(10,5))

#3.正态分布
# print(np.random.randn(10,5))

#4.随机整数
# print(np.random.randint(2,7,size=[2,5]))
#**********************************************************
#四.数组访问
#1.一维数组访问
# arr7 = np.linspace(1,11,6)
# print(arr7[:3])
# print(arr7[::2])

#2.二维数组的方位
# arr8 = np.linspace(0,11,12).reshape([3,4])
# print(arr8[:2,2])

#bool值切片
    # arr8 = np.linspace(0,11,12).reshape([3,4])
    # mask = np.array([1,1,0,1],dtype=np.bool)
    # print(arr8[:,mask])
#*********************************************************************
# 五.变换数组形态
#1.一维边二维
# arr9 = np.arange(12)
# print(arr9.reshape(3,4))

#2.展平
# arr9 = np.arange(12).reshape(3,4)

# # print(arr9.ravel())
# #横向展平
# print(arr9.flatten())
# #纵向展平
# print(arr9.flatten('F'))

#2.数组组合
arr1 = np.ones((3,4))
arr2= 2*arr1

#横向堆叠
# print(np.hstack((arr2,arr1)))

#纵向堆叠
# print(np.vstack((arr1,arr2)))

#组合concatenate
# print(np.concatenate((arr1,arr2),axis=1))

#3.数组分割
# arr12 = np.diag([1,2,3,4])

# print(np.hsplit(arr12,2)) #竖着切

# print(np.vsplit(arr12,2)) #横着切
# print(np.split(arr12,2,axis=1))

#****************************************************
#六.数组的运算
#1.加法运算
# ar1 = np.arange(10)
# ar2 = np.arange(1,11)
# # print(ar1)
# # print(ar2)
# # print(ar1+ar2)
# #2.乘法运算
# # print(ar1*ar2)

# #二维操作
# ar3 = np.arange(4).reshape(2,2)
# print(ar3)
# ar4 =np.arange(1,5).reshape(2,2)
# print(ar4)
# print(ar3*ar4) #二维乘法操作


# print(ar3<2)#比较操作

#例:运用比较判断 bool取数
# aa = np.array([2,4,6,2,1,6,2,78,5,3])
# mask = aa<4
# print(aa[mask])
# print("*******")
# bb= np.arange(12).reshape(3,4)
# print(bb[bb<4])
#*****************************
#数组广播运算   进行运算操作的一维数组的个数等于二维数组的列数,则一维数组进行扩充操作,可以进行运算
bb= np.arange(12).reshape(3,4)
cc = np.array([[3],[3],[3]])
dd = np.array([3,3,3,3])
print(bb+cc)
print(bb+dd)