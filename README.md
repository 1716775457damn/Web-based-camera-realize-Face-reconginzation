# Web-based-camera-realize-Face-reconginzation
# ESP32-CAM 人脸识别开灯项目  
![images
](https://raw.githubusercontent.com/1716775457damn/Web-based-camera-realize-Face-reconginzation/main/images/1.png)
## 简介  本项目使用ESP32-CAM摄像头模块结合人脸识别算法，实现当识别到人脸时自动开启灯光的功能。适用于家庭安全、自动化照明等场景。
![images](https://raw.githubusercontent.com/1716775457damn/Web-based-camera-realize-Face-reconginzation/main/images/Snipaste_2024-05-08_14-31-29.png)
## 硬件需求  - 1 x ESP32-CAM模块 - 1 x 继电器模块（用于控制灯光） - 1 x LED灯或其他类型的灯 - 1 x 电源（为ESP32-CAM和LED灯供电） - 1 x 面包板和一些跳线 
## 软件需求  - Arduino IDE - ESP32-CAM开发板的Arduino核心 - 人脸识别库（如OpenCV等） 
## 安装步骤  1. 安装Arduino IDE。 2. 在Arduino IDE中安装ESP32-CAM的开发板核心。 3. 通过USB将ESP32-CAM连接到计算机。 4. 将继电器模块和LED灯连接到ESP32-CAM的相应GPIO引脚。 5. 在Arduino IDE中打开项目代码，确保人脸识别库已正确安装。 
## 配置  在代码中配置WiFi连接信息、继电器控制引脚和人脸识别参数。

```cpp
const char* ssid = "your_SSID";
 const char* password = "your_PASSWORD"; 
// 人脸识别参数
int faceDetectThreshold = 250 ;
```

## 上传代码

将代码上传到ESP32-CAM模块。

## 使用

1.  打开电源，启动ESP32-CAM。
2.  通过ESP32-CAM连接到WiFi。
3.  当摄像头检测到人脸时，继电器将触发，LED灯将亮起。

## 故障排除

-   确保所有连接都已正确焊接或连接。
-   检查代码中的引脚分配是否与实际硬件连接相匹配。
-   确认WiFi凭据正确无误。

## 贡献

欢迎对本项目做出贡献。请遵循以下步骤：

1.  Fork本项目。
2.  创建一个新的分支 (`git checkout -b feature-branch`)。
3.  提交您的更改 (`git commit -am 'Add some feature'`)。
4.  推送到分支 (`git push origin feature-branch`)。
5.  开启一个新的Pull Request。

## 许可证

本项目采用
[MIT License](https://github.com/1716775457damn/Web-based-camera-realize-Face-reconginzation/blob/main/LICENSE)
您可以自由使用、修改和分发本软件，但请遵守许可证中的条款。

## 联系

如有问题或需要技术支持，请联系 [1716775457@qq.com](1716775457@qq.com)
