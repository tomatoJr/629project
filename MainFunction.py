#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-21 17:57:11
# @Author  : Dong (dongwei@tamu.edu)
# @Link    : https://github.com/tomatoJr
# @Version : 1.0.0

import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import collections
import time
from MyGraph import *
from MaxHeap import *
from Algs import *


def Testing():
    # testing
    graphs = []
    for i in range(1):
        sparse_graph = MyGraph(5000, 6, 1000)
        sparse_graph.make_random_edges(5000, 6, 1000)
        graphs.append(sparse_graph)

        dense_graph = MyGraph(5000, 1000, 1000)
        dense_graph.make_random_edges(5000, 1000, 1000)
        graphs.append(dense_graph)

    for graph in graphs:
        for i in range(1):
            src = int(random.random()*5000)
            dst = int(random.random()*5000)
            print('src:', src, ' dst:', dst)

            starttime = (time.time())
            Dijkstra1(graph, src, dst)
            endtime = (time.time())
            print("Dijkstra runs in ", endtime-starttime, " s")

            starttime = (time.time())
            Dijkstra2(graph, src, dst)
            endtime = (time.time())
            print("Dijkstra runs in ", endtime-starttime, " s")

            starttime = (time.time())
            DijkstraHeap(graph, src, dst)
            endtime = (time.time())
            print("DijkstraHeap runs in ", endtime-starttime, " s")

            starttime = (time.time())
            Kruskal(graph, src, dst)
            endtime = (time.time())
            print("Kruskal runs in ", endtime-starttime, " s")


def runDijkstra1(graph, src, dst):
    starttime = (time.time())
    ans = Dijkstra1(graph, src, dst)
    endtime = (time.time())
    print("Dijkstra runs in ", endtime-starttime, " s")
    print('max bandwidth: ', ans)


def runDijkstra2(graph, src, dst):
    starttime = (time.time())
    ans = Dijkstra2(graph, src, dst)
    endtime = (time.time())
    print("Dijkstra runs in ", endtime-starttime, " s")
    print('max bandwidth: ', ans)


def runDijkstraHeap(graph, src, dst):
    starttime = (time.time())
    ans = DijkstraHeap(graph, src, dst)
    endtime = (time.time())
    print("DijkstraHeap runs in ", endtime-starttime, " s")
    print('max bandwidth: ', ans)


def runKruskal(graph, src, dst):
    starttime = (time.time())
    ans = Kruskal(graph, src, dst)
    endtime = (time.time())
    print("Kruskal runs in ", endtime-starttime, " s")
    print('max bandwidth: ', ans)


if __name__ == "__main__":
    # sparse_graph = MyGraph(5000, 6, 1000)
    # sparse_graph.make_random_edges(5000, 6, 1000)

    dense_graph = MyGraph(5000, 1000, 1000)
    dense_graph.make_random_edges(5000, 1000, 1000)

    for i in range(5):
        src = int(random.random()*5000)
        dst = int(random.random()*5000)
        print('src:', src, ' dst:', dst)

        # # runDijkstra1(sparse_graph, src, dst)
        # runDijkstra2(sparse_graph, src, dst)
        # runDijkstraHeap(sparse_graph, src, dst)
        # runKruskal(sparse_graph, src, dst)

        # runDijkstra1(dense_graph, src, dst)
        runDijkstra2(dense_graph, src, dst)
        runDijkstraHeap(dense_graph, src, dst)
        runKruskal(dense_graph, src, dst)
