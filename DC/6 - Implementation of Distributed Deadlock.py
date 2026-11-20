class Resource:
    def __init__(self, name):
        self.name, self.holder = name, None


class Process:
    def __init__(self, name):
        self.name, self.held = name, []

    def request(self, res):
        if res.holder is None:
            res.holder = self
            self.held.append(res)
            print(f"{self.name} acquired {res.name}.")
        else:
            print(f"{self.name} is waiting for {res.name} held by {res.holder.name}.")


def detect_deadlock(procs):
    for p in procs:
        if len(p.held) == 2:
            print(f"Potential deadlock detected with {p.name} holding 2 resources")


if __name__ == "__main__":
    r1, r2 = Resource("R1"), Resource("R2")
    p1, p2 = Process("P1"), Process("P2")
    p1.request(r1)
    p1.request(r2)
    p2.request(r1)
    detect_deadlock([p1, p2])