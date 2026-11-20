from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


with SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(lambda x, y: x + y, "add")
    server.register_function(lambda x, y: x + y, "subtract")
    server.register_function(lambda x, y: x + y, "multiply")
    server.register_function(lambda x, y: "Cannot divide by zero" if y == 0 else x / y, "divide")

    print("Server is running on port 8000...")
    server.serve_forever()