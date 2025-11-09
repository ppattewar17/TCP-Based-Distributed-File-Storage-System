TCP-Based Distributed File Storage System

A distributed file storage solution built using TCP sockets. This system allows multiple clients to upload, download, and manage files across a cluster of servers, communicating via TCP.
It consists of a Python-based server component and a Node.js/EJS-based web UI client.

🚀 Features

File upload, download and management across networked nodes

Client-server architecture using TCP for reliable data transfer

Web UI (Node.js + EJS) to interact with the storage system

Simple authentication (basic) for accessing the system

Modular structure: you can extend it to add replication, partitioning, or metadata services

📁 Project Structure
/python_server           # Python server handling TCP file operations  
/node_ui                 # Web UI for user interaction (Node.js + EJS)  
/auth.db                 # Authentication/credentials database  


python_server/ — Implementation of the core storage server(s) listening for TCP connections from clients.

node_ui/ — Web interface: upload files, list stored files, download files, view status.

auth.db — A simple database (SQLite or similar) for user credentials (username/password) for UI access.

Other supporting files (scripts, helpers) may be included.

🛠️ Prerequisites

Python 3.x installed

Node.js (and npm) installed

A supported OS (Linux, macOS, or Windows)

Basic dependencies (see below for installation)

🔧 Installation & Setup
For the Python server

Navigate into python_server/

Install necessary Python packages:

pip install -r requirements.txt


Configure the server (e.g., set port, storage folder) — adjust configs in the server script as needed.

Run the server:

python server.py

For the Web UI

Navigate into node_ui/

Install dependencies:

npm install


Configure connection settings (TCP server host/port) in the UI config.

Start the UI:

npm start


or

node app.js


Open your browser and go to http://localhost:3000 (or configured port) to use the UI.

🧩 Usage

Use the web UI to login (using credentials in auth.db)

Upload files to the distributed storage

Browse the list of stored files, and download or delete them as needed

On the server side: files are distributed/stored via TCP, so you can monitor logs for transfer activity
