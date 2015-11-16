#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tarjan
import json


class TarjanHandler:

    def __init__(self, aHash):
        self._myStrongConnectedComponents = self._findConnectedComponents(
            aHash)

    def _findConnectedComponents(self, aHash):
        resultCycles = []
        for item in tarjan.tarjan(aHash):
            # remove self cycle
            if len(item) > 1:
                resultCycles.append(item)
        return resultCycles

    def getComponents(self):
        return self._myStrongConnectedComponents

    def writeComponents(self, path):
        try:
            with open(path, mode='w', encoding='utf-8') as myFile:
                myFile.write(json.dumps(
                    [{'Component': e}
                        for e in self._myStrongConnectedComponents],
                    indent=4, ensure_ascii=False))
        except(OSError, IOError):
            print('something went wrong with the json file')
