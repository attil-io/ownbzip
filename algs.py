#!/usr/bin/python

from huffman import *

def rotate(instr, steps=0):
    ret = "";
    steps = steps % len(instr);
    for i in range(0, steps):
        ret += instr[len(instr) - steps + i];
    ret += instr[:len(instr) - steps];
    return ret;


def safeIndex(somelist, needle):
    if needle in somelist:
       return somelist.index(needle)
    else:
       return None

def compressPrepare(instr):
    M=[];
    for i in range(len(instr)):
        M.append(rotate(instr, i));
    M.sort();
    return M,safeIndex(M,instr);


def getL(M):
    return [m[-1] for m in M];


def getF(L):
    F = L[:];
    F.sort();
    return F;


def findNth(lst, val, n):
    sumidx = -1;
    while n >= 0:
      idx = lst.index(val)
      sumidx = idx + sumidx + 1;
      lst = lst[idx + 1:];
      n = n - 1;
    return sumidx;


def getT(F, L):
  nthdict = {}
  T = []
  for l in L:
    if not l in nthdict:
      nthdict[l] = -1
    nextidx = nthdict[l] + 1
    nthdict[l] = nextidx
    idx = findNth(F, l, nextidx)
    T.append(idx)
  return T;


def getnthT(T, n, x):
  if n <= 0:
    return x;
  return T[getnthT(T, n-1, x)]


def getS(L, T, I):
  S = []
  for i in range(len(L)):
    nthT = getnthT(T, i, I)
    S.append(L[nthT])
  S.reverse()
  return S;

def XXXtestComp(instr):
    M,I = compressPrepare(instr);
    # print M, I
    L = getL(M);
    # print L;
    return L, I;


def testDecomp(L, I):
    F = getF(L);
    # print F;
    T = getT(F, L)
    # print T;
    S = getS(L, T, I);
    return S;


def testCompDecomp(instr):
    print "INPUT: '" + instr + "'"
    L, I = testComp(instr);
    print "L: '", L, "'"
    print "I: '", I, "'"
    S = "".join(testDecomp(L, I));
    print "OUTPUT: '" + S + "'"


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def getY(L):
   return sorted(list(set(L)))

def moveToFront(vec, nth):
    popped = vec.pop(nth)
    vec.insert(0, popped)

def getR(L):
    Y = getY(L)
    R = []
    for l in L:
       newR = Y.index(l)
       R.append(newR)
       moveToFront(Y, newR)
    return R,Y

def getLfromR(R,Y):
    L = []
    for r in R:
       numR = ord(r)
       newL = Y[numR]
       L.append(newL)
       moveToFront(Y, numR)
    return L
        
#-----------------------------------

#L,I = testComp(test)
#R1,Y=getR(L)
#R=(map(chr, R1))
#print 'R=',R
#huffmanMap, huffmanGraph = generateHuffmanMap(R)
#encoded = huffmanEncode(R, huffmanMap)
#print 'encoded:', encoded, len(encoded)/8, 'bytes'
#-----------------------------------

#decoded = huffmanDecode(encoded, huffmanMap, huffmanGraph)
#print 'xxx R`=', decoded
#L=getLfromR(R, sorted(Y))
#decoded=testDecomp(L, I)
#print 'decoded:', ''.join(decoded), len(decoded), 'bytes'


#--------------------------------------------------
EOF=chr(4)

def extendString(instr):
    return instr + EOF

def formArrayOfWords(Sap):
    return [Sap[ind:ind+1] for ind in range(len(Sap)) ] 

def formArrayOfSuffixes(Sap):
    return [ind for ind in range(len(Sap)) ] 

def sortArrayOfSuffixes(Sap, V):
    def compare(idx1, idx2):
        s1 = Sap[idx1:] + Sap[:idx1]
        s2 = Sap[idx2:] + Sap[:idx2]
        if (s1==s2):
           return 0
        elif s1 < s2:
           return -1
        else:
           return 1 
    return sorted(V, compare)

def getIandL(Sap, Vsorted):
    return safeIndex(Vsorted,0),[Sap[(len(Sap) + v-1) % len(Sap)] for v in Vsorted]

def testComp(S): 
    Sap = extendString(S)
    V = formArrayOfSuffixes(S)
    Vsorted =  sortArrayOfSuffixes(S, V)
    I,L = getIandL(S, Vsorted)
    return L,I

