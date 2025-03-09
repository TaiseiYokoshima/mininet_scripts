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
import os

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

def change_bandwidth(intf, bw):
    cmd = f"tc qdisc change dev {intf} root handle 1: tbf rate {bw}mbit burst 15000 latency 50ms"
    print(f"Changing {intf} bandwidth to {bw} Mbps...")
    Node("root").cmd(cmd)

def udt_test(net, stream):
    stream = "u"
    server = net.get( 'server' )
    client = net.get( 'client' )

    switch = net.get( 's1' )
    interface = switch.intfNames()[2]

    server_cmd = f"/home/mininet/udt/b.udt_server {stream}"
    server_process = server.popen(server_cmd, shell=True)
    print("server started")


    ip = server.IP()
    time.sleep(2)
    port = server.cmd(port_cmd)
    print(f"IP : {ip} | PORT : {port}")


    # client_cmd = f"/home/mininet/udt/b.udt_client {ip} {port} >> /home/mininet/udt/tmp/client.txt"
    client_cmd = f"/home/mininet/udt/b.udt_client {ip} {port} {stream}"
    client_process = client.popen(client_cmd, shell=True)
    print("client started")



    time_stamp = 0 
    sleep(3)
    change_bandwidth(interface, 100)
    time_stamp = int(time.time() * 1000)





    client_process.wait()
    server_process.wait()


    print("test finished")


    os.system(f"/home/mininet/udt/graph_data.py {time_stamp}")
    print("created graph")




    


if __name__ == '__main__':
    topo = test_network() 
    net = Mininet( topo=topo )
    net.start()

    # switch = net.get( 's1' )
    # interface = switch.intfNames()[0]


    # for i in interface:
    #     print(i)
    # CLI(net)

    udt_test(net, "d")



