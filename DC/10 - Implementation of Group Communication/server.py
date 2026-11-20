import socket, threading

clients = []

def send_all(msg, sender):
    for c in clients[:]:
        if c != sender:
            try: c.send(msg.encode())
            except: c.close(); clients.remove(c)

def handle(c):
    while True:
        try:
            msg = c.recv(1024).decode()
            if not msg: break
            print(f"Received: {msg}")
            send_all(msg, c)
        except: break
    c.close()
    if c in clients: clients.remove(c)

s = socket.socket()
s.bind(("0.0.0.0", 12345))
s.listen()
print("Server started. waiting for clients...")
while True:
    c, addr = s.accept()
    print(f"Client {addr} connected.")
    clients.append(c)
    threading.Thread(target=handle, args=(c,), daemon=True).start()