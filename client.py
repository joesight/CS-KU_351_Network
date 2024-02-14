import os, socket, time

sock_session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_session.bind((socket.gethostname(), 6969))
sock_session.listen(3)
print("Host Name: ", sock_session.getsockname())

client, addr = sock_session.accept()

file_name = input("File Name: ")
file_size = os.path.getsize(file_name)

client.send(file_name.encode())
client.send(str(file_size).encode())
print("File Size: ", file_size)

file = open(file_name, "rb")

check = 0
start = time.time()
while check <= int(file_size):
    data = file.read(1024)
    if not (data):
        break
    client.sendall(data)
    check += len(data)
end = time.time()
        
print("Total Time Transfered  = ", end - start)

file.close()
sock_session.close()