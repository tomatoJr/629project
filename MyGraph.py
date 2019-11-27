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


class MyGraph:
    def __init__(self, num=0, avg_degree=0, weight_rank=0):
        # def __init__(self, num=0):
        self.graph = collections.defaultdict(dict)
        # make nodes
        for i in range(num):
            self.add_node(i)
        # self.make_random_edges(num, avg_degree, weight_rank)

    def make_random_edges(self, num=0,  avg_degree=0, weight_rank=0):
        # make a weighted cycle
        for i in range(num-1):
            self.add_edge(i, i+1, int(random.random()*weight_rank))
        self.add_edge(num-1, 0, int(random.random()*weight_rank))

        for i in self.nodes():
            while len(self.graph[i]) < avg_degree:
                self.add_edge(i, int(random.random()*num),
                              int(random.random()*weight_rank))

        print('Number of nodes', self.num_nodes())
        print('Number of edges', self.num_edges())
        print('Average degree of the graph is',
              self.num_edges()*2/self.num_nodes())

    def add_node(self, i):
        if i not in self.graph:
            self.graph[i] = dict()

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def edges(self):
        edges = []
        for u, neighbors in self.graph.items():
            for v in neighbors:
                if u < v:
                    edge = [u, v, self.graph[u][v]]
                    edges.append(edge)
        return edges

    def nodes(self):
        return list(self.graph.keys())

    def num_nodes(self):
        return len(list(self.graph.keys()))

    def num_edges(self):
        return len(self.edges())

    def get_neighbors(self, u):
        return list(self.graph[u].keys())

    def get_weight(self, u, v):
        return self.graph[u][v]
