import socket, threading

def recv_msg(s):
    while True:
        try:
            msg = s.recv(1024).decode()
            if not msg: break
            print(f"\n{msg}")
        except:
            print("Error in receiving message.")
            break

s = socket.socket()
s.connect(("127.0.0.1", 12345))
threading.Thread(target=recv_msg, args=(s,), daemon=True).start()
while True:
    msg = input()
    if msg.lower() == "exit": break
    s.send(msg.encode())
s.close()