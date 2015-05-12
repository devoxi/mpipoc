def start_fork(sq):
    # Init
    print("[FORK] Init")

    # Looping
    while True:
        item = sq.get(block=True, timeout=None)
        print("[FORK] Received: "+item['type'])
        if item['type'] == "exit":
            break

    print("[FORK] Done!")