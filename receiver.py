# Server script (run on the receiving computer)
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(1)

print("Waiting for a connection...")
client, addr = server.accept()
print("Connection from", addr) # When it receives a connection

#message_log_file = "message_log.txt" # File for storing messages

while True:
    data = client.recv(1024)
    if not data:
        break

    received_message = data.decode('utf-8') # Receive message
    print("Received:", received_message)

    # # Append the received message to the log file
    # with open(message_log_file, 'a') as log_file:
    #     log_file.write(received_message + '\n')

# Close the client connection
client.close()
