from mininet.topo import Topo
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import CPULimitedHost


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=5):
        switch = self.addSwitch('s1')
        host = self.addHost('h1')
        self.addLink(host, switch, bw=1024 )
        self.addLink(host, switch, bw=1024 )
        self.addLink(host, switch, bw=1024 )
        self.addLink(host, switch, bw=1024 )
        # Python's range(N) generates 0..N-1
        for h in range(1,n):
            host = self.addHost('h%s' % (h + 1))
	    self.addLink(host, switch, bw=1024 )
            self.addLink(host, switch, bw=1024 )
        

   
def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=5)
    net = Mininet(topo = topo, link=TCLink)
    net.start()
    
    h1=net.get('h1')
    h1.cmd('ifconfig h1-eth0 10.0.0.50 netmask 255.0.0.0')
    h1.cmd('ifconfig h1-eth1 172.168.0.50 netmask 255.255.0.0')
    h1.cmd('ifconfig h1-eth2 10.0.0.51 netmask 255.0.0.0')
    h1.cmd('ifconfig h1-eth3 172.168.0.51 netmask 255.255.0.0') 

    h1.cmdPrint('ip rule add from 10.0.0.50 table 1')
    h1.cmdPrint('ip route add 10.0.0.0/8 dev h1-eth0 scope link table 1')
    h1.cmdPrint('ip route add default via 10.0.0.50 dev h1-eth0 table 1')
    h1.cmdPrint('ip route add default scope global nexthop via 10.0.0.50 dev h1-eth0')

    h1.cmdPrint('ip rule add from 172.168.0.50 table 2')
    h1.cmdPrint('ip route add 172.168.0.0/16 dev h1-eth1 scope link table 2')
    h1.cmdPrint('ip route add default via 172.168.0.50 dev h1-eth1 table 2')
    h1.cmdPrint('ip route add default scope global nexthop via 172.168.0.50 dev h1-eth1')
  
    h1.cmdPrint('ip rule add from 10.0.0.51 table 11')
    h1.cmdPrint('ip route add 10.0.0.0/8 dev h1-eth2 scope link table 11')
    h1.cmdPrint('ip route add default via 10.0.0.50 dev h1-eth2 table 11')
    h1.cmdPrint('ip route add default scope global nexthop via 10.0.0.50 dev h1-eth2')

    h1.cmdPrint('ip rule add from 172.168.0.51 table 12')
    h1.cmdPrint('ip route add 172.168.0.0/16 dev h1-eth3 scope link table 12')
    h1.cmdPrint('ip route add default via 172.168.0.50 dev h1-eth3 table 12')
    h1.cmdPrint('ip route add default scope global nexthop via 172.168.0.50 dev h1-eth3')
    


    h2=net.get('h2')
    h2.cmd('ifconfig h2-eth0 10.0.0.100 netmask 255.0.0.0')
    h2.cmd('ifconfig h2-eth1 172.168.0.100 netmask 255.255.0.0')

    h2.cmd('ifconfig h2-eth0:1 10.0.0.200 netmask 255.0.0.0')
    h2.cmd('ifconfig h2-eth0:2 172.168.0.200 netmask 255.255.0.0')
    h2.cmd('ifconfig h2-eth0:3 172.168.0.201 nettmask 255.255.0.0')

    h2.cmd('ifconfig h2-eth1:1 10.0.0.201 netmask 255.0.0.0')
    h2.cmd('ifconfig h2-eth1:2 172.168.0.202 netmask 255.255.0.0')
    h2.cmd('ifconfig h2-eth1:3 10.0.0.202 netmask 255.0.0.0')
   
    
    h2.cmdPrint('ip rule add from 10.0.0.100 table 3')
    h2.cmdPrint('ip route add 10.0.0.0/8 dev h2-eth0 scope link table 3')
    h2.cmdPrint('ip route add default via 10.0.0.50 dev h2-eth0 table 3')
    h2.cmdPrint('ip route add default scope global nexthop via 10.0.0.50 dev h2-eth0')

    h2.cmdPrint('ip rule add from 172.168.0.100 table 4')
    h2.cmdPrint('ip route add 172.168.0.0/16 dev h2-eth1 scope link table 4')
    h2.cmdPrint('ip route add default via 172.168.0.50 dev h2-eth1 table 4')
    h2.cmdPrint('ip route add default scope global nexthop via 172.168.0.50 dev h2-eth1')


    
    h3=net.get('h3')
    h3.cmd('ifconfig h3-eth0 10.0.0.101 netmask 255.0.0.0')
    h3.cmd('ifconfig h3-eth1 172.168.0.101 netmask 255.255.0.0') 

    h3.cmd('ifconfig h3-eth0:1 10.0.0.203 netmask 255.0.0.0')
    h3.cmd('ifconfig h3-eth0:2 172.168.0.203 netmask 255.255.0.0')
    h3.cmd('ifconfig h3-eth0:3 172.168.0.204 netmask 255.255.0.0')

    h3.cmd('ifconfig h3-eth1:1 10.0.0.204 netmask 255.0.0.0')
    h3.cmd('ifconfig h3-eth1:2 172.168.0.205 netmask 255.255.0.0')
    h3.cmd('ifconfig h3-eth1:3 10.0.0.205 netmask 255.0.0.0')
    

    h3.cmdPrint('ip rule add from 10.0.0.101 table 5')
    h3.cmdPrint('ip route add 10.0.0.0/8 dev h3-eth0 scope link table 5')
    h3.cmdPrint('ip route add default via 10.0.0.50 dev h3-eth0 table 5')
    h3.cmdPrint('ip route add default scope global nexthop via 10.0.0.50 dev h3-eth0')

    h3.cmdPrint('ip rule add from 172.168.0.101 table 6')
    h3.cmdPrint('ip route add 172.168.0.0/16 dev h3-eth1 scope link table 6')
    h3.cmdPrint('ip route add default via 172.168.0.50 dev h3-eth1 table 6')
    h3.cmdPrint('ip route add default scope global nexthop via 172.168.0.50 dev h3-eth1')
    


    h4=net.get('h4')
    h4.cmd('ifconfig h4-eth0 10.0.0.102 netmask 255.0.0.0')
    h4.cmd('ifconfig h4-eth1 172.168.0.102 netmask 255.255.0.0')

    h4.cmd('ifconfig h4-eth0:1 10.0.0.206 netmask 255.0.0.0')
    h4.cmd('ifconfig h4-eth0:2 172.168.0.206 netmask 255.255.0.0')
    h4.cmd('ifconfig h4-eth0:3 172.168.0.207 netmask 255.255.0.0')

    h4.cmd('ifconfig h4-eth1:1 10.0.0.207 netmask 255.0.0.0')
    h4.cmd('ifconfig h4-eth1:2 172.168.0.208 netmask 255.255.0.0')
    h4.cmd('ifconfig h4-eth1:3 10.0.0.208 netmask 255.0.0.0')
    

    h4.cmdPrint('ip rule add from 10.0.0.102 table 7')
    h4.cmdPrint('ip route add 10.0.0.0/8 dev h4-eth0 scope link table 7')
    h4.cmdPrint('ip route add default via 10.0.0.50 dev h4-eth0 table 7')
    h4.cmdPrint('ip route add default scope global nexthop via 10.0.0.50 dev h4-eth0')

    h4.cmdPrint('ip rule add from 172.168.0.102 table 8')
    h4.cmdPrint('ip route add 172.168.0.0/16 dev h4-eth1 scope link table 8')
    h4.cmdPrint('ip route add default via 172.168.0.50 dev h4-eth1 table 8')
    h4.cmdPrint('ip route add default scope global nexthop via 172.168.0.50 dev h4-eth1')



    h5=net.get('h5')
    h5.cmd('ifconfig h5-eth0 10.0.0.103 netmask 255.0.0.0')
    h5.cmd('ifconfig h5-eth1 172.168.0.103 netmask 255.255.0.0')

    h5.cmd('ifconfig h5-eth0:1 10.0.0.209 netmask 255.0.0.0')
    h5.cmd('ifconfig h5-eth0:2 172.168.0.210 netmask 255.255.0.0')
    h5.cmd('ifconfig h5-eth0:3 172.168.0.211 netmask 255.255.0.0')

    h5.cmd('ifconfig h5-eth1:1 10.0.0.210 netmask 255.0.0.0')
    h5.cmd('ifconfig h5-eth1:2 172.168.0.211 netmask 255.255.0.0')
    h5.cmd('ifconfig h5-eth1:3 10.0.0.211 netmask 255.0.0.0')
    

    h5.cmdPrint('ip rule add from 10.0.0.103 table 9')
    h5.cmdPrint('ip route add 10.0.0.0/8 dev h5-eth0 scope link table 9')
    h5.cmdPrint('ip route add default via 10.0.0.50 dev h5-eth0 table 9')
    h5.cmdPrint('ip route add default scope global nexthop via 10.0.0.50 dev h5-eth0')

    h5.cmdPrint('ip rule add from 172.168.0.102 table 10')
    h5.cmdPrint('ip route add 172.168.0.0/16 dev h5-eth1 scope link table 10')
    h5.cmdPrint('ip route add default via 172.168.0.50 dev h5-eth1 table 10')
    h5.cmdPrint('ip route add default scope global nexthop via 172.168.0.50 dev h5-eth1')
   
 
  

    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    #	net.pingAll()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
