from mpi4py import MPI
import sys
import time

count_bs = 2


def start_master(sq):
    # Init
    global count_bs
    print("[MASTER] Init")
    config = {}
    config['var1'] = "Hello"
    config['var2'] = 42

    # Spawn workers
    mpi_info = MPI.Info.Create()
    #mpi_info.Set("add-host", "localhost,host2,host3")
    comm = MPI.COMM_SELF.Spawn(sys.executable, args=["slave.py", str(config)], maxprocs=count_bs, info=mpi_info)

    # Printing debugs
    print("[MASTER] Rank: "+str(comm.Get_rank()))
    print("[MASTER] Size: "+str(comm.Get_size()))
    print("[MASTER] Remote Size: "+str(comm.Get_remote_size()))
    print("[MASTER] comm_name: "+comm.Get_name())
    print("[MASTER] is_inter : "+str(comm.Is_inter()))
    print("[MASTER] is_intra : "+str(comm.Is_intra()))

    # Sending messages
    status = MPI.Status()
    for i in range(0, count_bs):
        print("[MASTER] Loop number: "+str(i))
        msg = "lala"+str(i)
        comm.send(obj=msg, dest=i)
        print("[MASTER] Sent : \""+msg+"\" to "+str(i))
        msg = "huhuhuhu"+str(i)
        comm.send(obj=msg, dest=i)
        print("[MASTER] Sent : \""+msg+"\" to "+str(i))

    # Receiving messages
    for i in range(0, count_bs):
        print("[MASTER] Loop number: "+str(i))
        msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
        print("[MASTER] Received : \""+msg+"\" from "+str(status.Get_source()))
        msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
        print("[MASTER] Received : \""+msg+"\" from "+str(status.Get_source()))

    msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
    print("[MASTER] Received : \""+msg+"\" from "+str(status.Get_source()))
    msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
    print("[MASTER] Received : \""+msg+"\" from "+str(status.Get_source()))
    msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
    print("[MASTER] Received : \""+msg+"\" from "+str(status.Get_source()))

    # Shutdown
    time.sleep(5)
    print("[MASTER] Sending exit msg to fork")
    item = {}
    item['type'] = "exit"
    sq.put(item)
    comm.Disconnect()
    print("[MASTER] Disconnected")
