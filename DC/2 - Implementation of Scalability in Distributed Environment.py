import random
import time
from queue import Queue
from threading import Lock, Thread

print_lock = Lock()


class WorkerNode:
    def __init__(self, wid):
        self.id = wid

    def process_task(self, task):
        with print_lock:
            print(f"Worker {self.id} processing: {task}")
        time.sleep(random.uniform(1, 3))
        with print_lock:
            print(f"Worker {self.id} finished: {task}")


def worker(q, wid):
    node = WorkerNode(wid)
    while (task := q.get()) is not None:
        try:
            node.process_task(task)
        finally:
            q.task_done()
    q.task_done()


def main():
    q, n = Queue(), 2
    threads = [Thread(target=worker, args=(q, i), daemon=True) for i in range(n)]
    for t in threads:
        t.start()
    for i in range(5):
        q.put(f"Task {i}")
    q.join()
    for _ in range(n):
        q.put(None)
    for t in threads:
        t.join()
    print("All tasks processed.")


if __name__ == "__main__":
    main()