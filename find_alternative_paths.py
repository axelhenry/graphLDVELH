# -*- coding: utf-8 -*-
import treelib
import uuid
import utilities


def find_alternative_paths(myOriginalCycles, myHash, myStrongComponents):
    print('---- finding alternative paths -----')
    myCycles = {}
    for myCycle in myOriginalCycles:
        # build a tree !
        aTree = buildTree(
            myCycle, myHash, findStrongComponentContainingCycle(myCycle, myStrongComponents))
        myLstElem = myCycle[-1]
        myPaths = find_paths(aTree, myLstElem)
        # myCycles.append(myCycle)
        myCycles[utilities.stringifyCycle(myCycle)] = myCycle
        for aPath in myPaths:
            myCycles[utilities.stringifyCycle(aPath)] = aPath
            # myCycles.append(aPath)
        # print('paths :\n', myPaths)
        showTree(aTree, True)
    print('---- ending alternative paths -----')
    return [k for k in myCycles.values()]


def buildTree(aCycle, aHash, aStrongComponent):
    print('building tree :')
    print(aCycle)
    myVisitedNodes = []
    # myVisitedNodes = {}
    myTree = treelib.Tree()
    # conditions to stop building tree :
    # 1 - ancestor = descendant, ie 1->2->1
    # 2 - 1 visit by node for 1 path, if descedant already in processed list,
    # don't do anything
    # 3 - if node = start
    myFstElt = aCycle[0]
    myFstNode = myTree.create_node(myFstElt, getRandomId())
    if aStrongComponent:
        myVisitedNodes.append(myFstElt)
        # myVisitedNodes[myFstElt] = 1
        # maxDepth = len(aCycle) * 1.5 + 1
        # print('maxDepth : ', maxDepth)
        generateLeaves(
            myTree, myFstNode, aHash, aCycle, myVisitedNodes, aStrongComponent)
    return myTree


# def generateLeaves(aTree, aParent, myHash, myCycle, visitedNodes,
# aPrecedentPathLength, maxDepth):
def generateLeaves(aTree, aParent, myHash, myCycle, visitedNodes, aStrongComponent):
    myParentNode = aTree.get_node(aParent.identifier)
    # print('parentNode: ', myParentNode.tag)
    # if myParentNode.tag in myHash:
    for elem in myHash[myParentNode.tag]:
        # print('elem : ', elem)
        # print('visited : ', visitedNodes)
        # if elem not in visitedNodes and elem in aStrongComponent:
        if elem not in visitedNodes and elem in aStrongComponent:
            myVisited = list(visitedNodes)
            myVisited.append(elem)
            myNewNode = aTree.create_node(
                elem, getRandomId(), parent=myParentNode.identifier)
            # print('creatingNode : ',
            #       myNewNode.tag, 'son of ', myParentNode.tag)
            # myCurrentPathLength, myDist = getPathLengthFromNodeToRoot(
            #     aTree, myCycle, myNewNode)
            # print('current path length : ', myCurrentPathLength,
            #       'tree depth : ', aTree.depth(),
            #       'dist to our closest cycle member : ', myDist)
            if len(myVisited) < len(aStrongComponent):
                # if myDist < 5 and myCurrentPathLength > aPrecedentPathLength and
                # aTree.depth() < maxDepth:
                generateLeaves(
                    aTree, myNewNode, myHash, myCycle, myVisited, aStrongComponent)


def getRandomId():
    return uuid.uuid4()


def decodePath(myTree, myPath):
    myDecodedPath = []
    for elem in myPath:
        myNode = myTree.get_node(elem)
        myDecodedPath.append(myNode.tag)
    return myDecodedPath


def showTree(myTree, showId):
    myTree.show(idhidden=showId,line_type='ascii')


def find_paths(aTree, aElem):
    # print('elem : ', aElem)
    myPaths = aTree.paths_to_leaves()
    myValidPaths = []
    # print('paths :\n', myPaths)
    for aPath in myPaths:
        # decoded = decodePath(aTree, aPath)
        # print('decoded : ', decoded)
        myLstNode = aTree.get_node(aPath[-1])
        # print('decoded[-1] : ', decoded[-1], ', aElem : ', aElem)
        if myLstNode.tag == aElem:
            myValidPaths.append(decodePath(aTree, aPath))
    return myValidPaths


def findStrongComponentContainingCycle(aCycle, myStrongComponents):
    for aStrongComponent in myStrongComponents:
        print('aCycle : ', aCycle)
        print('aStrongComponent : ', aStrongComponent)
        myCycleInComponent = False
        for elem in aCycle:
            if elem in aStrongComponent:
                myCycleInComponent = True
            else:
                myCycleInComponent = False
                break
        if myCycleInComponent:
            return aStrongComponent
        # if aCycle in aStrongComponent:
        #     return aStrongComponent
