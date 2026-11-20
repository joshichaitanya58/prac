class NameResolver:
    def __init__(self):
        self.records = {
            "example.com": "33.423.243.24",
            "openai.com": "12.233.32.44",
            "google.com": "54.234.678.98",
        }
        self.cache = {}

    def resolve(self, host):
        if host not in self.cache and host in self.records:
            self.cache[host] = self.records[host]
        return self.cache.get(host)


if __name__ == "__main__":
    r = NameResolver()
    for h in ["example.com", "openai.com", "google.com", "not_exist.com"]:
        ip = r.resolve(h)
        print(f"{h} ->resolves to--> {ip}" if ip else f"{h} does not exist")