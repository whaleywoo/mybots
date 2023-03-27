import numpy as numpy

amplitudeBackLeg = numpy.pi/2
frequencyBackLeg = 4
phaseOffsetBackLeg = 0

amplitudeFrontLeg = numpy.pi/4
frequencyFrontLeg = 1
phaseOffsetFrontLeg = numpy.pi/4

sim_iterations = 100

targetAnglesBackLeg = numpy.linspace(-2*numpy.pi, 2*numpy.pi, sim_iterations)
targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(frequencyBackLeg * targetAnglesBackLeg + phaseOffsetBackLeg)

targetAnglesFrontLeg = numpy.linspace(-2*numpy.pi, 2*numpy.pi, sim_iterations)
targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * targetAnglesFrontLeg + phaseOffsetFrontLeg)

numberOfGenerations = 1

populationSize = 1

numSensorNeurons = 4
numMotorNeurons = 3