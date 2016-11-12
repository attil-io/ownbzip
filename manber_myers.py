#!/usr/bin/python

def manberMyers(word):
	def safeGetIdx(arr, idx):
	    if idx < len(arr):
	       return arr[idx]
	    else:
	       return -1

	n=len(word)
	Pprev = []
	sortedword = sorted(set(word))
	for i in range(n):
	    Pprev.append(sortedword.index(word[i])) 

	for cnt in [2**x for x in range(n) if 2**(x-1) < n]:
	    L=[]
	    for i in range(n):
		L.append((Pprev[i], safeGetIdx(Pprev, i + cnt), i))
	    sortedL = sorted(L, key=lambda x: (x[0], x[1]))
	    for i in range(n):
		if i > 0 and sortedL[i][0] == sortedL[i - 1][0] and sortedL[i][1] == sortedL[i - 1][1]:
		   Pprev[sortedL[i][2]] = Pprev[sortedL[i-1][2]]
		else:
		   Pprev[sortedL[i][2]] = i
	return Pprev


