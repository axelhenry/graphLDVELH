#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tarjan


class TarjanHandler:

    def __init__(self, aHash):
        self._myStrongConnectedComponents = self._findconnectedComponents(aHash)

    def _findconnectedComponents(self, aHash):
        tmpCycles = tarjan.tarjan(aHash)
        resultCycles = []
        for item in tmpCycles:
            if len(item) > 1:
                resultCycles.append(item)
        return resultCycles

    def getComponents(self):
        return self._myStrongConnectedComponents
