import socket
import json

# Server settings
HOST = '127.0.0.1'
PORT = 65432

# Create the server socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f'Server is listening on {HOST}:{PORT}')

# These variables are used in later exercise
response_body = 'Data received successfully'
response_headers = f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body)}\r\n\r\n'
response_http = response_headers + response_body


try:
    # Accept the incoming connection
    # This blocks (waits) for a new connection and continues only after a connection is received
    conn, addr = server_socket.accept()

    with conn:
        print(f'Connected by {addr}')
        while True:
            # Receive data from the client
            data = conn.recv(1024)

            # If no data is received, break the inner loop
            if not data:
                break
            
            conn.sendall(response_http.encode())
            
            # conn.sendall("David".encode())
            '''
            # Decode and load the JSON data
            json_data = json.loads(data.decode())

            # Process the JSON data
            print(f'Received JSON data: {json_data}')

            # Send a response back to the client
            response = 'Data received successfully'
            conn.sendall(response.encode()) 
            '''

except Exception as e:
    print("Problem with the connection:")
    print(e)

server_socket.close()
