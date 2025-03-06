import socket
import json

# Server settings
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Same port as the server

# Sample JSON data
json_data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Serialize the JSON data
serialized_data = json.dumps(json_data)

# Create the client socket (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send the serialized JSON data to the server
client_socket.sendall(serialized_data.encode())

# Receive the response from the server
response = client_socket.recv(1024)

# Print the response
print(f'Server response: {response.decode()}')

# Close the client socket
client_socket.close()
