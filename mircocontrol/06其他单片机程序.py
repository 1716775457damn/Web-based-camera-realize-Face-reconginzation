#此处要离线运行，需要把它保存到主板上并取名为main.py,这样设备通电之后就会自动运行该程序
import socket
import network
import time
from machine import Pin

led = Pin(4,Pin.OUT)


#连接wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    #wlan.connect('CKTN', '18900744765')#办公室局域网
    wlan.connect('ovo', 'twx20051')#手机热点
    
    while not wlan.isconnected():
        pass
print('网络配置:', wlan.ifconfig())

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
s.bind((wlan.ifconfig()[0],9090))# 连接wifi后将获取到的ip地址进行绑定
data,IP = s.recvfrom(1024) #接收客户端消息和IP地址
print(data,IP)

while True:
    data,IP = s.recvfrom(1024)
    print(data)
    if data == b'3':
        led.value(1)
    elif data == b'4':
        led.value(0)



