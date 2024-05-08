import socket
import numpy as np
import cv2
import time
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('192.168.13.254', 8080) #ip地址填入自己电脑的IP地址，端口与ESP32摄像头发送数据的端口保持一致
s.bind(addr)
end_data = b'Frame Over'
temp_data = b''
while True:
    data, addr= s.recvfrom(1435)
    if data == end_data: # 判断这一帧数据是不是结束语句 UDP会发送单独的一个包   但是TCP不会单独发送
        receive_data = np.frombuffer(temp_data, dtype='uint8')  # 将获取到的字符流数据转换成1维数组
        r_img = cv2.imdecode(receive_data, cv2.IMREAD_COLOR)  # 将数组解码成图像
        try:
            np.array(r_img)
            r_img = r_img.reshape(480, 640, 3)
            cv2.imshow('server_frame', r_img)
        except Exception as e:
            print(e)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        print("接收到的数据包：" + str(len(temp_data)))  # 显示该张照片数据大小
        temp_data = b''  # 清空数据 便于下一章照片使用
    else:
        temp_data = temp_data + data  # 不是结束的包 讲数据添加进temp_data
