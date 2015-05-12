#!/usr/bin/env python3.4

from mpi4py import MPI
import time
import random
import sys
import ast

def start_slave():
    # Init
    print("[SLAVE] Init")
    random.seed(42)

    # Connecting to parent
    try:
        comm = MPI.Comm.Get_parent()
        rank = comm.Get_rank()
        size = comm.Get_size()
    except:
        raise ValueError('Could not connect to parent')
        exit()

    # Init OK
    print("[SLAVE"+str(rank)+"] Init OK (comm_name: "+comm.Get_name()+" / rank: "+str(rank)+" / size: "+str(size)+")")
    print("[SLAVE"+str(rank)+"] is_inter : "+str(comm.Is_inter()))
    print("[SLAVE"+str(rank)+"] is_intra : "+str(comm.Is_intra()))
    status = MPI.Status()
    msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
    print("[SLAVE"+str(rank)+"] Slave "+str(rank)+" received "+msg+" from "+str(status.Get_source()))
    msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
    print("[SLAVE"+str(rank)+"] Slave "+str(rank)+" received "+msg+" from "+str(status.Get_source()))

    # Do something
    print("[SLAVE"+str(rank)+"] Start working...")
    time.sleep(int(random.random()*10))
    msg = "Hello I am number "+str(rank)
    comm.send(obj=msg, dest=0)
    comm.send("Second message", dest=0)
    comm.send("3rd message", dest=0)
    comm.send("4th message", dest=0)
    comm.send("5th message", dest=0)
    print("[SLAVE"+str(rank)+"] Done!")

    # test
    comm2 = MPI.COMM_WORLD
    print("[SLAVE"+str(rank)+"] COMM_WORLD (comm_name: "+comm2.Get_name()+" / rank: "+str(comm2.Get_rank())+" / size: "+str(comm2.Get_size())+")")
    print("[SLAVE"+str(rank)+"] is_inter : "+str(comm2.Is_inter()))
    print("[SLAVE"+str(rank)+"] is_intra : "+str(comm2.Is_intra()))

    # Shutdown
    comm.Disconnect()
    print("[SLAVE"+str(rank)+"] Disconnected")


if __name__ == '__main__':
    print(ast.literal_eval(sys.argv[1]))
    print(type(ast.literal_eval(sys.argv[1])))
    start_slave()