from collections import defaultdict, deque

def BFS():
    edges = 299997
    graph = defaultdict(list)
    parent = {}
    queue = deque([])
    visited = {}
    startNode = "Trey"
    endNode = "END"

    graph = listCreation(graph)
    queue.append(startNode)
    visited[startNode] = None

    while queue:
        s = queue.popleft()
        if s == endNode:
            return parentTrace(parent, startNode, endNode)
        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited[i] = None
                parent[i] = s    

def listCreation(graph):
    graphFile = open("graph-F21.txt", "r")
    for line in graphFile:
        values = line.rsplit(" ")
        values[1] = values[1].replace("\n", "")
        graph[values[0]].append(values[1]) 
        graph[values[1]].append(values[0])
    graphFile.close()
    return graph


def parentTrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

print(BFS())