#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygraph.classes.digraph import digraph
from pygraph.classes.exceptions import AdditionError
from pygraph.readwrite.dot import write
import find_all_cycles
import find_alternative_paths
# import graphviz
import pydot
import utilities
import constants


class PythonGraphHandler:

    def __init__(self, aFilePath, aHash, aTarjanHash, aTarjanComponents):
        self._filePath = aFilePath
        self._myHashFromXML = aHash
        self._myTarjanHash = aTarjanHash
        self._myStrongComponents = aTarjanComponents
        self._myGraph = digraph()
        # self.myVertexFillColor = self.myGraph.new_vertex_property("string")
        # self.myVertexColor = self.myGraph.new_vertex_property("string")
        # self.myEdgeColor = self.myGraph.new_edge_property("string")
        # self.myVertexDict = self.generateVertex()
        self._generateVertex()
        self._generateEdges()
        self._myCycles = find_all_cycles.find_all_cycles(self._myGraph)
        # self.myAltCycles = find_alternative_paths.find_alternative_paths(
        #     self.myCycles, self.myTarjanHash, self.myStrongComponents)
        # self.my121Cycles = self._find121Cycle()
        self._myCycles = self._uniqueCycles([self._myCycles,
                                             find_alternative_paths.find_alternative_paths(self._myCycles,
                                                                                           self._myTarjanHash, self._myStrongComponents),
                                             self._find121Cycle()])
        self._myUniqueEdges = self._uniqueEdges(
            self._myCycles, self._myHashFromXML)
        self._highlightEdges(self._myUniqueEdges)
        # self._highlightAllCycles([
        #     self.myCycles, self.myAltCycles, self.my121Cycles])
        self._drawGraph()

    def _generateEdge(self, aKey):
        myHash = self._myHashFromXML[aKey]
        if not myHash['fucking deadly trap']:
            myOriginVertex = aKey
            for myDest in myHash['destinations']:
                myDestVertex = myDest
                try:
                    self._myGraph.add_edge((myOriginVertex, myDestVertex),
                                           attrs=[('color', constants.BLACK)])
                except(AdditionError):
                    print('edge already in graph')

    def _generateEdges(self):
        for aKey in self._myHashFromXML:
            self._generateEdge(aKey)

    def _generateVertex(self):
        for aKey in self._myHashFromXML:
            myNodeColor = constants.WHITE
            if aKey is '0':
                myNodeColor = constants.GREEN_START
            else:
                myTmpDict = self._myHashFromXML[aKey]
                if myTmpDict['fucking deadly trap'] is True:
                    myNodeColor = constants.RED_DEATH
                    # self.myVertexFillColor[
                    #     self.myGraph.vertex(myDict[aKey])] = self.DEATH
                elif myTmpDict['dangerous'] is True:
                    myNodeColor = constants.ORANGE_DANGER
                    # self.myVertexFillColor[
                    #     self.myGraph.vertex(myDict[aKey])] = self.DANGER
                elif myTmpDict['potentialEnnemies'] is True:
                    myNodeColor = constants.YELLOW_ENNEMIES
            try:
                self._myGraph.add_node(
                    aKey, attrs=[('style', 'filled'),
                                 ('fillcolor', myNodeColor)])
            except(AdditionError):
                print('node already in graph')

    # def highlightCycles(self):
    #     if self.myCycles:
    #         for aCycle in self.myCycles:
    #             myPrev = aCycle[0]
    #             try:
    #                 self.myGraph.add_edge_attributes(
    #                     (aCycle[-1], myPrev),
    #                     [('color', constants.EDGECYCLE)])
    #                 for elem in aCycle[1:]:
    #                     self.myGraph.add_edge_attributes(
    #                         (myPrev, elem), [('color', constants.EDGECYCLE)])
    #                     myPrev = elem
    #             except(AdditionError):
    #                 print('plip')

    def _highlightEdges(self, myEdges):
        if myEdges:
            for aEdge in myEdges:
                try:
                    self._myGraph.add_edge_attributes(
                        aEdge, [('color', constants.EDGECYCLE)])
                except(AdditionError):
                    print('oups')

    def _uniqueCycles(self, aCycles):
        myUniqueCycles = {}
        for cyclesList in aCycles:
            for aCycle in cyclesList:
                mySCycle = utilities.stringifyCycle(aCycle)
                if mySCycle not in myUniqueCycles:
                    myUniqueCycles[mySCycle] = aCycle
        return [k for k in myUniqueCycles.values()]

    def _uniqueEdges(self, myCycles, aHash):
        myUniqueEdges = {}
        for aCycle in myCycles:
            for elem in aCycle:
                myDests = aHash[elem]['destinations']
                if myDests:
                    for aDest in myDests:
                        if aDest in aCycle:
                            mySEdge = elem + '_' + aDest
                            if mySEdge not in myUniqueEdges:
                                myUniqueEdges[mySEdge] = (elem, aDest)
        return [k for k in myUniqueEdges.values()]

    def _highlightAllCycles(self, myCycles):
        for aCycle in myCycles:
            self._highlightCycles(aCycle)

    def _highlightCycles(self, myCycles):
        if myCycles:
            # if self.myAltCycles:
            # for aCycle in self.myCycles:
            for aCycle in myCycles:
                myTuples = self._highlightCycle(aCycle, self._myHashFromXML)
                # print('tuples : ', myTuples)
                for aTuple in myTuples:
                    try:
                        self._myGraph.add_edge_attributes(
                            aTuple, [('color', constants.EDGECYCLE)])
                    except(AdditionError):
                        print('oups')

    def _highlightCycle(self, aCycle, aHash):
        # generate all valid edges in this cycle
        myTupleCycle = []
        print('Cycle : ', aCycle)
        for elem in aCycle:
            myDests = aHash[elem]['destinations']
            # myDests = aHash[elem]
            # print('myDests : ', myDests)
            if myDests:
                for aDest in myDests:
                    if aDest in aCycle:
                        myTupleCycle.append((elem, aDest))
        print('myTuples : ', myTupleCycle)
        return myTupleCycle

    def _find121Cycle(self):
        myL = []
        myVisitedEdges = []
        myEdges = self._myGraph.edges()
        for aEdge in myEdges:
            reversedEdge = (aEdge[1], aEdge[0])
            if aEdge not in myVisitedEdges and \
                    reversedEdge not in myVisitedEdges:
                if aEdge[0] != aEdge[1]:
                    if (reversedEdge) in myEdges:
                        myL.append([aEdge[0], aEdge[1], aEdge[0]])
                        myVisitedEdges.append(aEdge)
                        myVisitedEdges.append(reversedEdge)
        # print(myL)
        return myL

    def _drawGraph(self):
        print('drawing graph, could take some time...')
        dot = write(self._myGraph)
        # print('dot : ', dot)
        dot = dot.replace('}', self._generateLegend() + '}')
        # dot = dot.replace('digraph graphname {','digraph graphname {'+self._generateLegend2())
        # print('processed dot : ', dot)
        graph = pydot.graph_from_dot_data(dot)
        # print('graph : ', graph.to_string())
        # graph.write_png(self._filePath)
        # graph.to_string().replace('digraph graphname {', 'digraph graphname {'+self._generateLegend())
        # print('graph : ', graph.to_string())
        graph.write_svg(self._filePath)
        print('ending drawing')
        # gvv = graphviz.readstring(dot)
        # graphviz.layout(gvv, 'dot')
        # graphviz.render(gvv, 'png', self.filePath)

    def getCycles(self):
        return self._myCycles

    def _generateLegend(self):
        myLegend = """
            node[shape=box,margin="0,0",width=1, height=0.5];
            //edge [style=invis];

            Legend[width=2];
            subgraph cluster{{
            Start[group=g1,label="", shape=oval, style=filled, color="{0}",fillcolor="{1}"];
            Ennemies[group=g1,label="", shape=oval, style=filled, color="{0}",fillcolor="{2}"];
            Danger[group=g1,label="", shape=oval, style=filled, color="{0}",fillcolor="{3}"];
            Death[group=g1,label="", shape=oval, style=filled, color="{0}",fillcolor="{4}"];

            subgraph cluster_01 {{
            style=invis
            InvisNode[label="", shape=point, style=invis]
            //Edgecycle[group=g1,label="", shape=none, color="{4}"];
            Edgecycle[label="", shape=point, style=invis, color="{5}"];
            }}
            subgraph cluster_02{{
            style=invis
            StartDescription[color=white,label="\lthe start of our book"];
            EnnemiesDescription[color=white,label="\lpotential ennemies encounter"];
            DangerDescription[color=white,label="\lrisk of dying here"];
            DeathDescription[color=white,label="\lonly death awaits here, sorry"];
            EdgecycleDescription[color=white,label="\lnode is in a cycle "];
            }}
            }}

            Legend -> Start[style=invis];
            Legend -> StartDescription[style=invis];
            Start -> Ennemies[style=invis];
            StartDescription -> EnnemiesDescription[style=invis];
            Ennemies -> Danger[style=invis];
            EnnemiesDescription -> DangerDescription[style=invis];
            Danger -> Death[style=invis];
            DangerDescription -> DeathDescription[style=invis];
            //Death -> Edgecycle[style=invis];
            Death -> InvisNode[style=invis];
            DeathDescription -> EdgecycleDescription[style=invis];

            //Legend -> Foo;
            //Legend -> FooValue;
            //Foo -> Bar;
            //FooValue[label="", shape=oval, style=filled, color="{0}"];
            //FooValue -> BarValue;
            //Bar -> Baz;
            //BarValue -> BazValue;

            edge [constraint=false];
            //Foo -> FooValue;
            //Bar -> BarValue
            //Baz -> BazValue;
            Start -> StartDescription[style=invis];
            Ennemies -> EnnemiesDescription[style=invis];
            Danger -> DangerDescription[style=invis];
            Death -> DeathDescription[style=invis];
            Edgecycle -> InvisNode[shape=normal, color="{5}"];
            //InvisNode-> EdgecycleDescription[shape=normal, color="{4}"];
            InvisNode-> EdgecycleDescription[style=invis];
            """
        return myLegend.format(constants.BLACK,
                               constants.GREEN_START,
                               constants.YELLOW_ENNEMIES,
                               constants.ORANGE_DANGER,
                               constants.RED_DEATH,
                               constants.EDGECYCLE)
