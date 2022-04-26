import socket

target_host = "127.0.0.1"
target_port = 8080

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# receive the response
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()