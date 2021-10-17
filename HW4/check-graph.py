#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("Usage: check-graph.py <graph-file> <output-file>")
    sys.exit()

graph_file = sys.argv[1]
output_file = sys.argv[2]

edges = {}

f = open(graph_file)
f.readline()
f.readline()

for line in f:
    edge = line.strip().split(" ")
    x = int(edge[0])
    y = int(edge[1])
    if x not in edges:
        edges[x] = []
    edges[x].append(y)

f = open(output_file)
typ = f.readline().strip()

if typ == 'DAG':

    print(f"Checking DAG in {output_file}...")

    topsort = {}
    for (i,line) in enumerate(f):
        topsort[int(line)] = i

    for x in edges:
        for y in edges[x]:
            if (topsort[x] > topsort[y]):
                print(f"Found bad edge: {x} -> {y}")
                exit(1)

    print("Topsort looks good!")
else:
    print(f"Checking cycle in {output_file}...")

    try:
        start = int(f.readline())
        prev = start
        for nodestr in f:
            node = int(nodestr)
            if node not in edges[prev]:
                print(f"Edge {prev} -> {node} is not in the graph.")
                exit(1)
            prev = node

        if start not in edges[prev]:
            print(f"Edge {prev} -> {start} is not in the graph.")
            exit(1)

        print("Cycle looks good!")
    except ValueError:
        print("No cycle evidence given.")
