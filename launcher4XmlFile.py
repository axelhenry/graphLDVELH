#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import XmlHandler
import GraphToolHandler
# import GraphNetworkXHandler
# import IGraphHandler
import TarjanHandler
import utilities

parser = argparse.ArgumentParser(
    description='Generate a graph from a xml file and look for cycle')
parser.add_argument(
    '--xml_file', '-f',
    help='path to our input file', required=True)
parser.add_argument(
    '--output_file', '-of',
    help='path to our graph', required=True)
parser.add_argument(
    '--cycle_file', '-cf',
    help='path to our summary of cycles in graph', required=True)
args = parser.parse_args()

if args.xml_file:
    myXmlFile = args.xml_file
if args.output_file:
    myOutputFile = args.output_file
if args.cycle_file:
    myCycleFile = args.cycle_file


myXmlHandler = XmlHandler.XmlHandler(myXmlFile)


myTarjanHandler = TarjanHandler.TarjanHandler(myXmlHandler.getTarjanizedHash())
myCyclesList = myTarjanHandler.getCycles()
# print(utilities.presentCycles(myCyclesList))

myGraphToolHandler = GraphToolHandler.GraphToolHandler(
    myOutputFile, myXmlHandler.getProcessedHash(), myCyclesList)
# myNetworkXHandler = GraphNetworkXHandler.GraphNetworkXHandler(
#     myOutputFile, myXmlHandler.getProcessedHash())

# myIGraphHandler = IGraphHandler.IGraphHandler(
#     myOutputFile, myXmlHandler.getProcessedHash())
try:
    with open(myCycleFile, 'w') as myFile:
        myFile.write(utilities.presentCycles(myCyclesList))
except (OSError, IOError):
    print('something went wrong with the cycle file')
