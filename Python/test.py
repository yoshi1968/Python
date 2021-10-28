#Begin Portion 1#
import random
class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}
    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load
    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for connection_load in self.connections.values():
            total += connection_load
        return total
    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
#End Portion 1#

server = Server()
server.add_connection("192.168.1.1")

print(server.load())

