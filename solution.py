import numpy

class SOLUTION:
    def __init__(self):
        self.weights = numpy.matrix([[numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()]])
        self.weights = self.weights * 2 - 1
        exit()