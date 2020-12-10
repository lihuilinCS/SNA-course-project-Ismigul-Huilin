import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', type=str)
parser.add_argument('-o', type=str)
args=parser.parse_args()


data_files = os.listdir(args.d)

for file in data_files:
    if file.endswith(".mtx"):
        print(file)
        os.system("./bin/BatchLayout -input " + args.d + "/" + file + " -output " + args.o + " -algo 4")