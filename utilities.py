# -*- coding: utf-8 -*-


def presentCycles(aList):
    aString = ''
    for subList in aList:
        tmpString = 'Cycle : '
        tmpString = tmpString + \
            ''.join(["%s > " % k for k in subList[0:-1]]) + \
            ''.join(["%s\n" % subList[-1]])
        aString = aString + tmpString
    return aString


def isVertexInCycles(aKey, aList):
    myList = [aKey in k for k in aList]
    return isTrueInMyList(myList)


def isEdgeInCycles(aStart, aEnd, aList):
    myList = [aStart in k and aEnd in k for k in aList]
    return isTrueInMyList(myList)


def isTrueInMyList(aList):
    if True in aList:
        return True
    else:
        return False
