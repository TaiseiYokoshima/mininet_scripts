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

# def change_bandwidth(intf, bw):
#     cmd = f"tc qdisc change dev {intf} root handle 1: tbf rate {bw}mbit burst 15000 latency 50ms"
#     print(f"Changing {intf} bandwidth to {bw} Mbps...")
#     Node("root").cmd(cmd)


def change_bandwidth(intf, bw):
    print(f"Changing {intf} bandwidth to {bw} Mbps (OVS)...")
    Node("root").cmd(f"ovs-vsctl set Interface {intf} ingress_policing_rate={bw * 1000}")
    Node("root").cmd(f"ovs-vsctl set Interface {intf} ingress_policing_burst=1500")


def udt_test(net, stream):
    stream = "u"
    bandwidth = 10000
    server = net.get( 'server' )
    client = net.get( 'client' )

    switch = net.get( 's1' )

    if0 = switch.intfNames()[0]
    if1 = switch.intfNames()[1]
    if2 = switch.intfNames()[2]



    # change_bandwidth(if0, bandwidth)
    # change_bandwidth(if1, bandwidth)
    # change_bandwidth(if2, bandwidth)

    time_stamp = None


    # CLI(net)







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
    sleep(2)
    change_bandwidth(if2, 500)
    time_stamp = int(time.time() * 1000)





    client_process.wait()
    server_process.wait()


    print("test finished")


    if time_stamp is None:
        time_stamp = ""


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



