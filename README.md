<H3>INTRODUCTION</H3>
<hr>
My name is Lanpher Josh M. Garcia, a student of Gordon College BSIT - 3A.
<br>
This is a blog for my activity named Chat Application. 
<br>
It was made using Socket Programming and Tkinter for the GUI. 
<hr>
<H3>SERVER IMPLEMENTATION</H3>
<hr>
<b>import socket</b>
<br>
<b>import threading</b>
<hr>
I used these 2 libraries for my application. Socket is used for the network connection, while Threading is for performing
various tasks simultaneously.
<hr>
<b>
host = '127.0.0.1'
<br>
port = 55555
<br>
<br>
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
<br>
server.bind((host, port)) 
<br>
server.listen()
<br>
<br>
clients = []
<br>
usernames = []
</b>
<hr>
This part is for defining the data connection and to initialize the socket. I needed an IP - Address for the host and a free port
number for the server. These define the type of socket we want to use. The first one (AF_INET) indicates that we are using an internet socket rather than an unix socket. The second parameter stands for the protocol we want to use. SOCK_STREAM indicates that we are using TCP and not UDP.
<hr>
<b>
def broadcast(message):
<br>
for client in clients:
<br>
client.send(message)
</b>
<hr>
This is to define a little function that is going to help broadcasting messages and makes the code more readable. What it does is just sending a message to each client that is connected and therefore in the clients list. We will use this method in the other methods.
<hr>
<b>
def handle(client):
<br>
while True:
<br>
try:
<br>
message = client.recv(1024)
<br>
broadcast(message)
<br>
except:
<br>
index = clients.index(client)
<br>	
clients.remove(client)
<br>	
client.close()
<br>	
username = usernames[index]
<br>
broadcast('{} left!'.format(username).encode('ascii'))
<br>	
usernames.remove(nickname)
<br>	
break
</b>
<hr>
What this does is after receiving the message from the client. I broadcast it to all connected clients. So when one client sends a message, everyone else can see this message.
<hr>
<b>
def receive():
<br>
while True:
<br>
client, address = server.accept()
<br>
print("Connected with {}".format(str(address)))
<br>
<br>
client.send('NICK'.encode('ascii'))
<br>
nickname = client.recv(1024).decode('ascii')
<br>
nicknames.append(nickname)
<br>
clients.append(client)
<br>
<br>
print("Nickname is {}".format(nickname))
<br>
broadcast("{} joined!".format(nickname).encode('ascii'))
<br>
client.send('Connected to server!'.encode('ascii'))
<br>
<br>
thread = threading.Thread(target=handle, args=(client,))
<br>
thread.start()
<br>
<br>
<br>
receive()
</b>
<hr>
When we are ready to run the server, it will execute this receive function. It also starts an endless while-loop which constantly accepts new connections from clients. Once a client is connected it sends the string ‘USER’ to it, which will tell the client that its username is requested. After that it waits for a response and appends the client with the respective username to the lists. After that, it prints and broadcast this information. Finally, it starts a new thread that runs the previously implemented handling function for this particular client.
<hr>
<H3>CLIENT IMPLEMENTATION</H3>
<hr>
<b>
username = input("Choose your Username: ")
<br>
<br>
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<br>
client.connect(('127.0.0.1', 55555))
</b>
<hr>
The first steps of the client are to choose a username and to connect it to the server. It needs to know the exact address and the port at which the server is running.
<hr>
<b>
window = tk.Tk()
<br>
window.title("Chat Application")
<br>
window.resizable(0,0)
<br>
<br>
chat_frame = tk.Frame(window)
<br>
chat_frame.pack(padx=10, pady=10)
<br>
<br>
chat_box = tk.Text(chat_frame, height=20, width=50, state=tk.DISABLED)
<br>
chat_box.pack(side=tk.LEFT)
<br>
<br>
scrollbar = tk.Scrollbar(chat_frame, command=chat_box.yview)
<br>
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
<br>
chat_box.config(yscrollcommand=scrollbar.set)
<br>
<br>
input_box = tk.Entry(window, width=50)
<br>
input_box.pack(pady=10)
</b>
<hr>
This is for the implementation of Tkinter for the main GUI of the Chat Application.
<hr>
<b>
def receive():
<br>
while True:
<br>
try:
<br>
message = client.recv(1024).decode('utf-8')
<br>	
if message == 'USER':
<br>	
client.send(username.encode('utf-8'))
<br>	
else:
<br>	
date_chat(message)
<br>	
except:
<br>
print("An error occurred!")
<br>
client.close()
<br>	
break
</b>
<hr>
The is an endless while-loop. It constantly tries to receive messages and to print them onto the screen. If the message is ‘USER’ however, it doesn’t print it but it sends its username to the server. In case there are some error, it closes the connection and break the loop. 
<hr>
<b>
def write():
<br>
while True:
<br>
message = '{}: {}'.format(username, input(''))
<br>
client.send(message.encode('ascii'))
</b>
<hr>
This also runs in an endless loop which is always waiting for an input from the user. Once it gets some, it combines it with the given username and sends it to the server.
<hr>
<b>
receive_thread = threading.Thread(target=receive)
<br>
receive_thread.start()
<br>
<br>
write_thread = threading.Thread(target=write)
<br>
write_thread.start()
</b>
<hr>
Two threads to run the two functions.
<hr>
<h3>Conclusion</h3>
<hr>
This concludes my blog for my Chat Application. Have a nice day!
