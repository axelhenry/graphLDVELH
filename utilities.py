# -*- coding: utf-8 -*-


def cyclesToString(aListOfCycles, alternativePathsNotProcessed=False):
    myVariation = 'included' if not alternativePathsNotProcessed else 'excluded'
    aString = ''.join(["%s cycles in the xml file (variations %s).\n"
                       % (len(aListOfCycles), myVariation)]) + \
        'Visual representation of these cycles' + \
        ' could be found in our png file.\n'
    for aCycle in aListOfCycles:
        aString = aString + presentCycles('Cycle : ', '>', aCycle)
    return aString


def presentCycles(aPrefix, aSeparator, aList):
    # aString = ''
    # for subList in aList:
    #     tmpString = aPrefix + ''
    #     tmpString = tmpString + \
    #         ''.join(["%s %s " % (k, aSeparator) for k in subList[0:-1]]) + \
    #         ''.join(["%s\n" % subList[-1]])
    #     aString = aString + tmpString
    return aPrefix + ''.join(["%s %s " % (k, aSeparator) for k in aList[0:-1]])\
        + ''.join(["%s\n" % aList[-1]])


def stringifyCycle(aCycle):
    return ''.join(["%s_" % k for k in aCycle])


def flattenList(aList):
    return [x for l in aList for x in l]
