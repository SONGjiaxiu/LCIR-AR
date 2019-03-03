from __future__ import print_function
import sys
from operator import itemgetter
sys.setrecursionlimit(2000000000)
file2 = open(r"F:\sjx\destruction_example_1.txt", "w+")
def readfile(input):
	f = open(input,'rU')
	for line in f:
		temp = line.split()
		var1 = int(temp[0])
		var2 = int(temp[1])
		if var1 in adjlist:
			adjlist[var1].append(var2)
	
		else:
			adjlist[var1] = [var2] 
		if var2 in adjlist:
			adjlist[var2].append(var1)
		else:
			adjlist[var2] = [var1] 
def changelist1(netlist):
	max = 0
	for d in netlist:
		if len(d) > max:
			max = len(d)
			maxnet = d	
	max = 0
	for key in maxnet:
		if max < len(maxnet[key]):
			max = len(maxnet[key])
			k = key
	netlist.remove(maxnet)
	removenode(netlist, maxnet, k)
	return k, max
k=0
def changelist2(netlist):
	max = 0
	#print("**************netlist*******************", netlist)
	for d in netlist:
		if len(d) > max:
			max = len(d)
			maxnet = d
	maxmetric = 0
	sum = 0
	#CI_list = {}
	#CI_all = []
	prev = []
	#print("*********************************", len(maxnet))
	for key in maxnet:
		visited = []
		l = []
		for i in range(maxcount):
			visited.append(False)
		#DFS2(maxnet, key, visited, l)
		#print("key", key)
		#print("keyivisted",visited)
		#print("************maxnet*********************", maxnet)
		BFS(maxnet, key, visited, l,prev)
		prev[:]=[]
		#print("lllll",l)
		for i in l:
			sum += len(maxnet[i]) - 1
		metric = (len(maxnet[key]) - 1) * sum
		sum = 0
		#l[:] = []
		#print("************maxnet*********************", maxnet)
		#CI_list[key]=metric
		print("node", key,"CI",metric)
		if maxmetric < metric:
			maxmetric = metric
			k = key
		#print("&&&&&&&&&&&&&&CI&&&&&&&&&&&&&&&&",CI_all)
	netlist.remove(maxnet)
	print('DANG QIAN maxnode', k)
	print('DANG QIAN maxci', maxmetric)
	#print("geng xin_netlist",netlist)
	LCIRall.append(k)
	print (LCIRall)
	#file2.write(str(LCIRall)+'\n')
	removenode(netlist, maxnet, k)
	#print("geng xin_netlist2", netlist)
###BFS######
queue=[]
max_neighber = []
node_list=[]
l2=[]
def BFS(maxnet, node, visited, l, prev, c=0):
    max_nei = 0
    cnt=0
    if visited[node] == True:
        return
    visited[node]=True
    for i in maxnet[node]:
        if visited[i]==False and i not in prev and i not in queue:
            queue.append(i)
            max_nei=i
            cnt=cnt+1
    #print('&&&&&&&&&&&&queue&&&&&&&&&&&',queue)
   # print('&&&&&&&&&&&&prev&&&&&&&&&&&', prev)
    if cnt!=0:
        max_neighber.append(max_nei)
    #else:
        #max_neighber.append(node)
    if (queue!=[]):
        node1 = queue.pop(0)
       # print('node1',node1)
    #if node1 in prev:
      # node1=queue.pop(0)
        node_list.append(node1)
        #print('zuida neighbor[0]', max_neighber)
        if((max_neighber!=[])and(node1==max_neighber[0])):
            #visited[node] = True
            c=c+1
            if len(max_neighber) >1:
                k=len(max_neighber)
                while(k>1):
                    max_neighber.pop(0)
                    k=k-1
                if maxnet[node1]!=[]:
                    for kk in maxnet[node1]:
                        if visited[kk] == False and kk not in prev and kk not in queue:
                            max_neighber[:] = []
               # max_neighber.pop(0)

            else:
                max_neighber[:] = []
           # print('zuida neighbor[2]', max_neighber)
            #node_list.append(node1)
            if c==r+1:
                return
            #jia ru ci ceng jiedian
            if c==r:
                #print('erc ceng jiedian',node_list)
                for i in node_list:
                    l.append(i)
               # l.append(node_list)
                    #l.append(node1)
                queue[:]=[]
                max_neighber[:] = []
               # node_list[:] = []
                #l.remove(l[0])
                #print('lllll',l)
                node_list[:]=[]
                return
            if c<r:
                prev.append(node1)
                node_list[:]=[]
                #print('==========',prev)
                #prev[:] = []
                if visited[node1] == True:
                    node1 = queue.pop(0)
                BFS(maxnet, node1, visited, l, prev, c)
        else:
            prev.append(node1)
            BFS(maxnet, node1, visited, l,prev, c)
###BFS######

def removenode(netlist, maxnet, key):
	l = maxnet[key]
	del maxnet[key]
	d = {key:[key]}
	netlist.append(d)
	for i in l:
		maxnet[i].remove(key)
	visited = []
	for i in range(maxcount):
		visited.append(False)
	for node in l:
		d = {}
		DFS(maxnet, node, visited, d)
		if d != {}:
			netlist.append(d)
def DFS(maxnet, node, visited, d):
	if visited[node] == True:
		return
	visited[node] = True
	for i in maxnet[node]:
		if visited[i] == False:
			DFS(maxnet, i, visited, d)
	d[node] = maxnet[node]
	del maxnet[node]
def nettolist(dict):
	l = []
	for n in dict:
		l.append(n)
	l.sort()
	return l	
def listtostr(list):
	s = "Size: "
	s += str(len(list))
	s += " members: "
	list.sort()
	s += str(list)	
	return s
def customprint(s):
	if len(s) > 80:
		for i in range(79, 0, -1):
			if s[i] == ' ':
				break
		print(s[0:i])
		print("    ",end='')
		print(s[i+1:])
	else:
		print(s)
def printnets(netlist, node, metric):
	l = []
	print("Removing node:",node,"with metric:",metric)
	#LCIRall.append(node)
	#print ("********************",LCIRall)
	for d in netlist:
		l.append(nettolist(d))
	l.sort()
	for t in l:
		s = listtostr(t)
		customprint(s)
def count_influence(c):
	netlist = [adjlist]
	l = nettolist(netlist[0])
	s = listtostr(l)
	customprint(s)
	for i in range(c):
		node, metric = changelist1(netlist)
		printnets(netlist, node, metric)

def collective_influence(c):
	netlist = [adjlist]
	###print(netlist)
	l = nettolist(netlist[0])
	#print(l)
	s = listtostr(l)
	#print(s)
	customprint(s)
	for i in range(c):
         changelist2(netlist)
adjlist = {}
r = 3
LCIRall=[]
LCI_list_sum=[]
LCI_list_sum_rank=[]
readfile("F:\sjx\diandui.txt")
loops=3
print("%%%%%%%%%%%%%",adjlist)
maxcount = len(adjlist)+1
#visited=[]
#for i in range(maxcount):
	#visited.append(False)
import time
start = time.time()
t1=time.time() - start
print ("*****t1*****",t1)
collective_influence(loops)
t2=time.time() - start
print("*****t2*****",t2)
print("*****t2-t1*****",t2-t1)
file2.write("yunxingtime"+str(t2-t1)+'\n')
#print (SS_TOP50)
#file2.write(str(SS_TOP50)+'\n')
file2.write(str(LCIRall)+'\n')