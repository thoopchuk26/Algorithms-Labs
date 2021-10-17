from collections import defaultdict, deque
    
def listCreation():
    graph = defaultdict(list)
    parent = defaultdict(list)
    graphFile = open("graphs/graph-big-1.in", "r")
    for line in graphFile:
        if(len(line.split()) > 1):
            values = line.strip().split()
            graph[values[0]].append(values[1]) 
            if values[1] not in graph.keys():
                graph[values[1]] = []
    graphFile.close()
    return graph

def topSort():
    f = open("graphs/graph-big-1.out", "w")

    sorted = {}
    sorted["DAG"] = None
    queue = deque([])
    inD = defaultdict(int)
    graph = listCreation()

    for i in graph:
        for u in graph[i]:
            inD[u]+=1

    for i in graph:
        if inD[i] == 0:
            queue.append(i)

    while queue:
        s = queue.popleft()
        sorted[s] = None
        for i in graph[s]:
            inD[i]-=1
            if inD[i] == 0 and i not in sorted:
                queue.append(i)

    if len(sorted) < len(graph.keys()):
        for i in graph:
            cycle = {}
            parent = {}
            if inD[i] > 0:
                visited = {}
                parent[i] = None
                queue.append(i)
                visited[i] = None
                while queue:
                    s = queue.popleft()
                    for u in graph[s]:
                        if u not in visited:
                            visited[u] = None
                            queue.append(u)
                            parent[u] = s
                for u in parent:
                    if i in graph[u]:
                        queue.append(u)
                        while queue:
                            s = queue.popleft()
                            cycle[s] = None
                            if i not in cycle:
                                queue.append(parent[s])
                if len(cycle) > 0:
                    cycle["Cycle: "] = None
                    cycleList = list(cycle.keys())
                    cycleList.reverse()
                    for line in cycleList:
                        f.writelines(str(line)+"\n")
                    return cycleList
    else:
        for line in sorted:
            f.writelines(str(line)+"\n")
        return sorted

print(topSort())