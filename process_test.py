#!/usr/bin/python3

import subprocess
import time


server_cmd = "/home/mininet/udt/b.udt_server >> /home/mininet/udt/tmp/server.txt"

server = subprocess.Popen(server_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

time.sleep(1)
cmd = r"ss -l -p -n | grep 'b.udt_server' | grep -oP '0\.0\.0\.0:\K[0-9]+'"

result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
port = result.stdout.strip()
ip = "127.0.0.1"
client_cmd = f"/home/mininet/udt/b.udt_client {ip} {port} >> /home/mininet/udt/tmp/client.txt"

client = subprocess.Popen(client_cmd, shell=True)


server.wait()
client.wait()
