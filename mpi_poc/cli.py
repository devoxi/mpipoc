#!/usr/bin/env python3.4

from mpi4py import MPI
import multiprocessing as mp
from fork import start_fork
from master import start_master


def main():
    # Init
    print("[CLI] Init")

    # Preparing multiprocessing
    mpctx = mp.get_context('fork')
    stats_queue = mp.Queue()

    # Launching fork
    fork_process = mpctx.Process(target=start_fork, args=(stats_queue,))
    fork_process.start()

    # Launching MPI Master process
    mpimaster_process = mpctx.Process(target=start_master, args=(stats_queue,))
    mpimaster_process.start()

    # Joins
    print("[CLI] Joining")
    mpimaster_process.join()
    fork_process.join()

    # End
    print("[CLI] OK")


if __name__ == '__main__':
    main()