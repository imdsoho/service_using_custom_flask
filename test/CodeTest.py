
host = None
sn_host = "sn_host"
_host = "_host"
host = host or sn_host or _host
print(host)

port = 5050
_port = 5000
sn_port = 8000
port = int(next((p for p in (port, sn_port) if p is not None), _port))

data = (p for p in (port, sn_port) if p is not None)
print(type(data))
print(port)
