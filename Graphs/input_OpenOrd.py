import networkx as nx
import os
import stat
import argparse
from scipy.io import mmread,mminfo

parser = argparse.ArgumentParser()
parser.add_argument('-d', type=str)
parser.add_argument('-t', type=str)
args=parser.parse_args()

def mtx2sim(file):
    graph = mmread(args.d+"/"+file)
    G = nx.Graph()
    for i in range(mminfo(args.d+"/"+file)[0]):
        G.add_node(i)
    for i,j in zip(*graph.nonzero()):
        if i > j:
            G.add_edge(i, j)
    with open(args.t+"/"+file.split(".")[0]+".sim", "w") as fh:
        for e in G.edges():
            fh.write(str(e[0])+"\t"+str(e[1]))
            fh.write("\t1\n")

def to_mtx(filename):
    if filename == "web-BerkStan.txt":
        G = nx.read_edgelist(args.d+"/"+filename,create_using=nx.DiGraph)
        G = G.to_undirected()
    else:
        G = nx.read_edgelist(args.d+"/"+filename)
    
    with open(args.t+"/"+filename.split(".")[0]+".mtx", "w") as fh:
        fh.write("%%MatrixMarket matrix coordinate pattern symmetric\n")
        nr_n = str(G.number_of_nodes()+1)
        nr_e = str(G.number_of_edges())
        fh.write(nr_n+" "+nr_n+" "+nr_e+"\n")
        for e in G.edges():
            fh.write(str(int(e[0])+1)+"\t"+str(int(e[1])+1)+"\n")

data_files = os.listdir(args.d)


for file in data_files:
    print(file)
    if file[-3:] == "mtx":
        mtx2sim(file)
    if file[-3:] == "txt" or file[-5:] =="edges":
        to_mtx(file)
        mtx2sim(file.split(".")[0]+".mtx")
    st = os.stat(args.t+"/"+file.split(".")[0]+".sim")
    os.chmod(args.t+"/"+file.split(".")[0]+".sim", st.st_mode | stat.S_IEXEC)