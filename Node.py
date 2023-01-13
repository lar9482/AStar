import math 
from queue import PriorityQueue

class Location: 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def toNum(self):
        return (self.x, self.y)

class Node:
    def __init__(self, location = Location(0, 0), parent = None, cost = 0):

        # The coord represents the state of the node
        self.location = location

        self.parent = parent

        self.cost = cost



class GridProblem:

    def __init__(self, initialLocation = Location(0, 0), goalLocation = Location(100, 100), maxX = 100, maxY = 100):
        #Start state
        self.initialLocation = initialLocation

        #End state
        self.goalLocation = goalLocation

        #Blocked coords
        self.blockedCoords = []

        #The uppper bound coordinates of the grid problem
        self.maxX = maxX
        self.maxY = maxY
    
    def addBlockedCoord(self, coord):
        self.blockedCoords.append(coord)
    
    def isBlockedCoord(self, coord):
        for blockedCoord in self.blockedCoords:
            if (blockedCoord.toNum() == coord.toNum()):
                return True
        return False
    
    def outOfBounds(self, coord):
        return (coord.x < 0 or coord.x > self.maxX or 
                coord.y < 0 or coord.y > self.maxY)
            
    
    def get_neighbor_locations(self, location):

        return [Location(location.x, location.y+1),
                Location(location.x, location.y-1), 
                Location(location.x-1, location.y),
                Location(location.x+1, location.y)]
    
    def totalCost(self, coord):
        return self.actionCost() + self.euclideanHeuristicCost(coord)

    def actionCost(self):
        return 1
    
    def euclideanHeuristicCost(self, Location):
        distanceXSquared = abs(Location.x - self.goalLocation.x) ** 2
        distanceYSquared = abs(Location.y - self.goalLocation.y) ** 2

        return math.sqrt(distanceXSquared + distanceYSquared)

def expand(problem, node = Node()):
    initialLocation = node.location
    childNodes = []

    for resultLocation in problem.get_neighbor_locations(initialLocation):
        
        cost = node.cost + problem.totalCost(resultLocation)

        if (not (problem.isBlockedCoord(resultLocation) or problem.outOfBounds(resultLocation))):
            newNode = Node(resultLocation, node, cost)
            childNodes.append(newNode)

    return childNodes

def bfs(problem):
    node = Node(coord = problem.initialLocation) 

    frontier = PriorityQueue()
    frontier.put((node.cost, node))

    reached = {node.location.toNum: node}


def main():
    firstNode = Node(cost=15.15555555)
    secondNode = Node(cost=20.00052135413)
    thirdNode = Node(cost=141.14576455)

    queue = PriorityQueue()
    queue.put((firstNode.cost, firstNode))
    queue.put((secondNode.cost, secondNode))
    queue.put((thirdNode.cost, thirdNode))

    node = queue.get()[1]
    print()

    map = {firstNode.coord.toNum(): firstNode}

    test = map[firstNode.coord.toNum()]
    print()
    


if __name__ == "__main__":
    main()

