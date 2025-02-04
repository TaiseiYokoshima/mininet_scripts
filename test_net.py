#!/usr/bin/python3
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost, Controller, Node
from mininet.cli import CLI


class test_network(Topo):
    def build(self, **args):
        host1 = self.addHost("h1")
        switch1 = self.addSwitch("s1")
        host2 = self.addHost("h2")
        
        args = {}
        self.addLink(host1, switch1, **args)
        self.addLink(host2, switch1, **args)


def cmd(node, cmds):
    for cmd in cmds:
        output = node.cmd(cmd)
        print(output)

def ping_test(net):
    h1 = net.get( 'h1' )
    h2 = net.get( 'h2' )

    ip = h1.IP()

    CLI(net)

    


def bin_test(net):
    commands = [
        # "mkdir -p /tmp/test_mininet/"
        "cd /home/mininet",
        "cd src",
        "./server > /tmp/server.txt &",
    ]

    h1 = net.get( 'h1' )

    ip = h1.IP()

    h2 = net.get( 'h2' )


    print("server ip is " + ip)



    cmd(h1, commands)

    print("ran server")

    commands2 = [
        "cd /home/mininet",
        "cd src",
        f"./client {ip} > /tmp/client.txt" 
    ]


    cmd(h2, commands2)

    print("ran client")






def rust_bin(net):
    commands = [
        "cd /home/mininet",
        "mkdir -p /home/mininet/test"
    ]

    h1 = net.get( 'h1' )
    ip = h1.IP()
    h2 = net.get( 'h2' )


    cmd(h1, commands)
    cmd(h2, commands)

    # print("ran server")

    server = [
        "./server_bin > /home/mininet/test/server.txt &",
    ]

    client = [
        f"./client_bin {ip} >  /home/mininet/test/client.txt",
    ]




    cmd(h1, server)
    cmd(h2, client)

    # print("ran """  """client")





if __name__ == '__main__':
    topo = test_network() 
    net = Mininet( topo=topo )
    net.start()
    # ping_test(net)
    # bin_test(net)
    rust_bin(net)

