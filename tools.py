
from itertools import cycle
inputter = None



class ArrayInputter:

    def __init__(self,inputArray):
        self.inputArray = inputArray
        self.inputCycle = cycle(self.inputArray)

    def input(self):
        return next(self.inputCycle )


import linecache

class FileInputter(ArrayInputter):

    def __init__(self,inputFile):
        self.inputFile = inputFile
        self.inputCycle = cycle(linecache.getlines(self.inputFile))



def initArrayInputter(inputArray):
    global inputter
    inputter = ArrayInputter(inputArray)

def initFileInputter(inputFile):
    global inputter
    inputter = FileInputter(inputFile)


def input():
    return inputter.input()