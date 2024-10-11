#!/usr/bin/env python3

import socket
import arguments
import argparse

# Run 'python3 VPN.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and prints the response')
parser.add_argument('--VPN_IP', help='IP address at which to host the VPN', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which to host the VPN', **arguments.vpn_port_arg)
args = parser.parse_args()

VPN_IP = args.VPN_IP  # Address to listen on
VPN_PORT = args.VPN_port  # Port to listen on (non-privileged ports are > 1023)

def parse_message(message):
    message = message.decode("utf-8")
    # Parse the application-layer header into the destination SERVER_IP, destination SERVER_PORT,
    # and message to forward to that destination
    message_arr = message.split(":")
    return message_arr[0], message_arr[1], int(message_arr[2])

### INSTRUCTIONS ###
# The VPN, like the server, must listen for connections from the client on IP address
# VPN_IP and port VPN_port. Then, once a connection is established and a message recieved,
# the VPN must parse the message to obtain the server IP address and port, and, without
# disconnecting from the client, establish a connection with the server the same way the
# client does, send the message from the client to the server, and wait for a reply.
# Upon receiving a reply from the server, it must forward the reply along its connection
# to the client. Then the VPN is free to close both connections and exit.

# The VPN server must additionally print appropriate trace messages and send back to the
# client appropriate error messages.
print("VPN starting - listening for connections at IP", VPN_IP, "and port", VPN_PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((VPN_IP, VPN_PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            print(f"Received client message")

            #decode data
            message, server_ip, server_port = parse_message(data)
            print(f"Decoded client message: {message}, for server at IP {server_ip} and port {server_port}") 

            try: 
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_2:
                    s_2.connect((server_ip, server_port))
                    print(f"connection with server established, sending request '{message}'")
                    s_2.sendall(bytes(message, 'utf-8'))
                    print("message sent, waiting for reply")
                    final_message = s_2.recv(1024)
            except: 
                final_message = bytes("there was a problem connecting to the server. ", 'utf-8')
            
            print(f"sending result message'{final_message!r}' back to client")
            conn.sendall(final_message)

print("VPN is done!")
