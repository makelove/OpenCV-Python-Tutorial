网址：https://pypi.python.org/pypi/opencv-python

## 安装 opencv-python
- virtualenv -p python3 .cv2
- source .cv2/bin/activate
- pip install opencv-python
- pip install matplotlib
- 验证 python -c "import cv2;print(cv2.__version__,cv2.__doc__,cv2.__file__)"


## 安装 opencv-contrib-python
- pip install opencv-contrib-python
- 验证 python -c "import cv2;print(cv2.__version__,cv2.__doc__,cv2.__file__)"
- 验证 python -c "import cv2;print(print(help(cv2.CascadeClassifier))"

## 常见问题
软件包包含预编译的OpenCV二进制文件和Python绑定。 
这可以为Python提供超快速（通常<10秒）OpenCV安装。 

如果您只需要OpenCV Python绑定，则不需要单独的OpenCV安装。 

**重要提示** 

MacOS和Linux的轮子目前有一些局限性： 

- 不支持视频相关的功能（不用FFmpeg编译） 
- 例如``cv2.imshow（）``将不起作用（没有使用GTK + 2编译） x或碳支持） #可以使用matplotlib来显示
