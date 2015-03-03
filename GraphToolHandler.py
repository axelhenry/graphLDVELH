#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graph_tool.all import *
import utilities
import constants


class GraphToolHandler:

    def __init__(self, aFilePath, aHash, aListOfCycles):
        self.filePath = aFilePath
        self.myHashFromXML = aHash
        self.myCycles = aListOfCycles
        self.myGraph = Graph()
        self.myVertexFillColor = self.myGraph.new_vertex_property("string")
        self.myVertexColor = self.myGraph.new_vertex_property("string")
        # self.myEdgeColor = self.myGraph.new_edge_property("string")
        self.myVertexDict = self.generateVertex()
        self.generateEdges()
        self.drawGraph()

    def generateEdge(self, aKey):
        myHash = self.myHashFromXML[aKey]
        if not myHash['fucking deadly trap']:
            myOriginVertex = self.myVertexDict[aKey]
            for myDest in myHash['destinations']:
                myDestVertex = self.myVertexDict[myDest]
                self.myGraph.add_edge(myOriginVertex, myDestVertex)
                # myUsedColor = self.GREY
                # if utilities.isEdgeInCycles(aKey,aDest,self.myCycles):

                # self.myEdgeColor[self.myGrap]

    def generateEdges(self):
        for aKey in self.myHashFromXML:
            self.generateEdge(aKey)

    def generateVertex(self):
        myDict = {}
        for aKey in self.myHashFromXML:
            myDict[aKey] = self.myGraph.add_vertex()
            myFillColor = constants.OTHER
            myOuterColor = constants.GREY
            if aKey is '0':
                myFillColor = constants.START
                # self.myVertexFillColor[
                #     self.myGraph.vertex(myDict[aKey])] = self.START
            else:
                myTmpDict = self.myHashFromXML[aKey]
                if myTmpDict['fucking deadly trap'] is True:
                    myFillColor = constants.DEATH
                    # self.myVertexFillColor[
                    #     self.myGraph.vertex(myDict[aKey])] = self.DEATH
                elif myTmpDict['dangerous'] is True:
                    myFillColor = constants.DANGER
                    # self.myVertexFillColor[
                    #     self.myGraph.vertex(myDict[aKey])] = self.DANGER
                elif myTmpDict['potentialEnnemies'] is True:
                    myFillColor = constants.ENNEMIES
                    # self.myVertexFillColor[
                    #     self.myGraph.vertex(myDict[aKey])] = self.ENNEMIES
                else:
                    myFillColor = constants.OTHER
                    # self.myVertexFillColor[
                    #     self.myGraph.vertex(myDict[aKey])] = self.OTHER
            if utilities.isVertexInCycles(aKey, self.myCycles):
                myOuterColor = constants.OUTERCYCLE
            self.myVertexFillColor[
                self.myGraph.vertex(myDict[aKey])] = myFillColor
            self.myVertexColor[
                self.myGraph.vertex(myDict[aKey])] = myOuterColor
        return myDict

    def drawGraph(self):
        # graph_draw(self.myGraph, vertex_fill_color=self.myVertexFillColor)
        graph_draw(self.myGraph,
                   vertex_color=self.myVertexColor,
                   vertex_fill_color=self.myVertexFillColor,
                   output=self.filePath)
