import math 
from queue import PriorityQueue

class Coord: 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def toNum(self):
        return (self.x, self.y)

class Node:
    def __init__(self, coord = Coord(0, 0), parent = None, action = "", cost = 0):

        # The coord represents the state of the node
        self.coord = coord

        self.parent = parent

        self.action = action
        self.cost = cost



class GridProblem:

    def __init__(self, initialCoord = Coord(0, 0), goalCoord = Coord(100, 100), maxX = 100, maxY = 100):
        #Start state
        self.initialCoord = initialCoord

        #End state
        self.goalCoord = goalCoord

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
            
    
    def result(self, coord, action):
        match action:
            case "Up":
                return Coord(coord.x, coord.y+1)
            case "Down":
                return Coord(coord.x, coord.y-1)
            case "Left":
                return Coord(coord.x-1, coord.y)
            case "Right":
                return Coord(coord.x+1, coord.y)
            case _:
                Exception("Invalid Action Passed")
    
    def totalCost(self, coord):
        return self.actionCost() + self.euclideanHeuristicCost(coord)

    def actionCost(self):
        return 1
    
    def euclideanHeuristicCost(self, coord):
        distanceXSquared = abs(coord.x - self.goalCoord.x) ** 2
        distanceYSquared = abs(coord.y - self.goalCoord.y) ** 2

        return math.sqrt(distanceXSquared + distanceYSquared)

def expand(problem, node = Node()):
    initialCoords = node.coord
    possibleActions = ["Up", "Down", "Left", "Right"]
    childNodes = []

    for action in possibleActions:
        resultCoord = problem.result(initialCoords, action)
        cost = node.cost + problem.totalCost(resultCoord)

        if (not (problem.isBlockedCoord(resultCoord) or problem.outOfBounds(resultCoord))):
            newNode = Node(resultCoord, node, action, cost)
            childNodes.append(newNode)

    return childNodes

def bfs(problem):
    node = Node(coord = problem.initialCoord) 

    frontier = PriorityQueue()
    frontier.put((node.cost, node))

    reached = {node.coord.toNum: node}


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

