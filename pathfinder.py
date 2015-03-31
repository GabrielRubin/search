#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys
import Queue
import math
import copy

from common import *

# ==========================================
# Class Node
# ==========================================

class Node:

    m_cameFrom = None

    m_latestCost = 0

    m_treeHeight = 0

    def __init__(self, x, y, type="Common", cost=1):
        self.m_x = x
        self.m_y = y
        self.m_type = type
        self.m_cost = cost

    # ======================================
    # Equals
    # ======================================

    def __eq__(self, other):
        return self.m_x == other.m_x and self.m_y == other.m_y

    # ======================================
    # Not Equals
    # ======================================

    def __ne__(self, other):
        return not self == other

    # ======================================
    # Cost
    # ======================================

    def get_cost(self):
        return self.m_cost

# ==========================================
# Class PathFinder A Star
# ==========================================

class PathFinder_A_Star:

    m_maxTreeHeight = None

    m_minMoves = None

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

    def solve(self, sx, sy, gx, gy, map_data, map_width, map_height, getMaxHeigh = False):

        if(PathFinder_A_Star().get_solvable(sx, sy, gx, gy, copy.deepcopy(map_data), map_width, map_height) == False):
            return None

        visitedNodes = []

        nextNodes = Queue.PriorityQueue()

        maxHeight = 0

        start = Node(sx, sy)

        goal = Node(gx, gy)

        startScore = self.heuristic(start.m_x, start.m_y, goal.m_x, goal.m_y)

        nextNodes.put((startScore, start))

        while(nextNodes.empty() == False):

            currentNode = nextNodes.get()[1]

            if(maxHeight < currentNode.m_treeHeight):

                maxHeight = currentNode.m_treeHeight

            if(currentNode.m_x == goal.m_x and currentNode.m_y == goal.m_y):

                result = self.reconstruct_path(currentNode)

                if(getMaxHeigh == False):
                    return result

                continue

            # Was it already in the visited Nodes? If yes, update the value that was there. If not, ignore this node
            if(currentNode in visitedNodes):

                if(visitedNodes[visitedNodes.index(currentNode)].m_latestCost < currentNode.m_latestCost):
                    continue
                else:
                    visitedNodes[visitedNodes.index(currentNode)].m_latestCost = currentNode.m_latestCost

            else:
                visitedNodes.append(currentNode)

            neighbors = successors(currentNode.m_x, currentNode.m_y, map_data, map_width, map_height)

            for neighbor in neighbors:

                node = Node(neighbor[0], neighbor[1])

                score = self.heuristic(node.m_x, node.m_y, goal.m_x, goal.m_y) + node.get_cost()

                node.m_latestCost = currentNode.m_latestCost + node.get_cost()

                node.m_cameFrom = currentNode

                node.m_treeHeight = currentNode.m_treeHeight + 1

                nextNodes.put((score, node))

        if(getMaxHeigh):
            self.m_maxTreeHeight = maxHeight

        return None

    # ------------------------------------------
    # Reconstruct Path (for link)
    # ------------------------------------------

    def reconstruct_path(self, node):

        nodes = []

        directions = []

        while(True):
            if(node.m_cameFrom is not None):

                nodes.append(node)

                node = node.m_cameFrom

            else: # its the start node

                nodes.append(node)

                break

        nodes.reverse()

        for i in range(0, len(nodes) - 1):

            dir = direction(nodes[i].m_x, nodes[i].m_y, nodes[i + 1].m_x, nodes[i + 1].m_y)

            directions.append(dir)

        self.m_minMoves = len(directions)

        self.m_maxTreeHeight = len(directions)

        return directions

    # ------------------------------------------
    # Get solvable
    # ------------------------------------------

    def get_solvable(self, sx, sy, gx, gy, map, map_width, map_height):

        return self.searchGoal(sx, sy, map, map_width, map_height)

    # ------------------------------------------
    # Search For Goal
    # ------------------------------------------

    def searchGoal(self, x, y, map, map_width, map_height):

        result = False

        if(map[y][x] == TILE_CLOSED):
            return False

        if(map[y][x] == TILE_GOAL):
            return True

        map[y][x] = TILE_CLOSED

        neighbors = successors(x, y, map, map_width, map_height)

        for neighbor in neighbors:

            result = result or self.searchGoal(neighbor[0], neighbor[1], map, map_width, map_height)

        return result

    # ------------------------------------------
    # Get max tree height
    # ------------------------------------------

    def get_max_tree_height(self):

        return self.m_maxTreeHeight

    # ------------------------------------------
    # Get min moves
    # ------------------------------------------

    def get_min_moves(self):

        return self.m_minMoves

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

#print(PathFinder_A_Star().get_solvable(sx, sy, gx, gy, map_data, map_width, map_height))