from __future__ import print_function
import sys
import copy
from operator import itemgetter
sys.setrecursionlimit(1000000)
file2 = open("C:\Users\Administrator\Desktop\out31.txt", "w+") 
def readfile(input):
    f = open(input, 'rU')
   # print(adjlist)
    for line in f:
        temp = line.split()

        #print(temp)
        var1 = int(temp[0])
        # print(var1)

        var2 = int(temp[1])
        if var1 in adjlist:
            adjlist[var1].append(var2)

        else:
            adjlist[var1] = [var2]
        if var2 in adjlist:
            adjlist[var2].append(var1)
        else:
            adjlist[var2] = [var1]
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
	#print(list)
	s += str(list)
	return s

def customprint(s):
	if len(s) > 200:
		for i in range(199, 0, -1):
			if s[i] == ' ':
				break
		##print(s[0:i])
		##print("    ",end='')
		##print(s[i+1:])
	else:
		print(s)



#width first
queue=[]
max_neighber = []
node_list=[]
l2=[]
def BFS(maxnet, node, visited, l, prev, c=0):
    max_nei = 0
    cnt=0
    if visited[node]==True:
        return
    visited[node]=True
    for i in maxnet[node]:
        if visited[i]==False and i not in prev and i not in queue:
            queue.append(i)
            max_nei=i
            cnt=cnt+1
    ###print('&&&&&&&&&&&&queue&&&&&&&&&&&',queue)
    ###print('&&&&&&&&&&&&prev&&&&&&&&&&&', prev)
    if cnt!=0:
        max_neighber.append(max_nei)
    #else:
        #max_neighber.append(node)
    if (queue!=[]):
        node1 = queue.pop(0)
     ###   print('node1',node1)
    #if node1 in prev:
      # node1=queue.pop(0)
        node_list.append(node1)
        ###print('zuida neighbor[0]', max_neighber)
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
            ###print('zuida neighbor[2]', max_neighber)
            #node_list.append(node1)
            if c==r+1:
                return
            #join in this loop node
            if c==r:
                ###print('erc ceng jiedian',node_list)
                for i in node_list:
                    l.append(i)
               # l.append(node_list)
                    #l.append(node1)
                queue[:]=[]
                max_neighber[:] = []
               # node_list[:] = []
                #l.remove(l[0])
                ###print('lllll',l)
                node_list[:]=[]
                return
            if c<r:
                prev.append(node1)
                node_list[:]=[]
                ###print('==========',prev)
                #prev[:] = []
                if visited[node1] == True:
                    node1 = queue.pop(0)
                BFS(maxnet, node1, visited, l, prev, c)
        else:
            prev.append(node1)
            BFS(maxnet, node1, visited, l,prev, c)


def changelist2(netlist):
    max=0
    for d in netlist:
        if len(d)>max:
            max=len(d)
            maxnet=d
    maxmetric=0
    sum=0
    a=0
    b=0
    CI_list={}
    CI_all=[]
    LCI_list={}
    prev=[]
    #print("%%%%%%%each maxnet%%%%%%%%%%%",maxnet)
    l = []
    print("*********************************",len(maxnet))
    for key in maxnet:
        visited = []    
        #print(range(maxcount))

        for i in range(maxcount):
            visited.append(False)
        #DFS2(maxnet, key, visited, l)
        BFS(maxnet, key, visited, l,prev)
        #  print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        prev[:] = []
        if key==2: 
            print('--------L-value------', l)
        for i in l:
            sum += len(maxnet[i]) - 1
        metric = (len(maxnet[key]) - 1) * sum
        l[:] = []
        CI_list={key:metric}
        #print('DANG QIAN ci',CI_list)
        CI_all.append(CI_list)
        sum=0

    #print("&&&&&&&&&&&&&&CI&&&&&&&&&&&&&&&&",CI_all)
    for key in maxnet:
        LCI_list[key]=0
        for dd in CI_all:
            if key in dd and dd[key]==0:
                LCI_list[key] = -1
        #if CI_list.get(key)==0:
            #LCI_list[key]=-1
        if LCI_list[key]!=-1:
            #print("$$$$$$$$$$$$$$$$$$$$",CI_all)
            #for lx in CI_all:
            for nei in maxnet[key]:

                count=0
                for dd in CI_all:
                    if key in dd:
                        a=dd[key]
                    if nei in dd:
                        b=dd[nei]
                if b>a:

                    count=count+1
                    LCI_list[key]=count
    cnt=0
    #netlist.remove(maxnet)
    LCIR_list=[]
    LCIR_list2=[]
    Key_CI=0
    ###print("*****maxnet********",maxnet)
    LCIR2 = {}.fromkeys(['node_id', 'node_ci'])
    for key in maxnet:
        if LCI_list[key]==0:
            cnt=cnt+1
            for dd in CI_all:
                if key in dd:
                    Key_CI=dd[key]
            LCIR={'node_id':key,'node_ci':Key_CI}
            #LCIR = {key:Key_CI}
            LCIR_list.append(LCIR)
            LCI_list_sum.append(LCIR)
            #print("*****LCI_list_sum********", LCI_list_sum)
    #file2.write(str(LCI_list_sum)+'\n')
    #file2.flush()
    LCI_list_sum_rank=sorted(LCI_list_sum, key=itemgetter('node_ci'), reverse=True)
    #for i in LCI_list_sum_rank:
        #file2.write(str(i.get('node_id'))+'\n')
        #file2.flush()
            #LCIR_list2.append(LCIR2)
    ###print("*****LCIR_list********", LCIR_list)
    for kk in range(0,cnt):
        ke=LCIR_list[kk].get('node_id')
        ###print(ke)
        key = ke
        l = maxnet[key]
        #d = {key: [key]}
        #netlist.append(d)
        ###print("&&&&&netlist1&&&&&&&&&", netlist)
        ###print("&&&&&L&&&&&&&&&", l)
        for i in l:
            maxnet[i].remove(key)

        ###print("removed nodes", key)
        del netlist[0][key]
    ###print("&&&&&&&this loop find nodes&&&&&&&&&&&",cnt,"s")
    ###print(netlist)
    ###print("&&&&&&&&&&this loop removed node CI", LCIR_list)
    ranked_LCIR=sorted(LCIR_list, key=itemgetter('node_ci'), reverse=True)
    ###print("=====this loop ranked nodes and CI=====",ranked_LCIR)
    #S_len=len(LCI_list_sum_rank)
    return LCI_list_sum_rank


adjlist = {}
r = 3
LCIR_all=[]
LCI_list_sum=[]
LCI_list_sum_rank=[]
path=[r'c:\Users\Administrator\Desktop\sjxwork\lcir-ci\Email_linju.txt',r'c:\Users\Administrator\Desktop\sjxwork\lcir-ci\facebookone.txt',r'c:\Users\Administrator\Desktop\sjxwork\lcir-ci\Hamster.txt',r'c:\Users\Administrator\Desktop\sjxwork\lcir-ci\p2p_diandui.txt',r'c:\Users\Administrator\Desktop\sjxwork\lcir-ci\Political blogs.txt',r'c:\Users\Administrator\Desktop\sjxwork\lcir-ci\USA airportsN.txt',r'c:\Users\Administrator\Desktop\sjxwork\lcir-ci\Wiki_vote.txt',r'c:\Users\Administrator\Desktop\sjxwork\lcir-ci\YeastpB.txt']
for i in path:
    print (i)
    readfile(i)
    netlist = [adjlist]
        ###print(netlist)
    l = nettolist(netlist[0])
        #print(l)
    s = listtostr(l)
        #print(s)
    customprint(s)
    maxcount = len(adjlist)+1
    SS=changelist2(netlist)
    sum_len=len(SS)

    loops=1
    #print(adjlist)
    import time
    start = time.time()
    t1=time.time() - start
    print ("*****t1*****",t1)
    #temp_LEN=collective_influence(loops)
    while(int(sum_len*0.3)<50):
        loops=loops+1
        Temp=changelist2(netlist)
        Temp_LEN=len(Temp)
        sum_len=sum_len+Temp_LEN
    t2=time.time() - start
    print("*****t2*****",t2)
    print("*****t2-t1*****",t2-t1)
    file2.write("yunxingtime"+str(t2-t1)+'\n')
    print (loops)
    file2.write(str(loops)+'\n')
    print (sum_len)
    file2.write(str(sum_len)+'\n')
    SS_TOP50=Temp[0:50]
    print (SS_TOP50)
    file2.write(str(SS_TOP50)+'\n')
#file2.write(str(LCIR_list_sum)+'\n')
#LCI_list_sum_rank=sorted(LCI_list_sum, key=itemgetter('node_ci'), reverse=True)
#for i in LCI_list_sum_rank:
#    file1.write(str(i.get('node_id'))+'\n')
        
