import socket
import os

HOST = '127.0.0.1'
PORT = 5000

UPLOAD_FOLDER = 'C:\Users\patte\Documents\5 sem lab\CN\TCP-based-distributed-file-storage-system-updated_branch\python_server\uploads'

os.makedirs(UPLOAD_FOLDER,exist_ok = True)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}: {PORT}...")

while True:
  client_socket, addr = server_socket.accept()
  print(f"Connected by {addr}")
  filename = client_socket.recv(1024).decode()
  filepath = os.path.join(UPLOAD_FOLDER,filename)
  print(f"Receiving file: {filename}")
  with open(filepath,'wb') as f:
    while True:
      data = client_socket.recv(4096)
      if not data:
        break
      f.write(data)

  print(f"File saved as {filepath}")
  client_socket.close()
  