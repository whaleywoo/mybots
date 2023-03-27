from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parents = {}

        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)

        self.Print()

        self.Select()
        pass

    def Print(self):
        print("")
        for key in self.parents:
            print("Parent fitness: " + str(self.parents[key].fitness) + ", Child fitness: " + str(self.children[key].fitness))
        print("")
    
    def Show_Best(self):
        best_parent = self.parents[0]
        for parent in self.parents:
            if self.parents[parent].fitness < best_parent.fitness:
                best_parent = self.parents[parent]
        print("Best fitness: " + str(best_parent.fitness))
        best_parent.Start_Simulation("GUI")


    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()