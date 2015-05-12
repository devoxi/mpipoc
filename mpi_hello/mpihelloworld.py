#!/usr/bin/env python3.4

from mpi4py import MPI


comm = MPI.COMM_WORLD

print("Hello! I'm rank %d from %d running in total..." % (comm.rank, comm.size))

comm.Barrier()   # wait for everybody to synchronize _here_

rank = comm.Get_rank()
status = MPI.Status()

if rank == 0:
    comm.send("hello1", dest=1)
    comm.send("hello2", dest=1)
    comm.send("hello3", dest=1)
elif rank == 1:
    print(comm.recv(source=MPI.ANY_SOURCE, status=status))
    print(comm.recv(source=MPI.ANY_SOURCE, status=status))
    print(comm.recv(source=MPI.ANY_SOURCE, status=status))
