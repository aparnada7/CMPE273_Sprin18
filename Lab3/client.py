import zmq, threading, sys

# ZeroMQ Context
context = zmq.Context()
initiator = sys.argv[1]

# This socket is for publishing/sending all the messages.
#SEND
senderSocket = context.socket(zmq.PUB)
senderSocket.connect("tcp://127.0.0.1:1234")

# This socket is for receiving all the messages.
#RECEIVE
receiverSocket = context.socket(zmq.SUB)
receiverSocket.connect("tcp://127.0.0.1:7777")
receiverSocket.setsockopt_string(zmq.SUBSCRIBE, "")

print("User[{}] Connected to the chat server.".format(initiator))


#Function to handle incoming messages, published by server to clients.
def chat_handler():
    while True:
        chatMsg = receiverSocket.recv().decode()
        lastChatUser = receiverSocket.recv().decode()
        # Duplicating initiator's own message in chat window is not required.
        # Hence, pass if initiator is same as lastChatUser.
        if lastChatUser == initiator:
            pass
        else:
            print("\n[{}]: {} \n[{}] > ".format(lastChatUser, chatMsg, initiator),  end="")
            
            
#Defining thread so that message receiving/chat handling on client side is continuous        
def thread():
    thread = threading.Thread(target=chat_handler)
    thread.start()


thread()
while True:
    inputChatMsg = input("[{}] > ".format(initiator))
    #Send chat message and initiator info to server
    senderSocket.send(inputChatMsg.encode())
    senderSocket.send(initiator.encode())
