import zmq

# ZeroMQ Context
# Define the socket using the "Context"
context = zmq.Context()

# This socket is for receiving all the messages.
#RECEIVE 
receiverSocket = context.socket(zmq.SUB)
receiverSocket.setsockopt_string(zmq.SUBSCRIBE, "")
receiverSocket.bind("tcp://127.0.0.1:1234")

# This socket is for publishing/sending all the messages.
#SEND
senderSocket = context.socket(zmq.PUB)
senderSocket.bind("tcp://127.0.0.1:7777")

print("Server started...")

while True:
    #Handling messages received from client
    chatMsgRcvd = receiverSocket.recv().decode()
    chatUserRcvd = receiverSocket.recv().decode()
    #Printing chat status on server for overall visiblity/clarity
    print("[{}]: {}".format(chatUserRcvd, chatMsgRcvd))
    #Publishing received chat/user info to clients
    senderSocket.send_string(chatMsgRcvd)
    senderSocket.send_string(chatUserRcvd)

