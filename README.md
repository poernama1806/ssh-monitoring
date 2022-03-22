# ssh-monitoring

Prerequisite :
- The server and client is using Ubuntu 18 (and above)
- Python 3.6x (and above) installed
- The server and client accesible by the ansible server
- After clone the repository, update the inventory file (hosts file) with the target server and client IP address

Setup :

1. From the ansible server, please clone the repository :
    $ git clone https://github.com/poernama1806/ssh-monitoring.git
2. Change the directory to ssh-monitoring directory :
    $ cd ssh-monitoring
3. Run the ansible playbook with following command :
    $ ansible-playbook -i ~/hosts deployment.yml
4. Open the webpage in the browser with the server IP as the address :
    http://server_IP:5000
