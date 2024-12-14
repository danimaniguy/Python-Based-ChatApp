import socket
import threading
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

HOST = '192.168.0.12' #change this to the public ip of the host
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            elif message == 'CLEAR_CHAT':
                for widget in chat_area_frame.winfo_children():
                    widget.destroy()
            else:
                display_message(message)
        except:
            print("Dawg Server Isnt Runnin")
            client.close()
            break

def send_message(event=None):
    message = input_box.get()
    if message.strip():
        if message == '/clear':
            client.send('/clear'.encode('utf-8'))
        else:
            client.send(f'{nickname}: {message}'.encode('utf-8'))
    input_box.delete(0, tk.END)

def display_message(message):
    message_frame = tk.Frame(chat_area_frame, bg="#444", bd=2, relief=tk.GROOVE)
    message_frame.pack(anchor="w", fill="x", pady=5, padx=10)

    message_label = tk.Label(
        message_frame, 
        text=message, 
        bg="#444", 
        fg="white", 
        font=("Arial", 14),
        wraplength=600, 
        justify="left"
    )
    message_label.pack(padx=10, pady=5)

    chat_canvas.yview_moveto(1.0) 

def set_nickname():
    global nickname
    nickname = nickname_entry.get()
    if nickname.strip():
        nickname_entry.config(state='disabled')
        nickname_button.config(state='disabled')
        nickname_frame.pack_forget()
        client.connect((HOST, PORT))
        threading.Thread(target=receive, daemon=True).start()

root = tk.Tk()
root.title("Chat App")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#333333", foreground="white", borderwidth=0)
style.configure("TEntry", fieldbackground="#333333", foreground="white")
style.configure("TLabel", background="#1e1e1e", foreground="white")
style.configure("Vertical.TScrollbar", troughcolor="#333333", background="#555555", gripcount=0, borderwidth=0)

nickname_frame = tk.Frame(root, bg="#1e1e1e")
nickname_frame.pack(pady=20)

nickname_label = tk.Label(nickname_frame, text="Enter Your Name:", font=("Arial", 14), fg="white", bg="#1e1e1e")
nickname_label.pack(side=tk.LEFT, padx=10)

nickname_entry = ttk.Entry(nickname_frame, font=("Arial", 12))
nickname_entry.pack(side=tk.LEFT, padx=5)

nickname_button = ttk.Button(nickname_frame, text="Submit", command=set_nickname)
nickname_button.pack(side=tk.LEFT, padx=5)

chat_frame = tk.Frame(root, bg="#2e2e2e")
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_canvas = tk.Canvas(chat_frame, bg="#2e2e2e", highlightthickness=0)
chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

chat_scrollbar = ttk.Scrollbar(chat_frame, orient=tk.VERTICAL, command=chat_canvas.yview)
chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_canvas.configure(yscrollcommand=chat_scrollbar.set)

chat_area_frame = tk.Frame(chat_canvas, bg="#2e2e2e")
chat_canvas.create_window((0, 0), window=chat_area_frame, anchor="nw")

chat_area_frame.bind("<Configure>", lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all")))

input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(fill=tk.X, padx=10, pady=5)

input_box = ttk.Entry(input_frame, font=("Arial", 12))
input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
input_box.bind("<Return>", send_message)

send_button = ttk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5)

title_label = tk.Label(root, text="/clear to clear the chat", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
title_label.pack(pady=5)

root.mainloop()
