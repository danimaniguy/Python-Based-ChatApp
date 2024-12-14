# Python-Based Chat Application

A lightweight, Python-based chat application with a simple GUI built using Tkinter. This application allows you to chat from anywhere in the world by connecting a client to a server hosted on your device.



Features

Cross-Device Connectivity: Connect to the chat server from any device on the same network.

User-Friendly GUI: Designed with simplicity in mind using Tkinter.

Customizable: Easily adapt and extend the application to fit your needs.

Getting Started

Prerequisites

Ensure you have the following installed:

Python

A code editor like VS Code or PyCharm.

Installation

Download the Project: Download the repository as a ZIP file and extract it.

Set Up the Files:

Open the extracted folder in your preferred code editor.

Save the server.py and client.py scripts in a directory on your PC.

How to Use

Step 1: Start the Server

Navigate to the server.py script.

Right-click the file while holding Shift and select "Copy as Path".

Open a Command Prompt window.

Run the following command:

python "<server_script_path>"

Example:

python "C:\Users\DanTheMan\server.py"

This will host the server on the device.



Step 2: Find Your IP Address

Open another Command Prompt window.

Type ipconfig and press Enter.

Locate the IPv4 address in the output and copy it to your clipboard.



Step 3: Configure the Client

Open the client.py file in your code editor.

Replace the default IP address in the script with your copied IPv4 address.

Example:

server_ip = "192.168.1.100"  # Replace this with your IPv4 address



Save the changes.

Step 4: Connect the Client

Run the client.py script, and it will connect to the hosted server. Now you’re ready to chat!

Optional

You can compile the client.py script into an executable (.exe) or incorporate it into a website for broader usability.

Contributions

Feel free to fork this repository and submit pull requests to enhance the functionality or fix issues.

