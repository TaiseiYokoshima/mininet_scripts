#!/usr/bin/python3
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Controller, Node
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


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


def bin_test(net):
    commands = [
        "cd /home/mininet",
        "cd src",
        "./server",
    ]

    h1 = net.get( 'h1' )
    cmd(h1, commands)


if __name__ == '__main__':
    topo = test_network() 
    net = Mininet( topo=topo )
    net.start()
    bin_test(net)

