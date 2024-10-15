from sys import maxsize
import matplotlib.pyplot as plt
from math import sqrt
from itertools import combinations


class Graph():
        def __init__(self, M):
                self.AdjM = M
                self.sizeV = len(M) 
                
        def tspBF(self):
                """ Version naïve du TSP Dynamique:
                Plus lent mais utilise peu d'espace mémoire"""
                W = [j for j in range(1,self.sizeV)]
                return self.shortestSubPath(0, W)

        def shortestSubPath(self, i, W):
                """Entrées: sommet i et sous-ensemble W des indices des sommets (différent de 0 et i)
                Retourne la longueur du plus court chemin allant de i jusque 0 en passant
                par chaque sommet de W exactement une fois"""
                
                if W == []: return self.AdjM[0][i]
                shortestCand = maxsize
                for j in W:
                        WWithNoj = [k for k in W if k!=j]
                        d = self.shortestSubPath(j, WWithNoj)
                        if self.AdjM[i][j] + d < shortestCand:
                                shortestCand = self.AdjM[i][j] + d  
                return shortestCand   

        def tspHK(self):
                """ Version mémoïsée du TSP Dynamique pas Held-Karp"""
                n = self.sizeV
                print("Chargement: |"+(n-2)*' ' +'|')
                print(13*' ', end='')
                shortestLengths = {}
                shortestOrders = {}
                setVWithNo_0 = [i for i in range(1,n)]
                # Initialize shortest path from 0 to i for all i!=0
                for i in setVWithNo_0:
                        shortestLengths[((), i)] = self.AdjM[0][i]
                        shortestOrders[((), i)] = (0, i)
                # Loop on the sizes of the subsets
                for s in range(2,n): 
                        print("-", end='')
                        for subV in combinations(tuple(setVWithNo_0),s): # Loop on the subsets of size s, use tuples as key in dictionnary
                                for i in subV: # For all new ending vertex i, ...
                                        subVWithNo_i = tuple([j for j in subV if j!=i])
                                        shortestLengths[(subVWithNo_i,i)] = maxsize
                                        for j in subVWithNo_i: # We add the opt vertex j st 0a...bji is opt knowing 0a...b is opt  
                                                subSubVWithNo_j = tuple([k for k in subVWithNo_i if k!=j])
                                                candLength = shortestLengths[(subSubVWithNo_j,j)] + self.AdjM[j][i]
                                                if candLength < shortestLengths[(subVWithNo_i,i)]:
                                                        shortestLengths[(subVWithNo_i,i)] = candLength
                                                        shortestOrders[(subVWithNo_i,i)] = shortestOrders[(subSubVWithNo_j,j)]+(i,)
                # On ajoute la derniere arete
                shortestLength = maxsize
                for i in setVWithNo_0:
                        subVWithNo_i = tuple([j for j in setVWithNo_0 if j!=i])
                        candLength = self.AdjM[i][0] + shortestLengths[(subVWithNo_i,i)]
                        if candLength < shortestLength:
                                shortestLength = candLength
                                shortestOrder =  shortestOrders[(subVWithNo_i,i)]+(0,)
                return shortestOrder  


class EuclidianCompleteGraph(Graph):
        def __init__(self, Points):
                self.sizeV = len(Points) 
                self.AdjM = [[Point2D.dist(Points[i],Points[j]) for j in range(self.sizeV)] for i in range(self.sizeV)]
                self.Points = Points
                
class Point2D():
        def __init__(self, x, y):
                self.x = x
                self.y = y

        def dist(p1,p2):
                return sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
        
class Edge():
        def __init__(self, p1, p2):
                self.p1 = p1
                self.p2 = p2

if __name__ == "__main__":
        import random as rnd
        n = 15
        Points = []
        fig, ax = plt.subplots()
        
        for i in range(n):
                newP = Point2D(rnd.random(),rnd.random())
                Points.append(newP)
                plt.plot(newP.x, newP.y, 'bo')
        ax.set_axis_off()
       
        plt.axis('scaled')
        plt.show(block=False)
        plt.pause(1)
        
        G = EuclidianCompleteGraph(Points)
        tsp = G.tspHK()
        
        for i in range(n):
                plt.plot([G.Points[tsp[i]].x,G.Points[tsp[i+1]].x], [G.Points[tsp[i]].y,G.Points[tsp[i+1]].y],'g')
        for i in range(n):
                plt.plot(Points[tsp[i]].x, Points[tsp[i]].y, 'bo')

        plt.draw()


##        M = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
##        G = Graph(M)
##        print(G.tspHK())

        
 
