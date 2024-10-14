from sys import maxsize
import matplotlib.pyplot as plt
from math import sqrt

#from itertools import permutations


class Graph():
        def __init__(self, M):
                self.AdjMtx = M
                self.sizeV = len(M) 
                
        def tsp(self):
                W = [j for j in range(1,self.sizeV)]
                return self.shortestPathFromiWithinW(0, W)

        def shortestPathFromiWithinW(self, i, W):
                """Entrées: sommet i et sous-ensemble W des indices des sommets (différent de 0 et i)
                Retourne la longueur du plus court chemin allant de i jusque 0 en passant
                par chaque sommet de W exactement une fois"""
                
                if W == []: return self.AdjMtx[0][i]
                shortestCand = maxsize
                for j in W:
                        WWithNoj = [k for k in W if k!=j]
                        d = self.shortestPathFromiWithinW(j, WWithNoj)
                        if self.AdjMtx[i][j] + d < shortestCand:
                                shortestCand = self.AdjMtx[i][j] + d
                return shortestCand

        

class EuclidianCompleteGraph(Graph):
        def __init__(self, Points):
                self.sizeV = len(Points) 
                self.AdjMtx = [[Point2D.dist(Points[i],Points[j]) for j in range(self.sizeV)] for i in range(self.sizeV)]
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
        n = 7
        Points = []
        for i in range(n):
                newP = Point2D(rnd.random(),rnd.random())
                Points.append(newP)
                plt.plot(newP.x, newP.y, 'bo')
        
        plt.show()

        G = EuclidianCompleteGraph(Points)

        
        
        #M = [[0,1,1],[1,0,1],[1,1,0]]
        #M = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
        #G = Graph(M)

        print(G.tsp())

        
 
