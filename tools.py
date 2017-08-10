
from itertools import cycle
inputter = None
class ArrayInputter:

    def __init__(self,inputArray):
        self.inputArray = inputArray
        self.inputCycle = cycle(self.inputArray)

    def input(self):
        return next(self.inputCycle )


def initArrayInputter(inputArray):
    global inputter
    inputter = ArrayInputter(inputArray)

def input():
    return inputter.input()