#!/usr/bin/env python

import sys
import subprocess

class PeaceNegotiator :

    def __init__(self, scriptType, rack, crate) :
        if str.lower(scriptType) == "firmtool" :
            self.scriptType = "firmtool"
        elif str.lower(scriptType) == "cratemon" :
            self.scriptType = "cratemon"
        else :
            self.scriptType = scriptType
            print "Script type not supported, hope you know what you're doing"
        #print self.scriptType
        self.rack = rack
        self.crate = crate
        self.filepath = '/home/xtaldaq/PeaceNegotiator/.negotiations_{0}-{1}.txt'.format(self.rack, self.crate)

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
            line = f.readline()
            if line == 'Done!' or (line == 'Go ahead' and self.scriptType == 'firmtool')  :
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
                f.write('Cratemon working...')
        else :
            with open(self.filepath, 'w') as f:
                f.write('Firmtool working...')

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
    firm.PeaceNegotiator('firmtool')
    print(firm.getLine())
