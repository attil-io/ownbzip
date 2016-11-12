#!/usr/bin/python

import math

def manberMyers(word):
	def safeGetIdx(arr, idx):
	    if idx < len(arr):
	       return arr[idx]
	    else:
	       return -1

	n=len(word)
	P=[]
	P0 = []
	sortedword = sorted(set(word))
	for i in range(n):
	    P0.append(sortedword.index(word[i])) 

	P.append(P0)

	cnt = 1
	for k in range(1, int(math.ceil(math.log(n, 2))) + 1):
	    L=[]
	    for i in range(n):
		L.append((P[k-1][i], safeGetIdx(P[k-1], i + cnt), i))
	    sortedL = sorted(L, key=lambda x: (x[0], x[1]))
	    Pk = [0] * n
	    for i in range(n):
		if i > 0 and sortedL[i][0] == sortedL[i - 1][0] and sortedL[i][1] == sortedL[i - 1][1]:
		   Pk[sortedL[i][2]] = Pk[sortedL[i-1][2]]
		else:
		   Pk[sortedL[i][2]] = i
	    P.append(Pk)
	    cnt = cnt * 2
	return P[-1]


