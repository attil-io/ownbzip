#!/usr/bin/python

def initfrequs(s):
    ret = {}
    for ch in s:
        if ch in ret:
           ret[ch] += 1
        else:
           ret[ch] = 1
    return ret

def mergefreqs(frequs):
    if len(frequs) < 2:
       return frequs
    sortE = sorted(frequs.items(), key=lambda value: value[1])
    first = sortE[0]
    second = sortE[1]
    combinedKey = first[0] + second[0]
    combinedValue = first[1] + second[1]
    removed1 = sortE.pop(0)
    removed2 = sortE.pop(0)
    added = (combinedKey, combinedValue)
    sortE.append(added)
    return dict(sortE), removed1, removed2, added


def createGraph():
    return []


def addNode(graph, node):
    if 'key' not in node.keys():
        raise Exception('key is mandatory')
    nodeKey = node['key']
    otherNode = findNode(graph, nodeKey)
    if otherNode != None:
        raise Exception('node with key', nodeKey, 'already exists: ', otherNode, 'trying to add:', node)
    graph.append(node)

def findNode(graph, key):
    for node in graph:
        if node.get('key') == key:
           return node

def getParent(graph, node):
    parentKey = node.get('parent', None)
    if parentKey != None:
       return findNode(graph, parentKey)

def getChildren(graph, node):
    nodeKey = node.get('key') 
    children = []
    for node in graph:
       if node.get('parent', None) == nodeKey:
          children.append(node)
    return children

   
def findRoot(graph):
    rootNode = None
    for node in graph:
        if node.get('parent') == None:
           if rootNode == None:
              rootNode = node
           else:
              print 'found duplicate root nodes:', rootNode, node
              raise Exception('found duplicate root nodes:', rootNode, node)
    return rootNode

def bfswalk(graph, fn):
    rootNode = findRoot(graph)
    if rootNode == None:
       print "root node not found!"
       return
    nodesToVisit = [rootNode]
    while len(nodesToVisit) > 0:
       nextNode = nodesToVisit.pop(0)
       nextNodeChildren = getChildren(graph, nextNode)
       nodesToVisit.extend(nextNodeChildren)
       for childIdx in range(len(nextNodeChildren)):
           child = nextNodeChildren[childIdx]
           fn(child, childIdx)

def isLeaf(graph, node):
    return len(getChildren(graph, node)) == 0

def findLeaves(graph):
    leaves = []
    def processNode(node, idx):
        if isLeaf(graph, node): 
           leaves.append(node)
    bfswalk(graph, processNode)
    return leaves

def walkToParent(graph, node, process):
    accum = None
    while node != None:
        accum = process(node, accum) 
        node = getParent(graph, node)
    return accum

def dumpGraph(graph):
    for node in graph:
        nodekey = node.get('key')
        nodeparent = node.get('parent', '<NONE>')
        otherprops = {}
	for key, value in node.items():
		if key not in set(['key', 'parent']):
		   otherprops[key] = value
        print "key ='" + nodekey + "'",
        print "parent ='" + nodeparent + "'",
        print "otherprops =", otherprops


def doStep(freqs, graph):
    key23 = False
    newfreqs, removed1, removed2, added = mergefreqs(freqs)
    removed1key = removed1[0]
    removed1val = removed1[1]
    removed2key = removed2[0]
    removed2val = removed2[1]
    addedkey = added[0]
    addedval = added[1]
    key23 = removed1key ==  '23' or removed2key == '23'
    addNode(graph, {'key': addedkey, 'prob': addedval})
    removed1node = findNode(graph, removed1key)
    removed2node = findNode(graph, removed2key)
    if removed1node == None:
       addNode(graph, {'key': removed1key, 'prob': removed1val, 'parent': addedkey})
    else:
       removed1node['parent'] = addedkey 
    if removed2node == None:
       addNode(graph, {'key': removed2key, 'prob': removed2val, 'parent': addedkey})
    else:
       removed2node['parent'] = addedkey 
    return newfreqs
    


def generateHuffmanMap(text):
    g = createGraph()
    frequs = initfrequs(text)
    
    while len(frequs) > 1:
       frequs = doStep(frequs, g)
    
    def labelNode(node, idx):
       node['code'] = idx
    
    bfswalk(g, labelNode)
    
    leaves = findLeaves(g)
    
    def calcCode(node, accum):
        if accum == None:
           accum = '' + str(node.get('code', ''))
        else:
           accum = str(node.get('code', '')) + accum
        return accum
    
    codes = {} 
    for l in leaves:
        code = walkToParent(g, l, calcCode)
        codes[l.get('key')] = code
    return codes, g


def huffmanEncode(text, huffmanmap):
    return ''.join(map(lambda ch: huffmanmap[ch], text))


def huffmanDecode(encodedText, huffmanmap, huffmangraph):
    rootNode = findRoot(huffmangraph)
    ret = []
    reversemap = dict((v,k) for k,v in huffmanmap.iteritems())
    def findNextCodeWord(encodedText, huffmangraph, rootNode):
        actNode = rootNode
        actCharPtr = 0
        code = ''
        while not isLeaf(huffmangraph, actNode):
              actChar = encodedText[actCharPtr]
              children = getChildren(huffmangraph, actNode)
              chosenChild = None
              for ch in children:
                  if str(ch.get('code')) == actChar:
                     chosenChild = ch
                     break
              code = code + actChar
              actNode = chosenChild
              actCharPtr += 1
        return code
    totallen = 0
    while totallen < len(encodedText):
        code = findNextCodeWord(encodedText[totallen:], huffmangraph, rootNode)
        totallen = totallen + len(code)
        ret.append(reversemap[code])
    return ret


test="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

#huffmanMap, huffmanGraph = generateHuffmanMap(test)
#encoded = huffmanEncode(test, huffmanMap)
#decoded = huffmanDecode(encoded, huffmanMap, huffmanGraph)
#print "encoded:", encoded, len(encoded) / 8, 'bytes'
#print "decoded:", decoded, len(decoded), 'bytes'
#print "huffmanMap:", huffmanMap

#g = createGraph()
#addNode(g, {'key': 'e'})
#addNode(g, {'key': 'f', 'parent': 'e', 'prob': 22})
#dumpGraph(g)
#nodef = findNode(g, 'f')
#parentf = getParent(g, nodef)
#childe = getChildren(g, parentf)
#print nodef, parentf, childe

#frequs = initfrequs('Hello, world!')
#print frequs
#frequs = mergefreqs(frequs)
#print frequs

