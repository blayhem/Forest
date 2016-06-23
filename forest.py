# coding=UTF-8
import time
import curses
import random as r

trees = []
bufferTrees = []
    
def getRandomTree(x,y):
    pos = r.randrange(0,8,1)
    possibleTrees = [(x,y+1),(x,y-1),(x+1,y),(x-1,y),(x,y+2),(x,y-2),(x+2,y),(x-2,y)]
    return possibleTrees[pos]

def getCoordCont(x,y):
    i = 0
    for tree in trees:
        if (tree[0] == x) and (tree[1] == y):
            return (tree[2], i)
        else: i+=1
    return (0,0)

def isTree(x,y):
    return getCoordCont(x,y)[0] == 'T'

def setFire():
    x = r.randrange(3,13,1)
    y = r.randrange(3,23,1)
    elem = getCoordCont(x,y)
    if elem[0] == 'T':
        trees[elem[1]] = (x,y,'F')
    #     return (x,y)
    # else:
    #     return (0,0)

def hasTreesAround(x,y):
    return isTree(x,y+1) and isTree(x,y-1) and isTree(x+1,y) and isTree(x-1,y)

def pbar(window):
    trees.insert(0,(8,8,"T"))
    for i in range(50):
    #while not trees:
        if i%5==0:
             setFire()
        for tree in trees:
            x = tree[0]
            y = tree[1]
            if hasTreesAround(x,y) and getCoordCont(x,y)[0]!='F':
                trees.remove(tree)
                window.addstr(x,y, " ")
                # tree = [x for x in trees if x != tree]
            else:
                posNew = getRandomTree(x,y)
                while (posNew[0]<3 or posNew[1]<3 or posNew[0]>13 or posNew[1]>23):
                    posNew = getRandomTree(x,y)
                (xb,yb) = posNew
                if not hasTreesAround(xb,yb) and getCoordCont(xb,yb)[0]!='F':
                    bufferTrees.insert(0,(xb,yb,"T"))

                window.addstr(x,y, tree[2])
        #window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
        #window.addstr(11, 10, "This is test"+ str(i+1))
        for tree in bufferTrees:
            trees.insert(len(trees),tree)
        window.refresh()
        if i<10: time.sleep(0.1)

curses.wrapper(pbar)
