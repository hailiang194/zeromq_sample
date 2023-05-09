import zmq
import sys
import os

host = os.getenv("ZEROMQ_HOST", "localhost")
port = os.getenv("ZEROMQ_PORT", "5556")

context = zmq.Context()
url = "tcp://%s:%s" % (host, port)
print("Connecting to %s..." % url)
socket = context.socket(zmq.REQ)
socket.connect(url)
while True:
    socket.send_string("Hello")
    message = socket.recv()
    print("Replied: %s" % message)