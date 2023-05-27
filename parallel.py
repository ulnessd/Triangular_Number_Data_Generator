import os
import pandas as pd
from sympy import *
import networkx as nx
import numpy as np
import time
import concurrent.futures


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

def compute(m):
    structure = pcdinfo(m)  # Added line
    grp = make_graph(m)  # Added line
    data = {
        'mod m': m,
        'parity': structure[0],
        'prime factors': structure[1],
        'unique prime factors': structure[2],
        'max prime powers': structure[3],
        'range prime factors': structure[4],
        'max gap': structure[5],
        'totient': structure[6],
        'divisors': structure[7],
        'sum of divisors': structure[8],
        'mobius': structure[9],
        'saturation': make_trig_sat_set(m),
        'R': R(m),
        'Mr': fastreducer(m),
        'graph density': nx.density(grp),
        'triangles': count_triangles(grp),
        'transitivity': nx.transitivity(grp),
        'cliques': max(len(c) for c in nx.find_cliques(grp))
    }

    # Create DataFrame and write to a unique CSV file
    df_temp = pd.DataFrame(data, index=[0])
    df_temp.to_csv(f'temp_{m}.csv', index=False)
    return m  # Return m to show progress in the executor.map loop


if __name__ == '__main__':
    for i in range(100):
        num_workers = 10
        start_m=500000 + i*1000
        end_m=500000 + 1000 +i*1000
        dummycounter=0
        start_time = time.time()
    
        with concurrent.futures.ProcessPoolExecutor(num_workers) as executor:
            # Print m to show progress
            for m in executor.map(compute, range(start_m, end_m)):
                dummycounter+=1
    
    
        # Combine all individual CSV files into one
        df = pd.concat([pd.read_csv(f'temp_{m}.csv') for m in range(start_m, end_m)], ignore_index=True)
    
        # Write the combined DataFrame to a new CSV file
        df.to_csv('combined'+str(start_m)+'TO'+str(end_m-1)+'.csv', index=False)
        print('combined'+str(start_m)+'TO'+str(end_m-1)+'.csv file dumped')
    
        # Optional: delete the individual CSV files
        for m in range(start_m, end_m):
            os.remove(f'temp_{m}.csv')
        print("This time interval: ", time.time() - start_time, "s")
