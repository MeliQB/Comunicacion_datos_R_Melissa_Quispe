class Server:
    def __init__(self, cpu_capacity, memory_capacity):
        """
        Inicializa un objeto Server con las capacidades de CPU y memoria especificadas.
        También inicializa la carga de trabajo actual a 0.
        """
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.current_load = 0

    def scale_up(self, additional_cpu, additional_memory):
        """
        Aumenta la capacidad de CPU y memoria del servidor.
        """
        self.cpu_capacity += additional_cpu
        self.memory_capacity += additional_memory

class ServerCluster:
    def __init__(self):
        """
        Inicializa un objeto ServerCluster con una lista vacía de servidores.
        """
        self.servers = []

    def add_server(self, server):
        """
        Agrega un nuevo servidor al clúster.
        """
        self.servers.append(server)

    def remove_server(self):
        """
        Elimina el último servidor del clúster, si hay alguno.
        """
        if self.servers:
            self.servers.pop()

    def distribute_load(self, load):
        """
        Distribuye una carga de trabajo entre los servidores del clúster.
        Si no hay servidores en el clúster, se imprime un mensaje de advertencia.
        De lo contrario, la carga se divide uniformemente entre todos los servidores.
        """
        if not self.servers:
            print("No servers available.")
            return
        load_per_server = load / len(self.servers)
        for server in self.servers:
            server.current_load += load_per_server

# Ejemplo de uso
server1 = Server(cpu_capacity=4, memory_capacity=8)
server2 = Server(cpu_capacity=4, memory_capacity=8)
cluster = ServerCluster()
cluster.add_server(server1)
cluster.add_server(server2)
cluster.distribute_load(10)

print(f"Server 1 CPU: {server1.cpu_capacity}, Memory: {server1.memory_capacity}, Current Load: {server1.current_load}")
print(f"Server 2 CPU: {server2.cpu_capacity}, Memory: {server2.memory_capacity}, Current Load: {server2.current_load}")
