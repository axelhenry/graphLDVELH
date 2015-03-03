#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tarjan


class TarjanHandler:

    def __init__(self, aHash):
        self.myCycles = self.findOnlyCycles(aHash)

    def findOnlyCycles(self, aHash):
        tmpCycles = tarjan.tarjan(aHash)
        resultCycles = []
        for item in tmpCycles:
            if len(item) > 1:
                resultCycles.append(item)
        return resultCycles

    def getCycles(self):
        return self.myCycles
