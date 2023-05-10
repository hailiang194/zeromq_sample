import zmq
import time
import sys

import http.server
import socketserver
import threading

def test(port):
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()

PORT = 8000


port = "5556"

if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port) # make sure port is number

context = zmq.Context()
socket = context.socket(zmq.REP)
print("Binding from tcp://*:%s" % port)
socket.bind("tcp://*:%s" % port)

t = threading.Thread(target=test, args=(PORT,))
t.start()

while True:
    message = str(socket.recv().decode())
    print("Received request: " + message)
    time.sleep(1)
    socket.send_string("Hello friend from " + message)