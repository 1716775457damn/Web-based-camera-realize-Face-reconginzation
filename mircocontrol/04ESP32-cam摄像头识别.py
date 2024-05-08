import cv2
import socket
import io
import numpy as np
import os
from PIL import Image
# coding=utf-8
import urllib
import urllib.request
import hashlib
import time

aa = 0

#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('E://code//esp32//5.7//lesson7//trainer//trainer.yml')
names=[]

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
s.bind(("192.168.13.254",8080)) #办公室局域网

#准备识别的图片
def face_detect_demo(img):
    global aa
    face = ""
    try:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度
        face_detector = cv2.CascadeClassifier('E://opencv//sources//data//haarcascades//haarcascade_frontalface_alt2.xml')
        face=face_detector.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(300,300))
    except Exception as e:
        print(e)
    if len(face) == 0:
        pass
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)
        # 人脸识别
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        #print('标签id:',ids,'置信评分：', confidence)
        if confidence > 75:
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            print("识别失败")
        else:
            cv2.putText(img,str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            print("识别成功")
    cv2.imshow('server_frame', img)
    aa += 1

def name():
    path = 'E://code//esp32//5.7//lesson7//image//'
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
       name = str(os.path.split(imagePath)[1].split('.',2)[1])
       names.append(name)


end_data = b'Frame Over'
temp_data = b''
name()
while True:
    data, addr = s.recvfrom(1435)
    if data == end_data:  # 判断这一帧数据是不是结束语句 UDP会发送单独的一个包   但是TCP不会单独发送
        receive_data = np.frombuffer(temp_data, dtype='uint8')  # 将获取到的字符流数据转换成1维数组
        r_img = cv2.imdecode(receive_data, cv2.IMREAD_COLOR)  # 将数组解码成图像
        try:
            np.array(r_img)
            r_img = r_img.reshape(480, 640, 3)
            face_detect_demo(r_img)
        except Exception as e:
            print(e)
        if ord(' ') == cv2.waitKey(10):
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        temp_data = b''  # 清空数据 便于下一章照片使用
    else:
        temp_data = temp_data + data  # 不是结束的包 讲数据添加进temp_data
cv2.destroyAllWindows()
