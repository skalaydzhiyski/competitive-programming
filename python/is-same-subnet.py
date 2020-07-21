#!/usr/bin/python3

def is_same_subnet(ips):
  ip1, mask1 = ips[0]
  ip2, mask2 = ips[1]
  subnet1 = '.'.join(
      [str(int(n) & int(m))
        for n, m in zip(ip1.split('.'), mask1.split('.'))])
  subnet2 = '.'.join(
      [str(int(n) & int(m))
        for n, m in zip(ip2.split('.'), mask2.split('.'))])
  print("net1: {}".format(subnet1))
  print("net2: {}".format(subnet2))
  return subnet1 == subnet2

if __name__ == "__main__":
  ips1 = [('192.168.1.68','255.255.255.0'), ('192.168.1.89', '255.255.255.0')] 
  ips2 = [('192.168.1.68','255.0.0.0'), ('192.168.1.89', '255.255.255.0')] 
  print(ips1)
  print(is_same_subnet(ips1))
  print()
  print(ips2)
  print(is_same_subnet(ips2))

