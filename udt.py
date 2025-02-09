#!/usr/bin/python3
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import dumpNodeConnections, sleep
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost, Controller, Node
from mininet.cli import CLI


port_cmd =  ' ss -l -p -n | grep "b.udt_server" | grep -oP \'0\\.0\\.0\\.0:\\K[0-9]+\' ' 

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

    CLI(net)

    return
    server_commands = [
        "cd /home/mininet/udt",
        "./b.udt_server > /tmp/server.txt &",
    ]



    server = net.get( 'server' )
    client = net.get( 'client' )
    cmd(server, server_commands)

    ip = server.IP()

    sleep(1)

    port = server.cmd(port_cmd)
    print(f"IP : {ip} | PORT : {port}")


    client_commands = [
        "cd /home/mininet/udt",
        f"./b.udt_client {ip} {port} > /tmp/client.txt" 
    ]


    cmd(client, client_commands)

if __name__ == '__main__':
    print("starting test")
    topo = test_network() 
    net = Mininet( topo=topo )
    net.start()
    udt_test(net)



