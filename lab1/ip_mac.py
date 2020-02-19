import socket
host=socket.gethostname()
ip=socket.gethostbyname(host)
print("ip address=",ip)


import uuid 

print (hex(uuid.getnode())) 

