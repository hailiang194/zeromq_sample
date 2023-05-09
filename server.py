import zmq
import time
import sys

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port) # make sure port is number

context = zmq.Context()
socket = context.socket(zmq.REP)
print("Binding from tcp://*:%s" % port)
socket.bind("tcp://*:%s" % port)

while True:
    message = str(socket.recv().decode())
    print("Received request: " + message)
    time.sleep(1)
    socket.send_string("Hello friend from " + message)