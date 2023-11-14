import socket
import threading
import tkinter as tk

# Choosing Username
username = input("Choose your Username: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Create a Tkinter window
window = tk.Tk()
window.title("Chat Application")

# Frame to hold the chat area
chat_frame = tk.Frame(window)
chat_frame.pack(padx=10, pady=10)

# Text widget for displaying the chat
chat_box = tk.Text(chat_frame, height=20, width=50, state=tk.DISABLED)
chat_box.pack(side=tk.LEFT)

# Scrollbar for the chat box
scrollbar = tk.Scrollbar(chat_frame, command=chat_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_box.config(yscrollcommand=scrollbar.set)

# Entry widget for typing messages
input_box = tk.Entry(window, width=50)
input_box.pack(pady=10)

# Function to send messages
def send_message(event=None):
    message = input_box.get().strip()
    if message:
        formatted_message = '{}: {}'.format(username, message)
        client.send(formatted_message.encode('utf-8'))
        input_box.delete(0, tk.END)

# Button to send messages
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Event binding to Enter key
window.bind('<Return>', send_message)

# Function to update the chat box with new messages
def update_chat(message):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, message + '\n')
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)  # Scroll to the bottom to show the latest message

# Listening to Server and Sending Username
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK', send Username
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(username.encode('utf-8'))
            else:
                # Insert message into the chat box
                update_chat(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start the Tkinter main loop
window.mainloop()

