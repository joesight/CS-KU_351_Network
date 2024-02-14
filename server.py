import os, socket, time

host = input("Host Name: ")
sock_session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock_session.connect((host, 6969))
    print("Connected Successful!")
except:
    print("Can't connect to server")
    exit(0)

file_name = sock_session.recv(1024).decode()
print("File Name: ", file_name)
file_size = sock_session.recv(1024).decode()
print("File Size: ", file_size)

file = open("./store_file/" + file_name, "wb")

check = 0
start = time.time()
while check <= int(file_size):
    data = sock_session.recv(1024)
    if not (data):
        break
    file.write(data)
    check += len(data)
end = time.time()

print("Total Time Transfered  = ", end - start)
        
file.close()
sock_session.close()