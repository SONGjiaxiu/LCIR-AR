__author__='SONG Jiaxiu'
# -*- coding: utf-8 -*-
"""
This module implements LCI_ar.
"""

import linecache
import string
import os
import math
import time
import networkx as nx
import sys
from collections import Counter
import operator
import networkx as nx             
import matplotlib.pyplot as plt
from networkx.generators.atlas import *
import numpy as np
import random
import requests
import pandas as pd
import csv
from networkx.algorithms.isomorphism.isomorph import graph_could_be_isomorphic as isomorphic
import linecache
import matplotlib
from operator import itemgetter
matplotlib.rcParams['font.family'] = 'sans-serif'  
matplotlib.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'# 中文设置成宋体，除此之外的字体设置成New Roman



sys.setrecursionlimit(2000000000)

def createGraph(filename) :
    G = nx.Graph()
    for line in open(filename) :
        strlist = line.split(',', 3)
        #n1 = int(strlist[0])
        #n2 = int(strlist[1])
        n1 = strlist[0]
        n2 = strlist[1]
        #weight = float(strlist[2])
        #G.add_weighted_edges_from([(n1, n2)]) 
        G.add_edge(n1,n2)
    return G
##构建网络的方式2
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def createGraph1(filename) :
    G = nx.Graph()
    for line in open(filename) :
        strlist = line.split()
        n1 = int(strlist[0])
        n2 = int(strlist[1])
        #weight = float(strlist[w_index])
        #G.add_weighted_edges_from([(n1, n2)]) 
        G.add_edge(n1,n2)
    return G

def remove_node1(G,node):
    for k in G.neighbors(node):
        G.remove_edge(node,k)
    return G
#*******************************************************************************************#
##CI中心性的2阶实现
def Collective_Influence(G, l=2):
    Collective_Influence_Dic = {}
    node_set = G.nodes()
    for nid in node_set:
        CI = 0
        neighbor_set = []
        neighbor_hop_1 = G.neighbors(nid)
        neighbor_hop_2 = []
        for nnid in neighbor_hop_1:
            neighbor_hop_2  = list(set(neighbor_hop_2).union(set(G.neighbors(nnid))))
            #print '2_hop:', nnid, G.neighbors(nnid)
        #end for

        center = [nid]
        neighbor_set = list(   set(neighbor_hop_2).difference(   set(neighbor_hop_1).union(set(center))  )    )
        #print nid, neighbor_hop_1, neighbor_hop_2, neighbor_set

        total_reduced_degree = 0
        for id in neighbor_set:
            total_reduced_degree = total_reduced_degree + (G.degree(id)-1.0)
        #end

        CI = (G.degree(nid)-1.0) * total_reduced_degree
        Collective_Influence_Dic[nid] =round(CI,3) 
    #end for
    #print "Collective_Influence_Dic:",sorted(Collective_Influence_Dic.iteritems(), key=lambda d:d[1], reverse = True)

    return Collective_Influence_Dic
G=createGraph(r"C:\Python27\sjxwork\LNewCI\political blogs.csv")
LCI={}
CI={}
LCIequalto0=[]
K_SORT={}
k=2 ###需要找的影响力节点组的个数
lamida=1
c=0
###CI
time_CI_start=time.time()
CI_update={}
time_CI=time.time()-time_CI_start
print "ci"
print CI
while len(LCIequalto0)*lamida<k:
    LCI_CURRENT=[]
    CI=Collective_Influence(G)
    for nid in G.nodes():
        LCII=0
        neighbor_hop_1 = G.neighbors(nid)
        #print neighbor_hop_1
        for neighbor in neighbor_hop_1:
            print neighbor
            if CI[nid]<CI[neighbor]:
                LCII=LCII+1
            else:
                pass
        LCI[nid]=LCII
        if LCI[nid]==0:
            LCIequalto0.append(nid)
            LCI_CURRENT.append(nid)
            CI_update[nid]=CI[nid]
        else:
            pass
    #print LCIequalto0
    LCIequalto0_len=len(LCIequalto0 )
    for nid in LCI_CURRENT:
        remove_node1(G,nid)
    c=c+1

sort_k=sorted(CI_update.iteritems(), key=lambda d:d[1], reverse = True)
id_sort_k= [x for x,_ in sort_k]
print id_sort_k[0:k]
s=id_sort_k[0:k]