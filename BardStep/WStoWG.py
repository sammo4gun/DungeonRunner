import os
import networkx as nx

TRANSLATION = { 'adjacent': 'connected to', 'at': "located in", 'had': 'had',
                'in': "located in", 'has': 'has', 'burried': 'buried'}

def getNodes(domain, problem):
    pr = False
    objects = {}

    d = open(domain)
    for line in d:
        if line.strip().startswith("(:constants"): pr = True
        if pr:
            prline = line.strip().replace("(:constants ", "").strip(')')
            prline = prline.split()
            t = False
            wl = []
            for i in prline:
                if t == True:
                    type = i
                elif i == '-':
                    t = True
                else:
                    wl.append(i)
            objects[type] = wl
        if pr and ')' in line: pr = False
    d.close()

    p = open(problem)
    for line in p:
        if line.strip().startswith("(:objects"): pr = True
        if pr:
            prline = line.strip().replace("(:objects ", "").strip(')')
            prline = prline.split()
            t = False
            wl = []
            for i in prline:
                if t == True:
                    type = i
                elif i == '-':
                    t = True
                else:
                    wl.append(i)
            if type in objects: objects[type] += wl
            else: objects[type] = wl
        if pr and ')' in line: pr = False
    p.close()

    return objects

def makeRelations(problem, graph):
    #the relation names are:
    #"at" character to location
    #"adjacent" location to location
    #"has" item to character
    #"in" item to location
    pr = False
    p = open(problem)
    for line in p:
        if line.strip().startswith("(:init"): pr = True
        if pr:
            prline=line.strip().replace("(:init ", "").strip("()")
            prline=prline.split()
            if len(prline) == 0:
                break
            relation = prline[0]
            if relation.startswith(':'): pr = False
            if len(prline) > 1 and relation in TRANSLATION.keys():
                i1, i2 = prline[1],prline[2]
                graph.add_edge(i1, i2, label = TRANSLATION[relation])
            if len(prline) == 1:
                graph.add_nodes_from([relation], type='statement', fillcolor = "red", style = 'filled')
    p.close()
    return graph

def makeNodes(objects):
    graph = nx.Graph()
    graph.add_nodes_from(objects["room"], type='location', fillcolor="yellow", style="filled")
    graph.add_nodes_from(objects["item"], type='object', fillcolor="white", style="filled")
    graph.add_nodes_from(objects["character"], type='character', fillcolor="orange", style="filled")

    return graph

def getWG(  problem = 'tests/door-problem.pddl',
            domain = 'tests/door-domain.pddl',
            output = 'log/graph.dot'):
    objects = getNodes(domain, problem)
    g = makeNodes(objects)
    g = makeRelations(problem, g)

    nx.nx_pydot.write_dot(g, output)

if __name__ == "main":
    objects = getNodes("door-domain.pddl", "door-problem-output.pddl")
    print(objects)
    g = makeNodes(objects)
    g = makeRelations("door-problem-output.pddl", g)

    nx.nx_pydot.write_dot(g, "door.dot")
