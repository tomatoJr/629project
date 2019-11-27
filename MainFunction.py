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
    # print("Dijkstra runs in ", endtime-starttime, " s")
    print('max bandwidth: ', ans)


def runDijkstra2(graph, src, dst):
    starttime = (time.time())
    ans = Dijkstra2(graph, src, dst)
    endtime = (time.time())
    # print("Dijkstra runs in ", endtime-starttime, " s")
    print('max bandwidth: ', ans)
    print('The running time of Modified Dijkstra’s algorithm without heap structure: ', end='')
    print(endtime-starttime)


def runDijkstraHeap(graph, src, dst):
    starttime = (time.time())
    ans = DijkstraHeap(graph, src, dst)
    endtime = (time.time())
    # print("DijkstraHeap runs in ", endtime-starttime, " s")
    print('max bandwidth: ', ans)
    print('The running time of Modified Dijkstra’s algorithm using heap structure: ', end='')
    print(endtime-starttime)


def runKruskal(graph, src, dst):
    starttime = (time.time())
    ans = Kruskal(graph, src, dst)
    endtime = (time.time())
    # print("Kruskal runs in ", endtime-starttime, " s")
    print('max bandwidth: ', ans)
    print('The running time of Modified Kruskal’s algorithm using heapsort: ', end='')
    print(endtime-starttime)


if __name__ == "__main__":
    num_nodes = 5000
    weight_rank = 1000
    src = int(random.random()*num_nodes)
    dst = int(random.random()*num_nodes)
    print('src:', src, ' dst:', dst)

    # run the following code for sparse graph test cases
    print('In sparse graph:')
    sparse_graph = MyGraph(num_nodes, 6, weight_rank)
    sparse_graph.make_random_edges(num_nodes, 6, weight_rank)
    runDijkstra2(sparse_graph, src, dst)
    runDijkstraHeap(sparse_graph, src, dst)
    runKruskal(sparse_graph, src, dst)

    # # run the following code for dense graph test cases
    # print('In dense graph:')
    # dense_graph = MyGraph(num_nodes, 1000, weight_rank)
    # dense_graph.make_random_edges(num_nodes, 1000, weight_rank)
    # runDijkstra2(dense_graph, src, dst)
    # runDijkstraHeap(dense_graph, src, dst)
    # runKruskal(dense_graph, src, dst)
