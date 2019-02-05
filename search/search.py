# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    # *** YOUR CODE HERE ***

    chemin = []
    seen = []
    looking = []

    start = problem.getStartState()
    neighboors = problem.getSuccessors(start)
    for e in neighboors:
        looking.append(e[0])
    chemin.append(neighboors[-1])
    print neighboors

    flag = True
    while flag:

        if looking == []:
            print 'looking is empty'
            break
        else:
            currentPlace = chemin.pop()  # Triplet currentPlace
            print ' ####  currentPlace : ', currentPlace

        if (problem.isGoalState(currentPlace[0])):  # Just arrived !
            chemin.append(currentPlace)
            break

        chemin.append(currentPlace)  # Indent du chemin reponse

        neighboors = problem.getSuccessors(currentPlace[0])

        neiNotSeen = []
        for e in neighboors:
            if not(e[0] in seen):
                neiNotSeen.append(e)

        if neiNotSeen == []:
            supp = chemin.pop()
        else:
            for e in neiNotSeen:
                if not(e[0] in looking):
                    looking.append(e[0])
            looking.pop()
            chemin.append(neiNotSeen[-1])

        seen.append(currentPlace[0])

    sol = []
    for e in chemin:
        sol.append(e[1])
    return sol


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    dic = dict()
    decouverts = []
    Q = util.Queue()

    start = problem.getStartState()
    Q.push(start)
    decouverts.append(start)

    finish = start
    print 'isEmpty', Q.isEmpty()
    while not(Q.isEmpty()):
        current = Q.pop()
        print 'current', current
        if problem.isGoalState(current[0]):
            print 'current', current
            finish = current
            break
        if current == start:
            neighboors = problem.getSuccessors(current)
        else:
            neighboors = problem.getSuccessors(current[0])
        print 'neighboors', neighboors
        for v in neighboors:
            if not(v[0] in decouverts):
                dic[v] = current
                decouverts.append(v[0])
                Q.push(v)

    P, last, start = dic, finish, start
    print 'last', last
    chemin = [last]
    while last != start:
        last = P[last]
        chemin.append(last)
    chemin.reverse()

    sol = []
    for e in chemin:
        if e != start:
            sol.append(e[1])

    return sol


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    dic = dict()
    decouverts = []
    Q = util.PriorityQueue()

    start = problem.getStartState()
    Q.push(start, 0)
    decouverts.append(start)

    finish = start
    print 'isEmpty', Q.isEmpty()
    while not(Q.isEmpty()):
        current = Q.pop()
        print 'current', current
        if problem.isGoalState(current[0]):
            print 'current', current
            finish = current
            break
        if current == start:
            neighboors = problem.getSuccessors(current)
        else:
            neighboors = problem.getSuccessors(current[0])
        print 'neighboors', neighboors
        for v in neighboors:
            if not(v[0] in decouverts):
                dic[v] = current
                decouverts.append(v[0])
                Q.push(v, v[2])

    P, last, start = dic, finish, start
    print 'last', last
    chemin = [last]
    while last != start:
        last = P[last]
        chemin.append(last)
    chemin.reverse()

    sol = []
    for e in chemin:
        if e != start:
            sol.append(e[1])

    return sol


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
