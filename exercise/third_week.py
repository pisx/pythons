__author__ = 'pisx'
#
"""
python 第三周作业
"""
import math
import time

#
# w = int(input())
# h = float(input())
# print("%.2f" % (w/(h*h)))

# H = 60*60
# M = 60
# sec = int(input())
# if sec > 0 :
#     h = int(sec/H)
#     m = int(sec%H/M)
#     s = sec%M
#     print("%d %d %d" % (h,m,s))

#3-1
# a = int(input())
# r=0
# if a > 3:
#     for i in range(1,a):
#         if i%3==0 or i%5==0:
#             r += i
#
#     print(r)


def is_prime(n):
    if n == 1 or n==0:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        flag = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                flag = False
                break
        return flag

#Eratosthenes
#埃拉托斯特尼筛法
def eratosthenes(n):
    if n > 1:
        #初始化一个长度为n的list
        s = time.time()
        lst = [1 for i in range(n+1)]
        e = time.time()
        print("初始化长度为 %d 的list，耗费时间：%d 。" % (n,(e-s)))
        lst[0] = 0
        lst[1] = 0

        for i in range(2,n+1):
            #目前序列第一个素数
            if lst[i] == 1:
                prime_cursor = i
                t = prime_cursor
                while (t+prime_cursor) <= n:
                    t += prime_cursor
                    lst[t] = 0

        primes = []
        for j in range(2,n+1):
            if lst[j]==1:
                primes.append(j)
    return primes

#用list存储已知素数 ，当前数不能被已有素数整除，则此数为素数
def find_prime(n):
    if n == 0 or n == 1:
        return []
    if n > 1:
        primes = []
        for i in range(2, n):
            isPrime = True
            if len(primes) > 0:
                for j in primes:
                    #这一步判断很关键
                    if j > int(math.sqrt(i)):
                        break
                    if i % j == 0:
                        isPrime = False
                        break
            if isPrime:
                primes.append(i)
        return primes


#
n = 1000000
print("求%d以内的素数：" % n)

begin = time.time()
find_prime(n)
end = time.time()
print("试除已有素数法耗费时间：%d s" % (end-begin))

begin = time.time()
primes1 = eratosthenes(n)
end = time.time()
print("筛法耗费时间：",end-begin,"s")

begin = time.time()
primes2 = []
flag = False
for i in range(n):
    if is_prime(i):
        primes2.append(i)
# print(primes)
end = time.time()
print("\n试除法耗费时间：%d s" % (end-begin))
#3-2
#输入正整数n ，求n以内所有素数的和
#
# n = int(input())
#
# if n>=1:
#     sum = 0
#     for i in range(1,n):
#         if is_prime(i):
#             sum += i
# print(sum)

#3-3
#计算在1901年1月1日至2000年12月31日间共有多少个星期天落在每月的第一天上
# total = 1
# month = 1
# day = 1
# month_days = 31
# count = 0
# for y in range(1900, 2001):
#     for i in range(1, 13):
#         if i == 2:
#             if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
#                 month_days = 29
#             else:
#                 month_days = 28
#         elif i == 4 or i == 6 or i == 9 or i == 11:
#             month_days = 30
#         else:
#             month_days = 31
#
#         total += month_days
#         if y>1900 or (y==1900 and i==12):
#             if total % 7 == 0:
#                 count += 1
#
# print(count)

#3-4
#求n以内的循环素数的个数
# n = int(input())
# count = 0
# for i in range(2,n):
#     if is_prime(i):
#         if i<10:
#             count += 1
#         else:
#             t = i
#             top = 1
#             while t>10:
#                 t //=10
#                 top *= 10
#
#             flag = True
#             cycle = i
#             t = i
#             while t>0:
#                 remainder = t%10
#                 cycle//=10
#                 cycle += remainder*top
#                 if not is_prime(cycle):
#                     flag = False
#                     break
#
#                 t//=10
#             if flag:
#                 count += 1
# print(count)