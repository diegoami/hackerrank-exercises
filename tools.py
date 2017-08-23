
from itertools import cycle
inputter = None
import os


class ArrayInputter:

    def __init__(self,inputArray):
        self.inputArray = inputArray
        self.inputCycle = cycle(self.inputArray)

    def input(self):
        return next(self.inputCycle ).strip()


import linecache

class FileInputter(ArrayInputter):

    def __init__(self,inputFile):
        if (os.path.isfile(inputFile)):
            self.inputFile = inputFile
            self.inputCycle = cycle(linecache.getlines(self.inputFile))
        else:
            raise IOError("FILE NOT FOUND "+inputFile)


def initArrayInputter(inputArray):
    global inputter
    inputter = ArrayInputter(inputArray)

def initFileInputter(inputFile):
    global inputter
    inputter = FileInputter(inputFile)


def input():
    return inputter.input()