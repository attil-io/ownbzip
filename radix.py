#!/usr/bin/python

def radixSort(a,n,maxLen,valueGetterFun=None):
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        exponent = n**x
        for y in a:
            if valueGetterFun:
               mappedY=valueGetterFun(y)
            else:
               mappedY=y
            bins[(mappedY/exponent)%n].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a

#a=[1, 2, 3]
#a=[44, 43, 100, 123, 100, 1]
#def inverter(num):
#    return 65536-num
#
#sorteda=radixSort(a, 65536, 1, inverter)
#print sorteda

