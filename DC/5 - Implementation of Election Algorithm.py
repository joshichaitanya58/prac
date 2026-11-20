class Pro:
    def __init__(self, pid):
        self.id = pid
        self.act = True


class RingElection:
    def __init__(self, n=5):
        self.n = n
        self.process = [Pro(i) for i in range(n)]
        print(f"No of processes {n}")

    def max_active_idx(self):
        return max((i for i, p in enumerate(self.process) if p.act), key=lambda i: self.process[i].id)

    def election(self, init_id=2):
        fail_idx = self.max_active_idx()
        print(f"Process no {self.process[fail_idx].id} fails")
        self.process[fail_idx].act = False

        print(f"Election Initiated by {init_id}")
        old, newer = init_id, (init_id + 1) % self.n
        while newer != init_id:
            if self.process[newer].act:
                print(f"Process {self.process[old].id} pass Election({self.process[old].id}) to{self.process[newer].id}")
                old = newer
            newer = (newer + 1) % self.n

        coord = self.process[self.max_active_idx()].id
        print(f"Process {coord} becomes coordinator")

        old, newer = coord, (coord + 1) % self.n
        while newer != coord:
            if self.process[newer].act:
                print(f"Process {self.process[old].id} pass Coordinator({coord}) message to process {self.process[newer].id}")
                old = newer
            newer = (newer + 1) % self.n
        print("End Of Election ")


if __name__ == "__main__":
    RingElection(5).election(2)