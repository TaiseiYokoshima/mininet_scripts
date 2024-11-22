from mininet.topo import Topo

class mytopo (Topo):

    def build(self):
        lefthost = self.addHost("h1")
        righthost = self.addHost("h2")
        leftswitch = self.addSwitch("s3")
        rightswitch = self.addSwitch("s4")

        self.addLink(lefthost, lef


