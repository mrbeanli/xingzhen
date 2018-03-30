# -*- coding: utf-8 -*-
from __future__ import print_function
# 1-->a   2-->b 3-->c 4-->d   a[1]-->question1

a=[None]*11                                                       #11是为了下标方便些，要不逻辑描述的时候容易出错
sum=[None]*4

for i in range(4**10):                                            #定义循环次数
    for j in range(1,11):                                         #定义每个问题的答案
        a[j]=int(i%(4**j)/(4**(j-1)))+1
    for k in range(4):                                            #计算每个选项的个数
        sum[k]=a.count(k+1)
                                                                  #开始逻辑运算
    if(
            (a[2]==1 and a[5]==3 or
             a[2]==2 and a[5]==4 or
             a[2]==3 and a[5]==1 or
             a[2]==4 and a[5]==2)
        and (a[3]==1 and a[3]!=a[6] and a[3]!=a[2] and a[3]!=a[4] or
             a[3]==2 and a[6]!=a[3] and a[6]!=a[2] and a[6]!=a[4] or
             a[3]==3 and a[2]!=a[3] and a[2]!=a[6] and a[2]!=a[4] or
             a[3]==4 and a[4]!=a[3] and a[4]!=a[6] and a[4]!=a[2])
        and (a[4]==1 and a[1]==a[5] and a[2]!=a[7] and a[1]!=a[9] and a[6]!=a[10] or
             a[4]==2 and a[2]==a[7] and a[1]!=a[5] and a[1]!=a[9] and a[6]!=a[10] or
             a[4]==3 and a[1]==a[9] and a[1]!=a[5] and a[2]!=a[7] and a[6]!=a[10] or
             a[4]==4 and a[6]==a[10] and a[1]!=a[5] and a[1]!=a[9] and a[2]!=a[7])
        and (a[5]==1 and a[8]==1 or
             a[5]==2 and a[4]==2 or
             a[5]==3 and a[9]==3 or
             a[5]==4 and a[7]==4)
        and (a[6]==1 and a[8]==a[4] and a[8]==a[2] or
             a[6]==2 and a[8]==a[1] and a[8]==a[6] or
             a[6]==3 and a[8]==a[3] and a[8]==a[10] or
             a[6]==4 and a[8]==a[5] and a[8]==a[9])
        and (a[7]==1 and sum.index(min(sum))+1==3 or
             a[7]==2 and sum.index(min(sum))+1==2 or
             a[7]==3 and sum.index(min(sum))+1==1 or
             a[7]==4 and sum.index(min(sum))+1==4)
        and (a[8]==1 and abs(a[7]-a[1])!=1 or
             a[8]==2 and abs(a[5]-a[1])!=1 or
             a[8]==3 and abs(a[2]-a[1])!=1 or
             a[8]==4 and abs(a[10]-a[1])!=1)
        and (a[9]==1 and (a[1]==a[6])!=(a[6]==a[5]) or
             a[9]==2 and (a[1]==a[6])!=(a[10]==a[5]) or
             a[9]==3 and (a[1]==a[6])!=(a[2]==a[5]) or
             a[9]==2 and (a[1]==a[6])!=(a[9]==a[5]))
        and (a[10]==1 and max(sum)-min(sum)==3 or
             a[10]==2 and max(sum)-min(sum)==2 or
             a[10]==3 and max(sum)-min(sum)==4 or
             a[10]==4 and max(sum)-min(sum)==1)

        ):
        for i in a[1:]:
            print(chr(ord('a')+i-1),end='')
        print('\n')
