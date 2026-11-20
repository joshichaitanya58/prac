class RoundBinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    def add_server(self, server):
        self.servers.append(server)

    def remove_server(self, server):
        self.servers.remove(server)
        self.index %= len(self.servers)


if __name__ == "__main__":
    lb = RoundBinLoadBalancer(input("Enter the server names: ").split(","))
    for i in range(11):
        print(f"Request {i + 1} is handled by {lb.get_next_server()}")



# Output : 
# Enter the server names: server 1, server 2, server 3
# Request 1 is handled by server 1
# Request 2 is handled by  server 2
# Request 3 is handled by  server 3
# Request 4 is handled by server 1
# Request 5 is handled by  server 2
# Request 6 is handled by  server 3
# Request 7 is handled by server 1
# Request 8 is handled by  server 2
# Request 9 is handled by  server 3
# Request 10 is handled by server 1
# Request 11 is handled by  server 2