import numpy as numpy

amplitudeBackLeg = numpy.pi/2
frequencyBackLeg = 4
phaseOffsetBackLeg = 0

amplitudeFrontLeg = numpy.pi/4
frequencyFrontLeg = 1
phaseOffsetFrontLeg = numpy.pi/4

sim_iterations = 500

targetAnglesBackLeg = numpy.linspace(-2*numpy.pi, 2*numpy.pi, sim_iterations)
targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(frequencyBackLeg * targetAnglesBackLeg + phaseOffsetBackLeg)

targetAnglesFrontLeg = numpy.linspace(-2*numpy.pi, 2*numpy.pi, sim_iterations)
targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * targetAnglesFrontLeg + phaseOffsetFrontLeg)

numberOfGenerations = 10
populationSize = 10

numSensorNeurons = 9
numMotorNeurons = 8

motorJointRange = 0.2

gravityCorrectionFactor = 5.0