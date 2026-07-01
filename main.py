from entities.server import Server

print("=" * 60)
print("SKEBA")
print("=" * 60)

server = Server()

server.setup()

print()

print("Protocol :", server.protocol)
print("Version  :", server.version)
print("Hash     :", server.hash_algorithm)
print("Security :", server.security_level)

print()

print("Server Ready :", server.initialized)