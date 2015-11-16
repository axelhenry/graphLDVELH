#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import bs4 as BeautifulSoup


class XmlHandler:

    def __init__(self, aFilePath):
        self._myHash = {}
        self._myTarjanHash = {}
        if os.path.isfile(aFilePath):
            self._mySoup = BeautifulSoup.BeautifulSoup(open(aFilePath), 'xml')
            myParagraphes = self.getParagraphsFromXml()
            self.processParagraphs(myParagraphes)

    def getParagraphsFromXml(self):
        return self._mySoup.find_all('paragraphe')

    def processParagraph(self, aParagraphe):
        myNumber = aParagraphe['numero']
        myList = []
        isDangerous = False
        isDeadlyTrap = False
        isPotentialEnnemies = False
        if not aParagraphe.find('mort'):
            myActions = aParagraphe.find_all('action')
            for anAction in myActions:
                if anAction.getText() == 'mort':
                    # print('ça pue la merde par là')
                    isDangerous = True

            myEnnemies = aParagraphe.find_all('adversaire')
            if myEnnemies:
                isPotentialEnnemies = True
        else:
            isDeadlyTrap = True
        # common processing
        myDestinations = aParagraphe.find_all('destination')
        for aDest in myDestinations:
            # print(aDest)
            # print(
            #     'aParagraphe : ' + myNumber
            #     + ', aDest : ', aDest.getText())
            myList.append(aDest.getText())
        return {myNumber: {'destinations': myList,
                           'dangerous': isDangerous,
                           'potentialEnnemies': isPotentialEnnemies,
                           'fucking deadly trap': isDeadlyTrap}}

    def processParagraphs(self, someParagraphes):
        for aParagraphe in someParagraphes:
            tmpHash = self.processParagraph(aParagraphe)
            for key, value in tmpHash.items():
                self._myHash[key] = value
                myDests = list(value['destinations'])
                # remove self loops
                if key in myDests:
                    myDests.remove(key)
                self._myTarjanHash[key] = myDests

    def getProcessedHash(self):
        return self._myHash

    def getTarjanizedHash(self):
        return self._myTarjanHash
