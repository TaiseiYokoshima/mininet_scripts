#!/usr/bin/python3
from sys import stderr, stdout
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import dumpNodeConnections, sleep
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost, Controller, Node
from mininet.cli import CLI

import threading
import time

port_cmd =  ' ss -l -p -n | grep "b.udt_server" | grep -oP \'0\\.0\\.0\\.0:\\K[0-9]+\' ' 

def thread_engine(node, cmd_str, name):
    return threading.Thread(target=lambda : node.cmd(cmd_str), name=name )

class test_network(Topo):
    def build(self, **args):
        server = self.addHost("server")
        switch1 = self.addSwitch("s1")
        client = self.addHost("client")
        
        args = {}
        self.addLink(server, switch1, **args)
        self.addLink(client, switch1, **args)


def cmd(node, cmds):
    for cmd in cmds:
        output = node.cmd(cmd)
        print(output)


def udt_test(net):
    server = net.get( 'server' )
    client = net.get( 'client' )

    server_cmd = "/home/mininet/udt/b.udt_server >> /home/mininet/udt/tmp/server.txt"
    server_process = server.popen(server_cmd, shell=True)
    ip = server.IP()
    time.sleep(2)
    port = server.cmd(port_cmd)
    print(f"IP : {ip} | PORT : {port}")


    # client_cmd = f"/home/mininet/udt/b.udt_client {ip} {port} >> /home/mininet/udt/tmp/client.txt"
    client_cmd = f"/home/mininet/udt/client.bash {ip} {port}"
    client_process = client.popen(str(client_cmd), shell=True)



    client_process.wait()
    server_process.wait()
    


if __name__ == '__main__':
    print("starting test")
    topo = test_network() 
    net = Mininet( topo=topo )
    net.start()
    udt_test(net)



