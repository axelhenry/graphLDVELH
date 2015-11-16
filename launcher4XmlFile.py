#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import XmlHandler
# import GraphToolHandler
# import GraphNetworkXHandler
# import IGraphHandler
import PythonGraphHandler
import TarjanHandler
# import CyclesHandler
import utilities

parser = argparse.ArgumentParser(
    description='Generate a graph from a xml file and look for cycle')
parser.add_argument(
    '--xml_file', '-f',
    help='path to our input file', required=True)
parser.add_argument(
    '--output_cycle_file', '-ocf',
    help='path to our summary of cycles in graph', required=True)
parser.add_argument(
    '--output_graph_file', '-ogf',
    help='path to our representation of the graph, in a svg file',
    required=True)
parser.add_argument('--disable_alternate_paths', '-dap', action='store_true')
args = parser.parse_args()

if args.xml_file:
    myXmlFile = args.xml_file
if args.output_graph_file:
    myOutputFile = args.output_graph_file
if args.output_cycle_file:
    myCycleFile = args.output_cycle_file


myXmlHandler = XmlHandler.XmlHandler(myXmlFile)

myWorkingHash = myXmlHandler.getTarjanizedHash()
myTarjanHandler = TarjanHandler.TarjanHandler(myWorkingHash)
myTarjanHandler.writeComponents(myCycleFile)
myPGHHandler = PythonGraphHandler.PythonGraphHandler(
    myOutputFile,
    myXmlHandler.getProcessedHash(),
    myWorkingHash,
    myTarjanHandler.getComponents())
# myCyclesList = myTarjanHandler.getCycles()
# myCyclesHandler = CyclesHandler.CyclesHandler(myCyclesList, myWorkingHash)
# mySortedCyclesList = utilities.sortCycles(myCyclesList, myWorkingHash)
# print(utilities.presentCycles(myCyclesList))
# myStringToWrite = utilities.cyclesToString(myCyclesHandler.myPaths)

# myStringToWrite = utilities.cyclesToString(
#     myPGHHandler.getCycles(), args.disable_alternate_paths)
# print(myStringToWrite)
# try:
#     with open(myCycleFile, 'w') as myFile:
#         myFile.write(myStringToWrite)
# except (OSError, IOError):
#     print('something went wrong with the cycle file')

# if args.output_file:
#     import GraphToolHandler

#     myOutputFile = args.output_file
#     myGraphToolHandler = GraphToolHandler.GraphToolHandler(
#         myOutputFile, myXmlHandler.getProcessedHash(), myCyclesList)
# myNetworkXHandler = GraphNetworkXHandler.GraphNetworkXHandler(
#     myOutputFile, myXmlHandler.getProcessedHash())

# myIGraphHandler = IGraphHandler.IGraphHandler(
#     myOutputFile, myXmlHandler.getProcessedHash())
