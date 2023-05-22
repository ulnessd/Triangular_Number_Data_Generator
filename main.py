import pandas as pd
from sympy import *
import networkx as nx
import numpy as np
import time
import keyboard

def pcdinfo(n):
    oddeven = int(simplify(n).is_odd)
    facint = factorint(n)
    upf=list(facint.keys())
    upfnum=len(upf)
    pp=list(facint.values())
    pfnum=0
    for j in range(len(upf)):
        pfnum=pfnum+pp[j]
    mpp=max(pp)
    prg=max(upf)-min(upf)
    gaps=[]
    if len(upf)==1:
        gaps.append(0)
    else:
        for j in range(1,len(upf)):
            gaps.append(upf[j]-upf[j-1])
    mgap=max(gaps)
    return [oddeven,pfnum,upfnum,mpp,prg,mgap,totient(n),divisor_count(n),divisor_sigma(n),mobius(n)]


def make_trig_sat_set(modnum):
    tset={0}
    for i in range(modnum):
        tset.add(int(i * (i + 1) / 2) % modnum)
    s=len(tset)/modnum
    return s


def make_trig_seq(modnum):
    tlist=[]
    for i in range(modnum):
        tlist.append(int(i * (i + 1) / 2) % modnum)
    return tlist


def make_trig_full_set(modnum):
    i = np.arange(modnum)
    tlist = ((i * (i + 1)) // 2) % modnum
    return set(tlist)

def make_graph(m):
    G = nx.Graph()
    vertlist=make_trig_full_set(m)
    tpath=make_trig_seq(m)
    edgelist=[]
    for i in range(len(tpath)-1):
        edgelist.append(tuple(sorted((tpath[i],tpath[i+1]))))
    edgelist=list(set(edgelist))
    G.add_nodes_from(vertlist)
    G.add_edges_from(edgelist)
    return G


def count_triangles(grp):
    triangle_count = 0
    for node in grp.nodes():
        # Get the neighbors of the current node as a list
        neighbors = list(grp.neighbors(node))
        # Iterate through all pairs of neighbors
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                # Check if the two neighbors are connected
                if grp.has_edge(neighbors[i], neighbors[j]):
                    # If so, increment the triangle count
                    triangle_count += 1
    triangle_count = triangle_count // 3
    return triangle_count


def R(m):
    tlist = []
    ss = []
    for i in range(m):
        tlist.append(int(i * (i + 1) / 2) % m)
        ss.append(i ** 2 % m)
    tls=set(tlist)
    sss=set(ss)
    qrl=len(sss)
    qnrl=m-qrl
    Q=qnrl/qrl
    iis=tls.intersection(sss)
    sds=tls-sss
    QT=len(sds)/len(iis)
    return QT/Q


def fastreducer(m):
    test = make_trig_full_set(m)
    l1 = len(test)
    bad = set()
    for e1 in test:
        if e1 not in bad and e1 not in [0, 1]:
            for e2 in test:
                if (e1 * e2 % m) not in test:
                    bad.add(e2)
                    bad.add(e1)

    l2 = len(bad)
    return (l1-l2)/l1




df = pd.DataFrame(columns=['mod m', 'parity', 'prime factors', 'unique prime factors',
                           'max prime powers', 'range prime factors', 'max gap', 'totient',
                           'divisors', 'sum of divisors', 'mobius', 'saturation', 'R', 'Mr',
                           'graph density', 'triangles', 'transitivity', 'cliques'])

# Save the column headers to the CSV file first
m=1656

if m == 3:
    df.to_csv('temp.csv', index=False)

start_time = time.time()
while True:
    stucture = pcdinfo(m)
    grp = make_graph(m)
    data = {
        'mod m': m,  # Data for append should be scalar
        'parity': stucture[0],
        'prime factors': stucture[1],
        'unique prime factors': stucture[2],
        'max prime powers': stucture[3],
        'range prime factors': stucture[4],
        'max gap': stucture[5],
        'totient': stucture[6],
        'divisors': stucture[7],
        'sum of divisors': stucture[8],
        'mobius': stucture[9],
        'saturation': make_trig_sat_set(m),
        'R': R(m),
        'Mr': fastreducer(m),
        'graph density': nx.density(grp),
        'triangles': count_triangles(grp),
        'transitivity': nx.transitivity(grp),
        'cliques': max(len(c) for c in nx.find_cliques(grp))
    }
    # Convert the dictionary to a dataframe and transpose it
    df_temp = pd.DataFrame(data, index=[0])
    # Append the data to the CSV file
    df_temp.to_csv('temp.csv', mode='a', header=False, index=False)

    if m % 1000 == 0:
        print("m = " + str(m) + " completed")
        print("This time interval: ", time.time() - start_time, "s")
        start_time = time.time()

    # Check if 'q' has been pressed
    if keyboard.is_pressed('q'):
        print("Stopping at m = ", m)
        break

    m += 1
