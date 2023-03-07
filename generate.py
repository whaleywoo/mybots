import pyrosim.pyrosim as pyrosim
import random

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-3,3,z] , size=[length, width, height])
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    #pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length, width, height])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    for sensor_neuron in [0, 1, 2]:
        for motor_neuron in [3, 4]:
            pyrosim.Send_Synapse( sourceNeuronName = sensor_neuron , targetNeuronName = motor_neuron , weight = random.random() * 2 - 1)
    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()