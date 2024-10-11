# CSC 249 – Project 2 – Simple VPN Anisha Jain 

## Overview of Application

The application consists of a client and a VPN. The purpose of the VPN is to hide the identity of the client, acting as a middle man between the client and server. The client takes in a message that it wants to send to a server, specified by an IP and port, as well as the VPN's ip and port. The client will send an encoded message to the VPN and then wait for its reply. The VPN will listen on its port and receive the client message, then decode the message and send it to the specified server. If the VPN is unable to connect to the server, then it will send a message that the VPN was unable to connect. 

## Client->VPN Server Message Format
The client will take in the `message`, `server_IP`, and `server_port` as arguments. It will then join each of these arguments together as a string separated by the delimiter ":". This is what it will look like: `message:server_ip:server_port`

## VPN Server->Client Message Format 
The VPN server will receive a `message` from the server that is the intended final destination of the client. It will send that message unadulterated to the client. It will just look like `message`. Alternatively, if the VPN is unable to connect to the server, then it will send a message to the client that the VPN was unable to connect. 


## Example Output

Echo server output. 

1. Client trace: 

client starting - connecting to VPN at IP 127.0.0.1 and port 55554

connection established, sending message 'Hello, world:127.0.0.1:65432'

message sent, waiting for reply

Received response: 'Hello, world' [12 bytes]

client is done!

2. VPN trace: 

VPN starting - listening for connections at IP 127.0.0.1 and port 55554

Connected established with ('127.0.0.1', 58850)

Received client message

Decoded client message: Hello, world, for server at IP 127.0.0.1 and port 65432

connection with server established, sending request 'Hello, world'

message sent, waiting for reply

sending result message'b'Hello, world'' back to client

VPN is done!


3. Server trace: 

server starting - listening for connections at IP 127.0.0.1 and port 65432

Connected established with ('127.0.0.1', 58782)

Received client message: 'b'Hello, world'' [12 bytes]

echoing 'b'Hello, world'' back to client

server is done!


## a description of how the network layers are interacting when you run your server, VPN server, and client
The client, VPN, and server are all on the same IP address. We can think of the application layer and the transport layer preparing the data as necessary. But when it hits the networking layer, then it sees that it has the same IP address. So instead of touching the link layer it goes back up the stack because the data has arrived at its destination. 


## Acknowledgments

No help was needed for this project 

