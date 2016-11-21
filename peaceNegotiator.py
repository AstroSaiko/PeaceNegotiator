#!/usr/bin/env python

import sys
import subprocess

class PeaceNegotiator :
    
    'A class to make the crate monitoring script and firmware tool scripts \
    talk to each other and avoid them accessing a FEDs mmc at the same time \
    The instantiated object can be of either firmtool type or cratemon type'
   
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
        # Checks if the negotiations file exists or if it's empty
        # If it doesn't exist or is empty it will write it with "Done!"
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
        # Used by both firmtool and cratemon to request access to the FED.
        # If the file says "Done!" or "Go ahead!" and the object type is firmtool
        # the function returns True and the script can continue.
        self.checkFile() # But first, check if the file is there.
        with open(self.filepath, 'r') as f:
            line = f.readline()
            if line == 'Done!' or (line == 'Go ahead' and self.scriptType == 'firmtool') :
                return True
            else :
                if self.scriptType == 'firmtool' :
                    f.close()
                    with open(self.filepath, 'w') as f:
                        f.write('Firmtool in line!')
                return False

    def done(self): 
        # Used by both types to write "Done!" to the negotiations
        # file when they have finished their mmc work
        with open(self.filepath, 'w') as f:
                f.write('Done!')

    def firmtoolInLine(self):
        # Used by firmware tool scripts to tell the crate monitoring
        # that it wants to access the FED and is now waiting.
        self.checkFile()
        with open(self.filepath, 'r') as f:
            if f.readline() == 'Firmtool in line!':
                return True
            else:
                return False

    def IAmWorking(self):
        # Used by both types to indicate that they are using the mmc
        if self.scriptType == 'cratemon':
            with open(self.filepath, 'w') as f:
                f.write('Cratemon working...')
        else :
            with open(self.filepath, 'w') as f:
                f.write('Firmtool working...')

    def getLine(self):
        # Read the negotiations file
        self.checkFile()
        with open(self.filepath, 'r') as f:
            line = f.readline()
            #print(line)
        return line

    def writeToFile(self, string):
        # write string to negotiatons file
        with open(self.filepath, 'w') as f:
            f.write(string)

    def giveWay(self):
        # Used by the crate monitoring to indicate that it has seen
        # the "Firmtool in line" message and is now terminating to
        # let the firmware tool work.
        with open(self.filepath, 'w') as f:
            f.write('Go ahead')

if __name__ == '__main__' :
    firm = PeaceNegotiator('firmtool', 's1g04', '27')
    print(firm.getLine())
