# -*- coding: utf-8 -*-
import numpy as np
import cv2

'''
• img: 你想 绘制图形的 幅图像。
• color: 形状的颜色。以RGB为例  需要传入一个元组BGR 例如 255,0,0 
   代表蓝色，第一个是蓝色通道，第二个是绿色通道，第三个是红色通道。对于灰度图只需要传入灰度值。
• thickness 线条的粗细。如果给一个闭合图形 置为 -1  那么这个图形
就会被填充。 默认值是 1.
• linetype 线条的类型， 8 连接，抗锯齿等。  默认情况是8 连接。cv2.LINE_AA
   为抗锯齿  这样看起来会非常平滑。

'''

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img, pt1=(0, 0), pt2=(511, 511), color=(255, 0, 0), thickness=5)  # pt1, pt2, color, thickness=
# cv2.polylines() 可以 用来画很多条线。只需要把想 画的线放在一 个列表中， 将 列表传给函数就可以了。每条线 会被独立绘制。 这会比用 cv2.line() 一条一条的绘制 要快一些。
# cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)
cv2.arrowedLine(img,pt1=(21, 13), pt2=(151, 401), color=(255, 0, 0), thickness=5)

cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

cv2.circle(img, center=(447, 63), radius=63, color=(0, 0, 255), thickness=-1)  # center, radius, color, thickness=None

# 一个参数是中心点的位置坐标。 下一个参数是长轴和短轴的长度。椭圆沿逆时针方向旋转的角度。
# 椭圆弧演顺时针方向起始的角度和结束角度 如果是 0 很 360 就是整个椭圆
cv2.ellipse(img, center=(256, 256), axes=(100, 50), angle=0, startAngle=0, endAngle=180, color=255,
            thickness=-1)  # center, axes, angle, startAngle, endAngle, color, thickness=

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
# 这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
# 注意 如果第三个参数是 False 我们得到的多边形是不闭合的 ，首 尾不相  连 。

font = cv2.FONT_HERSHEY_SIMPLEX
#org :Bottom-left corner of the text string in the image.左下角
#或使用 bottomLeftOrigin=True,文字会上下颠倒
cv2.putText(img, text='bottomLeftOrigin', org=(10, 400), fontFace=font, fontScale=1, color=(255, 255, 255), thickness=1,bottomLeftOrigin=True)#text, org, fontFace, fontScale, color, thickness=
cv2.putText(img, text='OpenCV', org=(10, 500), fontFace=font, fontScale=4, color=(255, 255, 255), thickness=2)#text, org, fontFace, fontScale, color, thickness=

# 所有的绘图函数的返回值都是 None ，所以不能使用 img = cv2.line(img,(0,0),(5

winname = 'example'
cv2.namedWindow(winname, 0)
cv2.imshow(winname, img)

cv2.imwrite("example.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
