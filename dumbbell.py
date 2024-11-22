from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Controller, Node
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class LinuxRouter(Node):
    "A Node with IP forwarding enabled."
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class Dumbbell(Topo):

    def build(self):
        host1 = self.addHost("h1")
        host2 = self.addHost("h2")
        host3 = self.addHost("h3")

        node1 = self.addNode("n1", cls=LinuxRouter)
        node2 = self.addNode("n2", cls=LinuxRouter)

        # node1 = self.addSwitch("s1")
        # node2 = self.addSwitch("s2")



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

def perfTest():
    "Create network and run simple performance test"
    topo = Dumbbell()
    net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink )

    # n1, n2 = net.get( 'n1', 'n2')
    # n1.cmd('sysctl net.ipv4.ip_forward=1')
    # n2.cmd('sysctl net.ipv4.ip_forward=1')
    net.start()
    # print( "Dumping host connections" )
    # dumpNodeConnections( net.hosts )
    # print( "Testing network connectivity" )
    # net.pingAll()
    print( "Testing bandwidth between h1 and h4" )
    h1, h4 = net.get( 'h1', 'h4' )
    net.iperf( (h1, h4) , port=7777)
    net.stop()

topos = { 'dumbbell': (lambda: Dumbbell()) }

if __name__ == '__main__':
    setLogLevel( 'info' )
    perfTest()



