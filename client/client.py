import requests
import socket
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# The Monitoring server
SERVER = "http://172.26.10.171:5000/host/"

# Get the hostname
hostname = socket.gethostname()

def on_modified(event):
    # Get the attempt
    file = open("/var/log/auth.log", "r")
    data = file.read()
    attempt = data.count("authentication failure")
    requests.put(SERVER + hostname, {"hostname":hostname,"attempt":attempt})
    print("modified")

if __name__ == "__main__":
    path = "/var/log/auth.log"
    event_handler = FileSystemEventHandler()
    event_handler.on_modified=on_modified
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print("Monitoring")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

