#!/usr/bin/env python

import sys
import os
import subprocess

class PeaceNegotiator :

    def __init__(self, scriptType) :
        if str.lower(scriptType) == "firmtool" :
            self.scriptType = "firmtool"
        elif str.lower(scriptType) == "cratemon" :
            self.scriptType = "cratemon"
        else :
            self.scriptType = scriptType
        #print self.scriptType
        self.filepath = '/home/xtaldaq/PeaceNegotiator/.negotiations.txt'

    def checkFile(self):
        try :
            with open(self.filepath, 'r') as f:
                #print "file exists"
                if f.readline() == '':
                    f.close()
                    with open(self.filepath, 'w') as f:
                        f.write('Done!')
        except :
            with open(self.filepath, 'w') as f:
                f.write('Done!')

    def requestAccess(self):
        self.checkFile()
        with open(self.filepath, 'r') as f:
            if f.readline() == 'Done!' or (f.readline() == 'Go ahead' and self.scriptType == 'firmtool')  :
                return True
            else :
                if self.scriptType == 'firmtool' :
                    f.close()
                    with open(self.filepath, 'w') as f:
                        f.write('Firmtool in line!')
                return False

    def done(self):
        with open(self.filepath, 'w') as f:
                f.write('Done!')

    def firmtoolInLine(self):
        self.checkFile()
        with open(self.filepath, 'r') as f:
            if f.readline() == 'Firmtool in line!':
                return True
            else:
                return False

    def IAmWorking(self):
        if self.scriptType == 'cratemon':
            with open(self.filepath, 'w') as f:
                f.write('cratemon working...')
        else :
            with open(self.filepath, 'w') as f:
                f.write('firmtool working...')

    def getLine(self):
        self.checkFile()
        with open(self.filepath, 'r') as f:
            line = f.readline()
            print(line)
        return line

    def writeToFile(self, string):
        with open(self.filepath, 'w') as f:
            f.write(string)

if __name__ == '__main__' :
    PeaceNegotiator('test').done()
    firmNegotiator = PeaceNegotiator('FIRMtool')
    monNegotiator = PeaceNegotiator('crateMon')
    print(monNegotiator.requestAccess())
