#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import bs4 as BeautifulSoup


class XmlHandler:

    def __init__(self, aFilePath):
        self.myXmlTree = None
        self.myHash = {}
        self.myTarjanHash = {}
        if os.path.isfile(aFilePath):
            self.mySoup = BeautifulSoup.BeautifulSoup(open(aFilePath))
            # self.myXmlTree = parse(aFilePath)
            myParagraphes = self.getParagraphsFromXml()
            self.processParagraphs(myParagraphes)

    def getParagraphsFromXml(self):
        # return
        # self.myXmlTree.documentElement.getElementsByTagName('paragraphe')
        return self.mySoup.find_all('paragraphe')

    def processParagraph(self, aParagraphe):
        myNumber = aParagraphe['numero']
        # print('Paragraphe #' + myNumber)
        myList = []
        isDangerous = False
        isDeadlyTrap = False
        isPotentialEnnemies = False
        if not aParagraphe.find('mort'):
            myDestinations = aParagraphe.find_all('destination')
            for aDest in myDestinations:
                # print(aDest)
                # print(
                #     'aParagraphe : ' + myNumber
                #     + ', aDest : ', aDest.getText())
                myList.append(aDest.getText())

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
        return {myNumber: {'destinations': myList,
                           'dangerous': isDangerous,
                           'potentialEnnemies': isPotentialEnnemies,
                           'fucking deadly trap': isDeadlyTrap}}

    def processParagraphs(self, someParagraphes):
        for aParagraphe in someParagraphes:
            tmpHash = self.processParagraph(aParagraphe)
            for key, value in tmpHash.items():
                self.myHash[key] = value
                self.myTarjanHash[key] = value['destinations']

    def getProcessedHash(self):
        return self.myHash

    def getTarjanizedHash(self):
        return self.myTarjanHash
