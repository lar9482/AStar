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

    def __lt__(self, other):
        return (self.location.toNum() < other.location.toNum())

class GridProblem:

    def __init__(self, initialLocation = Location(0, 0), goalLocation = Location(100, 100), maxX = 100, maxY = 100):
        #Start state
        self.initialLocation = initialLocation

        #End state
        self.goalLocation = goalLocation

        #Blocked Locations
        self.blockedLocations = []

        #The uppper bound coordinates of the grid problem
        self.maxX = maxX
        self.maxY = maxY
    
    def isGoal(self, location):
        return (location.toNum() == self.goalLocation.toNum())

    def addBlockedLocation(self, location):
        self.blockedLocations.append(location)
    
    def isBlockedLocation(self, location):
        for blockedLocation in self.blockedLocations:
            if (blockedLocation.toNum() == location.toNum()):
                return True
        return False
    
    def outOfBounds(self, location):
        return (location.x < 0 or location.x > self.maxX or 
                location.y < 0 or location.y > self.maxY)
            
    
    def get_neighbor_locations(self, location):        
        neighbor_locations = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (not (i == 0 and j == 0)):
                    neighbor_locations.append(Location(location.x+i, location.y+j))

        return neighbor_locations
    
    def totalCost(self, location):
        return self.actionCost() + self.euclideanHeuristicCost(location)

    def actionCost(self):
        return 1
    
    def euclideanHeuristicCost(self, location):
        distanceXSquared = abs(location.x - self.goalLocation.x) ** 2
        distanceYSquared = abs(location.y - self.goalLocation.y) ** 2

        return math.sqrt(distanceXSquared + distanceYSquared)

def expand(problem, node):
    initialLocation = node.location
    childNodes = []

    for resultLocation in problem.get_neighbor_locations(initialLocation):
        
        resultCost = node.cost + problem.totalCost(resultLocation)

        if (not (problem.isBlockedLocation(resultLocation) or problem.outOfBounds(resultLocation))):
            newNode = Node(resultLocation, node, resultCost)
            childNodes.append(newNode)

    return childNodes

def best_first_search(problem = GridProblem()):
    node = Node(problem.initialLocation) 

    frontier = PriorityQueue()
    frontier.put((node.cost, node))

    reached = {node.location.toNum(): node}

    while not frontier.empty():
        node = frontier.get()[1]
        if (problem.isGoal(node.location)):
            return node

        for childNode in expand(problem, node):
            childLocation = childNode.location

            if ((reached.get(childLocation.toNum()) is None) or 
                (childNode.cost < reached.get(childLocation.toNum()).cost)):                
                reached[childLocation.toNum()] = childNode
                frontier.put((childNode.cost, childNode))

    return False

def main():
    problem = GridProblem(Location(0, 0), Location(134, 443), 500, 500)
    node = best_first_search(problem)
    while (not (node == None)):
        print(node.location.toNum())
        node = node.parent
    print()
    
    
if __name__ == "__main__":
    main()

