from ipaddress import ip_address
import re
import requests
import socket

# Get the hostname
hostname = socket.gethostname()

# Get the attempt
file = open("/var/log/auth.log", "r")
data = file.read()
attempt = data.count("authentication failure")

SERVER = "http://127.0.0.1:5000/"

response = requests.put(SERVER + hostname, {"hostname":hostname,"attempt":attempt})