
https://github.com/SciTechStrategies/OpenOrd

This cannot directly run on lab computer.

We made changes like follows:

In the ./example/recursive_layout.sh file:

```
# parallel version information
#MPI=0							# use mpiexec
#change to ==>	
MPI=1
#MPIBIN=/home/smartin/recursive_layout/bin			# mpi bin
#change to ==>	
MPIBIN=../../bin
#MPIDATA=/home/smartin/recursive_layout/datasets/yeast_gs	# mpi data 
#change to ==>	
MPIDATA=../parallel
```

Also

delete

```
  echo "Cleaning old files ..."
  rm *coord
  rm *edges
  rm *int
  rm *.full
  rm *.real
  rm *.ind
  rm *.clust
  
 ```
