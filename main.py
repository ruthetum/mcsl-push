import os
import time
import datetime
import scapy.layers.l2
from dotenv import load_dotenv
load_dotenv(verbose=False)

MCSL_IP_ADDRESS = os.getenv('MCSL') # Router Address Ex. 111.111.111.1/24
iphone = os.getenv('iphone')    # IPhone MAC Address
ipad = os.getenv('ipad')        # IPad MAC Address
net = MCSL_IP_ADDRESS

# done = True
while True:
    ack, nak = scapy.layers.l2.arping(net, timeout=1, verbose=False)
    for sent, recevied in ack.res:
        ip = recevied.psrc # 응답한 기기의 IP address
        mac = recevied.hwsrc # 응답한 기기의 MAC address
        # if done:
        #     print('%s\t%s' %(ip, mac))
        if mac == iphone:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(now + ' : iphone 접속')
        elif mac == ipad:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(now + ' : ipad 접속')
    # done = False
    time.sleep(5)
