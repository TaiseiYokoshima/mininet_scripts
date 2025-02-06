#!/usr/bin/python3


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Controller, Node
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


# class LinuxRouter(Node):
#     "A Node with IP forwarding enabled."
#     def config(self, **params):
#         super(LinuxRouter, self).config(**params)
#         self.cmd('sysctl net.ipv4.ip_forward=1')
#
#     def terminate(self):
#         self.cmd('sysctl net.ipv4.ip_forward=0')
#         super(LinuxRouter, self).terminate()

# node1 = self.addNode("n1", cls=LinuxRouter)
# node2 = self.addNode("n2", cls=LinuxRouter)

class Dumbbell(Topo):
    def build(self):
        host1 = self.addHost("h1")
        host2 = self.addHost("h2")
        host3 = self.addHost("h3")


        node1 = self.addSwitch("s1")
        node2 = self.addSwitch("s2")


        host4 = self.addHost("h4")
        host5 = self.addHost("h5")
        host6 = self.addHost("h6")


        self.addLink(host1, node1)
        self.addLink(host2, node1)
        self.addLink(host3, node1)


        self.addLink(host4, node2)
        self.addLink(host5, node2)
        self.addLink(host6, node2)


        self.addLink(node1, node2)

class Dumbbell_LINK_PROP_APPLIED(Topo):
    def build(self, **args):
        host1 = self.addHost("h1")
        host2 = self.addHost("h2")
        host3 = self.addHost("h3")


        node1 = self.addSwitch("s1")
        node2 = self.addSwitch("s2")


        host4 = self.addHost("h4")
        host5 = self.addHost("h5")
        host6 = self.addHost("h6")


        self.addLink(host1, node1)
        self.addLink(host2, node1)
        self.addLink(host3, node1)


        self.addLink(host4, node2)
        self.addLink(host5, node2)
        self.addLink(host6, node2)


        self.addLink(node1, node2, **args)




def perfTest(net):
    h1, h4 = net.get( 'h1', 'h4' )
    net.iperf( (h1, h4) , port=7777)

def ping_test(net):
    print("Testing connectivity between all")
    net.pingAll()

def latency(net):
    # print("test")
    h1, h4 = net.get('h1', 'h4')
    # print(h1.IP())
    # print(h4.IP())
    #
    # print("test")

    output = h1.cmd(f"ping -c 3 {h4.IP()} ")
    output = output.split("\n")
    print(output[len(output) - 2])


def compare_diff():
    #(bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
    link_opts = {}
    link_opts['bw'] = 10
    link_opts['loss'] = 10
    link_opts['delay'] = "100ms" 
    link_opts['max_queue_size'] = 100 

    topo = Dumbbell_LINK_PROP_APPLIED()
    net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink )
    net.start()
    perfTest(net)
    latency(net)
    net.stop()

    topo = Dumbbell_LINK_PROP_APPLIED(**link_opts)
    net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink )
    net.start()
    perfTest(net)
    latency(net)
    net.stop()


 
class binary_test(Topo):
    def build(self, **args):
        host1 = self.addHost("h1")


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
    # output = h1.cmd(f"ls")
    
    # output = h1.cmd(f"cd ~")
    # print(output)

    cmd(h1, commands)


if __name__ == '__main__':
    # setLogLevel( 'info' )
    topo = Dumbbell()
    net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink )
    # net.start()

    # topo = binary_test() 
    # net = Mininet( topo=topo )
    net.start()
    # bin_test(net)


    #
    # print("network initialized")
    # print("\n"*2)
    # print("_"*20)
    #
    # print("first test")
    perfTest(net)
    # net.stop()
    






    # compare_diff()
