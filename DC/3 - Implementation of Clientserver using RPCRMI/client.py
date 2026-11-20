import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    print("Addition: 5 + 3 =", proxy.add(5, 3))
    print("Subtraction: 10 - 3 =", proxy.subtract(10, 3))
    print("Multiplication: 2 * 2 =", proxy.multiply(2, 2))
    print("Division: 2 / 2 =", proxy.divide(2, 2))