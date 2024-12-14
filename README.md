# Python-Based Chat Application

A lightweight, Python-based chat application with a simple GUI built using Tkinter. This application allows you to chat from anywhere in the world by connecting a client to a server hosted on your device.

![image](https://github.com/user-attachments/assets/fc24bc52-59d3-4734-b34c-6808114805c1)

# Features

Cross-Device Connectivity: Connect to the chat server from any device on the same network.

User-Friendly GUI: Designed with simplicity in mind using Tkinter.

Customizable: Easily adapt and extend the application to fit your needs.

# Getting Started

- Prerequisites: 

  Ensure you have the following installed:

    Python

    A code editor like VS Code or PyCharm. (VS Code is better)

# Installation

- Download the Project: Download the repository as a ZIP file and extract it.

- Set Up the Files:

    Open the extracted folder in your preferred code editor.

    Save the server.py and client.py scripts in a directory on your PC. (preferably in your user directory)

# How to Use

- Step 1: Start the Server

    Navigate to the server.py script.

    Right-click the file while holding Shift and select "Copy as Path".

    Open a Command Prompt window.

    Run the following command:

    python "<server_script_path>"

    Output:
  
    ![image](https://github.com/user-attachments/assets/4a250a7b-98c6-4337-a1e2-acb5046baecf)

- Step 2: Find Your IP Address 

    Open another Command Prompt window.

    Type ipconfig and press Enter.

    Locate the IPv4 address in the output and copy it to your clipboard.
  
    ![image](https://github.com/user-attachments/assets/f93e828d-8471-4f5b-a86b-ef431928b483)


- Step 3: Configure the Client

    Open the client.py file in your code editor.

    Replace the default IP address in the script with your copied IPv4 address.

    ![image](https://github.com/user-attachments/assets/4a8f4185-22bd-4e8a-a8d1-6c70f3972dfa)

    Save the changes.

- Step 4: Connect the Client

    Run the client.py script, and it will connect to the hosted server. Now you’re ready to chat!

    Server Will Output:
  
    ![image](https://github.com/user-attachments/assets/668869fc-572f-4282-92ed-db916b636411)

# Optional

You can compile the client.py script into an executable (.exe) or incorporate it into a website for broader usability.

# Contributions

Feel free to fork this repository and submit pull requests to enhance the functionality or fix issues.

