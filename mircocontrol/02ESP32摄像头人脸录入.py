import socket
import numpy as np
import cv2
import time
from PIL import Image
import io

# 创建UDP服务器
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 注意 这里是服务器的IP和端口  不是客户端的
addr = ('192.168.176.254', 8080)
s.bind(addr)
end_data = b'Frame Over'
temp_data = b''
num = 1
while True:
    data, addr = s.recvfrom(1430)
    if data == end_data:  # 判断这一帧数据是不是结束语句 UDP会发送单独的一个包   但是TCP不会单独发送
        receive_data = np.frombuffer(temp_data, dtype='uint8')  # 将获取到的字符流数据转换成1维数组
        r_img = cv2.imdecode(receive_data, cv2.IMREAD_COLOR)  # 将数组解码成图像
        try:
            np.array(r_img)
            r_img = r_img.reshape(480, 640, 3)
            cv2.imshow('server_frame', r_img)
        except Exception as e:
            print(e)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):
            cv2.imwrite("E://code//esp32//5.7//lesson7//image//" + str(num) + ".jim" + ".jpg", r_img)
            print("success to save" + str(num) + ".jpg")
            print("--------")
            num += 1
        elif k == ord(' '):
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        temp_data = b''  # 清空数据 便于下一章照片使用
    else:
        temp_data = temp_data + data  # 不是结束的包 讲数据添加进temp_data
cv2.destroyAllWindows()
