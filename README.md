# Code 401 Python 

## TCP Echo Server

### Specifications
* Create a repository called sockets with a directory called src

* Create a branch on your sockets repository called echo

* Within src, create three Python files: client.py, server.py, test_server.py

In server.py:

* Construct a socket server that will accumulate a message from some client and return that exact message back to the client.
* When the server first starts, a message should be printed to the console of the format "--- Starting server on port 8888 at 12:43:08 29/01/2018 ---"
* When the server is stopped, the user shouldn't see any error message.
* When the server is stopped, a message should be printed to the console of the format --- Stopping server on port 8888 at 12:43:39 29/01/2018 ---
* Whenever a message is received by the server, the server prints to the console a log of that message. It doesn't have to match this exactly, but it should be something like: [12:43:10 29/01/2018] Echoed: 'Hello, world!'

In client.py:

* Construct a socket client that will accept a message from the command line and send it to a server
* You may need to review the docs for accepting command line arguments when running a script.
* When the server sends a response back, the client should accumulate the response and print it to the console.
* Both your client and your server should be able to accept a message of any length, containing any unicode characters. Specifically it should be able to accept messages of lengths that are multiples of the buffer length of either the client or server.

For any of the date-time logs, you'll need to use the datetime library