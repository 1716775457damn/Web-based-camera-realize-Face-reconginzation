import socket
import numpy as np
import cv2
from ultralytics import YOLO
import os
print(os.getcwd())
model = YOLO('yolo11s.pt')

# 设置UDP接收
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('192.168.107.254', 8080)  # IP地址和端口
s.bind(addr)
end_data = b'Frame Over'
temp_data = b''

# 设置窗口大小
original_window_name = 'Original Frame'
detected_window_name = 'Detected Frame'
cv2.namedWindow(original_window_name, cv2.WINDOW_NORMAL)
cv2.namedWindow(detected_window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(original_window_name, 1280, 720)  # 设置原始窗口大小
cv2.resizeWindow(detected_window_name, 1280, 720)  # 设置检测窗口大小

while True:
    data, addr = s.recvfrom(65507)  # 增大缓冲区大小
    if data == end_data:
        if len(temp_data) > 0:
            receive_data = np.frombuffer(temp_data, dtype='uint8')
            r_img = cv2.imdecode(receive_data, cv2.IMREAD_COLOR)
            if r_img is not None:
                # 进行目标检测
                results = model(r_img)
                # 绘制检测结果
                detected_img = results.render()[0]

                # 显示原始画面
                cv2.imshow(original_window_name, r_img)
                # 显示检测后的画面
                cv2.imshow(detected_window_name, detected_img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("图像解码失败")
        temp_data = b''
    else:
        temp_data += data

s.close()
cv2.destroyAllWindows()
