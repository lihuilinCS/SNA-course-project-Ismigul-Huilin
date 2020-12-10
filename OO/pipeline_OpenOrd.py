import os
import argparse
import time
import stat

parser = argparse.ArgumentParser()
parser.add_argument('-d', type=str)
args=parser.parse_args()


data_files = os.listdir(args.d)


for file in data_files:
    if file.endswith(".sim"):
        print(file)
        fin = open("recursive_layout.sh", "rt")
        fout = open("parallel/"+file[:-3]+"sh", "wt")
        for line in fin:
            if 'ROOTNAME=' in line:
                line = line.replace('yeast', file[:-4])
            fout.write(line)
        fin.close()
        fout.close()
        st = os.stat("parallel/"+file[:-3]+"sh")
        os.chmod("parallel/"+file[:-3]+"sh", st.st_mode | stat.S_IEXEC)

os.chdir("parallel") 

for file in data_files:
    if file.endswith(".sim"):
        start = time.time()
        os.system("./"+file.split(".")[0]+".sh")
        print(time.time()-start)
        
