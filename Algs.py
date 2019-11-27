#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-21 17:57:11
# @Author  : Dong (dongwei@tamu.edu)
# @Link    : https://github.com/tomatoJr
# @Version : 1.0.0

import random
import math
import collections
import time
from MyGraph import *
from MaxHeap import *


def Dijkstra1(graph, src, dst):
    width = [0-math.inf]*len(graph.nodes())
    dad = [None]*len(graph.nodes())
    width[src] = math.inf
    queue = collections.deque([src])
    while queue:
        currentSrc = queue.popleft()
        for neighbor in graph.get_neighbors(currentSrc):
            alter = max(width[neighbor], min(width[currentSrc],
                                             graph.get_weight(currentSrc, neighbor)))
            if alter > width[neighbor]:
                width[neighbor] = alter
                dad[neighbor] = currentSrc
                queue.append(neighbor)

    # print results
    path = []
    last = dst
    while last != src:
        path.append(last)
        last = dad[last]

    # print('Max bandwidth path:', src, end=" ")
    # while path:
    #     print('->', path.pop(), end=" ")
    # print('\nmax bandwidth:', width[dst])

    return width[dst]


def Dijkstra2(graph, src, dst):
    status = dict()
    width = dict()
    dad = dict()
    for v in graph.nodes():
        status[v] = 'unseen'
    status[src] = 'intree'

    for neighbor in graph.get_neighbors(src):
        status[neighbor] = 'fringe'
        width[neighbor] = graph.get_weight(src, neighbor)
        dad[neighbor] = src

    while status[dst] != 'intree':
        # pick the best fringe v
        max = 0-math.inf
        for v, weight in width.items():
            if weight > max and status[v] == 'fringe':
                max = weight
                best_fringe = v

        # put best fringe v in tree
        status[best_fringe] = 'intree'
        for neighbor in graph.get_neighbors(best_fringe):
            weight = graph.get_weight(best_fringe, neighbor)
            if status[neighbor] == 'unseen':
                status[neighbor] = 'fringe'
                dad[neighbor] = best_fringe
                width[neighbor] = min(width[best_fringe], weight)
            elif status[neighbor] == 'fringe' and width[neighbor] < min(width[best_fringe], weight):
                dad[neighbor] = best_fringe
                width[neighbor] = min(width[best_fringe], weight)
    # print results
    path = []
    last = dst
    while last != src:
        path.append(last)
        last = dad[last]

    # print('Max bandwidth path:', src, end=" ")
    # while path:
    #     print('->', path.pop(), end=" ")
    # print('\nmax bandwidth:', width[dst])

    return width[dst]


def DijkstraHeap(graph, src, dst):
    # Initialization
    heap = MaxHeap()

    status = dict()
    width = dict()
    dad = dict()
    for v in graph.nodes():
        status[v] = 'unseen'
    status[src] = 'intree'
    for neighbor in graph.get_neighbors(src):
        status[neighbor] = 'fringe'
        width[neighbor] = graph.get_weight(src, neighbor)
        dad[neighbor] = src
        # insert into fringe heap
        heap.insert(neighbor, width[neighbor])

    while status[dst] != 'intree':
        # pick the best fringe v
        best_fringe = heap.maximum()[0]

        # put best fringe v in tree
        status[best_fringe] = 'intree'
        # heap.delete(0)
        heap.delete(best_fringe)

        for neighbor in graph.get_neighbors(best_fringe):
            weight = graph.get_weight(best_fringe, neighbor)
            if status[neighbor] == 'unseen':
                status[neighbor] = 'fringe'
                dad[neighbor] = best_fringe
                width[neighbor] = min(width[best_fringe], weight)
                # insert into fringe heap
                heap.insert(neighbor, width[neighbor])
            elif status[neighbor] == 'fringe' and width[neighbor] < min(width[best_fringe], weight):
                dad[neighbor] = best_fringe
                width[neighbor] = min(width[best_fringe], weight)
                heap.delete(neighbor)
                heap.insert(neighbor, width[neighbor])

    # print results
    path = []
    last = dst
    while last != src:
        path.append(last)
        last = dad[last]

    # print('Max bandwidth path:', src, end=" ")
    # while path:
    #     print('->', path.pop(), end=" ")
    # print('\nmax bandwidth:', width[dst])

    return width[dst]


def Kruskal(graph, src, dst):

    parent = [i for i in graph.nodes()]
    rank = [0]*len(graph.nodes())

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xr, yr = find(x), find(y)
        if xr != yr:
            if rank[xr] > rank[yr]:
                parent[yr] = xr
            elif rank[xr] < rank[yr]:
                parent[xr] = yr
            else:
                parent[xr] = yr
                rank[yr] += 1

    heap = MaxHeap()

    for edge in graph.edges():
        u, v, w = edge
        heap.insert((u, v), w)

    heap.heapSort()

    mst = MyGraph(graph.num_nodes())
    index = len(heap.H)-1

    while find(src) != find(dst):
        # u, v = heap.H[len(heap.H)-1]
        # weight = heap.D[len(heap.D)-1]
        # heap.delete((u, v))
        u, v = heap.H[index]
        weight = heap.D[index]
        index -= 1

        ur, vr = find(u), find(v)
        if ur != vr:
            union(ur, vr)
            mst.add_edge(u, v, weight)

    color = [None]*len(mst.nodes())
    path = []
    width = {}

    for i in mst.nodes():
        color[i] = 'white'
        width[i] = math.inf
    path.append(src)

    def dfs(src, dst, color, path, width):
        if src == dst:
            return path, width[dst]
        color[src] = 'grey'
        for neighbor in mst.get_neighbors(src):
            if color[neighbor] == 'white':
                width[neighbor] = min(
                    width[src], mst.get_weight(src, neighbor))
                path.append(neighbor)
                path, width[dst] = dfs(neighbor, dst, color, path, width)
                if dst in path:
                    return path, width[dst]
        color[src] = 'black'
        path.remove(src)
        return path, width[dst]

    dfs(src, dst, color, path, width)

    # # print results
    # print('Max bandwidth path:', path.pop(0), end=" ")
    # while path:
    #     print('->', path.pop(0), end=" ")
    # print('\nmax bandwidth:', width[dst])

    return width[dst]
