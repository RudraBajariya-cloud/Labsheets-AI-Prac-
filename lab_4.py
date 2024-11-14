# -*- coding: utf-8 -*-
"""lab_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z-FuPUVe2d_9TkEiGlRI-GhWPp3_J2zI
"""

import queue

def getHeuristics():
  heuristics={}
  f=open("heuristics.txt")
  for i in f.readlines():
    node_heuristic_val=i.split()
    heuristics[node_heuristic_val[0]]=int(node_heuristic_val[1])
  return heuristics

def createGraph():
    graph = {}
    file = open("/content/citiesGraph.txt")
    for i in file.readlines():
        node_val = i.split()

        if node_val[0] in graph and node_val[1] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

        elif node_val[0] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            graph[node_val[1]] = [[node_val[0], node_val[2]]]

        elif node_val[1] in graph:
            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

            graph[node_val[0]] = [[node_val[1], node_val[2]]]

        else:
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
            graph[node_val[1]] = [[node_val[0], node_val[2]]]

    return graph

def GBFS(startNode, heuristics, graph, goalNode="Bucharest"):
    priorityQueue = queue.PriorityQueue()
    priorityQueue.put((heuristics[startNode], startNode))

    path = []

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current)

        if current == goalNode:
            break

        priorityQueue = queue.PriorityQueue()

        for i in graph[current]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]], i[0]))

    return path

def Astar(startNode, heuristics, graph, goalNode="Bucharest"):
  priorityQueue = queue.PriorityQueue()
  distance = 0
  path = []
  priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))
  while priorityQueue.empty() == False:
    current = priorityQueue.get()[1]
    path.append(current[0])
    distance += int(current[1])
    if current[0] == goalNode:
      break
    priorityQueue = queue.PriorityQueue()
    for i in graph[current[0]]:
      if i[0] not in path:
        priorityQueue.put((heuristics[i[0]] + int(i[1]) + distance, i))
  return path

heuristic = getHeuristics()
graph = createGraph()
#city, citiesCode = getCity()

cityName = "Zerind" #citiesCode[inputCode]
gbfs = GBFS(cityName, heuristic, graph)
astar = Astar(cityName, heuristic, graph)
print("GBFS => ", gbfs)
print("ASTAR => ", astar)

"""1. given a pathfind out the cost
2. given a new destination calcculate new heuristics to perform A* and greedy best first search
3. check if it is admissible or not
"""

def getStepCost(source, target):
  file=open("citiesGraph.txt")
  for i in file.readlines():
    parts=i.split(" ")
    if(parts[0]==source and parts[1]==target):
      return int(parts[2])
    if(parts[0]==target and parts[1]==source):
      return int(parts[2])
  return 0

def getPathCost(route):
  pathCost=0
  for i in range(0, len(route)-1):
    source=route[i]
    target=route[i+1]
    pathCost+=getStepCost(source, target)
  return pathCost

print(getPathCost(gbfs))
print(getPathCost(astar))

def getManhattanHeuristic(goal):
  file=open("cities.txt")
  lines=file.readlines()
  goalX=0
  goalY=0
  cityList=set()
  for line in lines:
    parts=line.split(" ")
    cityList.add(parts[0])
  for line in lines:
    parts=line.split(" ")
    if(parts[0]==goal):
      goalX=int(parts[1])
      goalY=int(parts[2])
      break
  heuristics={}
  for line in lines:
    parts=line.split(" ")
    cityX=int(parts[1])
    cityY=int(parts[2])
    xdiff=abs(cityX-goalX)
    ydiff=abs(cityY-goalY)
    heuristics[parts[0]]=xdiff+ydiff
   # print(heuristics)
  return heuristics



heuristic=getHeuristics()
graph=createGraph()
cityName="Oradea"
gbfs=GBFS(cityName, heuristic, graph)
astar=Astar(cityName, heuristic, graph)
print("GBFS => ", gbfs)
print("ASTAR => ", astar)

goalNode='Neamt'
heuristic=getManhattanHeuristic(goalNode)
graph=createGraph()

cityName="Oradea"
gbfs=GBFS(cityName, heuristic, graph,goalNode)
astar=Astar(cityName, heuristic, graph,goalNode)
print("GBFS => ", gbfs)
print("ASTAR => ", astar)

print(getManhattanHeuristic("Neamt"))

import math

def getEuclideanHeuristic(goal):
    file = open("cities.txt")
    lines = file.readlines()
    goalX = 0
    goalY = 0
    cityList = set()

    for line in lines:
        parts = line.split(" ")
        cityList.add(parts[0])

    # Find the coordinates of the goal city
    for line in lines:
        parts = line.split(" ")
        if parts[0] == goal:
            goalX = int(parts[1])
            goalY = int(parts[2])
            break

    heuristics = {}

    # Compute Euclidean distance for all cities
    for line in lines:
        parts = line.split(" ")
        cityX = int(parts[1])
        cityY = int(parts[2])
        xdiff = cityX - goalX
        ydiff = cityY - goalY
        heuristics[parts[0]] = math.sqrt(xdiff**2 + ydiff**2)

    return heuristics

print(getEuclideanHeuristic("Neamt"))

goalNode='Neamt'
heuristic=getEuclideanHeuristic(goalNode)
graph=createGraph()

cityName="Oradea"
gbfs=GBFS(cityName, heuristic, graph,goalNode)
astar=Astar(cityName, heuristic, graph,goalNode)
print("GBFS => ", gbfs)
print("ASTAR => ", astar)

def is_admissible(heuristic, graph, start_node, goal_node):
  def dijkstra(start, graph):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    priority_queue = [(0, start)]

    while priority_queue:
      current_distance, current_node = priority_queue.pop(0)

      if current_node in visited:
        continue
      visited.add(current_node)

      for neighbor, edge_cost in graph.get(current_node, []):
        distance = current_distance + int(edge_cost)
        if distance < distances[neighbor]:
          distances[neighbor] = distance
          priority_queue.append((distance, neighbor))
          priority_queue.sort()  # Maintain min-heap

    return distances

  distances = dijkstra(start_node, graph)

  for node in graph:
    if heuristic[node] > distances[node]:
      print(f"Heuristic for {node} ({heuristic[node]}) is greater than actual cost to goal ({distances[node]})")
      return False

  return True

# Example usage:
heuristic = getManhattanHeuristic('Neamt')
graph = createGraph()
start_node = 'Oradea'
goal_node = 'Neamt'

if is_admissible(heuristic, graph, start_node, goal_node):
  print("Heuristic is admissible.")
else:
  print("Heuristic is not admissible.")