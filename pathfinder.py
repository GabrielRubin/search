#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys
import Queue
import math

from common import *

# ==========================================
# Class Node
# ==========================================

class Node:

    def _init_(self, x, y, type="Common", cost=1):
        self.m_x = x
        self.m_y = y
        self.m_type = type
        self.m_cost = cost

    # ======================================
    # Cost
    # ======================================

    def get_cost(self):
        return self.m_cost

# ==========================================
# Class PathFinder A Star
# ==========================================

class PathFinder_A_Star:

    def __init__(self):

        pass

    # ------------------------------------------
    # Heuristic
    # ------------------------------------------

    def heuristic(self, x1, y1, x2, y2):

        xdif = x1 - x2
        ydif = y1 - y2

        return abs(xdif) + abs(ydif)
    
    # ------------------------------------------
    # Solve
    # ------------------------------------------

    def solve(self, sx, sy, gx, gy, map_data, map_width, map_height):

        visitedNodes = []

        nextNodes = Queue.PriorityQueue()

        pathNodes = []

        start = Node(sx, sy)

        goal = Node(gx, gy)

        startNeighbors = successors(start.m_x, start.m_y, map_data, map_width, map_height)

        foundPath = False

        for neighbor in startNeighbors:
            node = Node(neighbor[0], neighbor[1])

            score = self.heuristic(start.m_x, start.m_y, node.m_x, node.m_y)

            nextNodes.put(score * -1, node) # Phytons PriorityQueue gets elements by lowest numbers (score * -1) (TEST ?)

        while(nextNodes.empty() == False and foundPath == False):

            currentNode = nextNodes.get()[1]

            if(currentNode.m_x == goal.m_x and currentNode.m_y == goal.m_y):
                pathNodes.append(currentNode)
                foundPath = True
                break

            visitedNodes.append(currentNode)

        if(foundPath == True):
            return pathNodes

        return None

    # ------------------------------------------
    # Get solvable
    # ------------------------------------------

    def get_solvable(self):
        # TODO return True if plan found, otherwise False
        return False

    # ------------------------------------------
    # Get max tree height
    # ------------------------------------------

    def get_max_tree_height(self):
        # TODO return max tree height if plan found, otherwise None
        return None

    # ------------------------------------------
    # Get min moves
    # ------------------------------------------

    def get_min_moves(self):
        # TODO return size of minimal plan to reach goal if plan found, otherwise None
        return None

# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 2:
        map_name = sys.argv[1]
    else:
        map_name = DEFAULT_MAP
    print "Loading map: " + map_name
    sx, sy, gx, gy, map_data, map_width, map_height = read_map(map_name)
    plan = PathFinder_A_Star().solve(sx, sy, gx, gy, map_data, map_width, map_height)
    if plan == None:
        print "No plan was found"
    else:
        print "Plan found:"
        for i, move in enumerate(plan):
            if move == MOVE_UP:
                print i, ": Move Up"
            elif move == MOVE_DOWN:
                print i, ": Move Down"
            elif move == MOVE_LEFT:
                print i, ": Move Left"
            elif move == MOVE_RIGHT:
                print i, ": Move Right"
            else:
                print i, ": Movement unknown = ", move