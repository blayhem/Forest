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
    x = r.randrange(0,20,1)
    y = r.randrange(0,20,1)
    elem = getCoordCont(x,y)
    if elem[0] == 'T':
        trees[elem[1]] = (x,y,'F')

def hasTreesAround(x,y):
    return isTree(x,y+1) and isTree(x,y-1) and isTree(x+1,y) and isTree(x-1,y)

def pbar(window):
    trees.insert(0,(10,10,"T"))
    for i in range(50):
    #while not trees:
        # if i%5==0:
        #     setFire()
        for tree in trees:
            x = tree[0]
            y = tree[1]
            if hasTreesAround(x,y):
                trees.remove(tree)
                # tree = [x for x in trees if x != tree]
            else:
                posNew = getRandomTree(x,y)
                while (posNew[0]<3 or posNew[1]<3):
                    posNew = getRandomTree(x,y)
                xb = posNew[0]
                yb = posNew[1]
                if not hasTreesAround(xb,yb):
                    bufferTrees.insert(0,(xb,yb,"T"))

                window.addstr(x,y, tree[2])
        #window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
        #window.addstr(11, 10, "This is test"+ str(i+1))
        for tree in bufferTrees:
            trees.insert(0,tree)
        window.refresh()
        time.sleep(0.5)

curses.wrapper(pbar)
