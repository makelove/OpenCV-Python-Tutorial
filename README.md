- 我在B站做视频博客VLoger，欢迎大家来捧场。不只是OpenCV
    - 程序员赚钱指南 https://space.bilibili.com/180948619

# [OpenCV-Python-Tutorial](https://github.com/makelove/OpenCV-Python-Tutorial)

## [OpenCV-Python-Tutorial-中文版.pdf](OpenCV-Python-Tutorial-中文版.pdf)
- 这个repo是这本书PDF的所有源代码，几乎都被测试过，能正常运行。程序使用的图片和视频，都在data文件内。

### 平时会添加一些有趣的代码，实现某种功能。
- 官网 https://opencv.org/
- 官方文档api https://docs.opencv.org/4.0.0/
- 官方英文教程 http://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html

## 运行:官方samples/demo.py 会有很多有趣的例子，介绍你去了解OpenCV的功能。


~~python 2.7 分支被废弃了，不再更新~~

~~# 添加了 Python3.6分支,
该分支是使用 opencv3.2+Python3.6~~

## 把原来的master分支改为python2.7分支，python3.6分支改为master分支
* git clone https://github.com/makelove/OpenCV-Python-Tutorial.git
* ~~git checkout python3.6~~

##### 建议使用PyCharm来编写/调试Python代码

## 开发环境
* macOS Mojave 10.14
* Python 3.6.1
* OpenCV 3.2.0
* PyCharm 2018.3


### VMware 虚拟机
如果安装OpenCV有问题，可以使用VMware 虚拟机安装Ubuntu系统，本人可以帮你们安装一个，再共享到百度云

### 树莓派3b
本人有一块【树莓派3b】开发板，也安装了OpenCV3，很好用，建议你们也买一块来玩一玩。

### 摄像头
* MacBook pro自带
* 淘宝，[130W像素高清摄像头模组 720P 1280x720 USB2.0免驱 微距模块](https://s.click.taobao.com/gOB3ACw)
* 淘宝，[树莓派3代B Raspberry Pi USB摄像头，免驱动](https://s.click.taobao.com/kTu2ACw) 不好用，可视角度太小！
* Kinect for Xbox360 Slim， AUX接口不能直接插入电脑，需要购买电源适配器 [淘宝](https://s.click.taobao.com/t?e=m%3D2%26s%3DuOhQTZaHKEQcQipKwQzePOeEDrYVVa64LKpWJ%2Bin0XLjf2vlNIV67rEUhWAGPPKrYFMBzHxYoCOlldgrEKAMDfvtTsPa%2Bvw8FDXjhIkoffd7RTQd3LKg2nJi6DFpZGNc%2Bht3wBcxEogkdIkZMKiRbrUG0ypJDuSgXlTpbZcV4j5YC7K2OdchcA%3D%3D&scm=null&pvid=null&app_pvid=59590_11.9.33.73_524_1585572680125&ptl=floorId%3A17741&originalFloorId%3A17741&app_pvid%3A59590_11.9.33.73_524_1585572680125&union_lens=lensId%3APUB%401585572666%400b1a25a5_48ac_1712b7ede03_179a%40023mXY9mmpUNuNySUoJofoOt)

## 教程资源
- http://www.learnopencv.com/
- http://www.pyimagesearch.com/
- [YouTube上sentex的OpenCV视频教程](https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq)
- B站 [OpenCV YouTube](https://search.bilibili.com/all?keyword=OpenCV%20YouTube)
- [官方教程](https://opencv.org/courses/)

## 新闻News https://opencv.org/news.html
- 中文论坛 http://www.opencv.org.cn/
- [OpenCV 3.3发布了](http://opencv.org/opencv-3-3.html) 
    1. 主要消息是我们将DNN模块从opencv_contrib推广到主存储库，改进和加速了很多。不再需要外部BLAS实现。对于GPU，使用Halide（http://halide-lang.org）进行实验性DNN加速。有关该模块的详细信息可以在我们的wiki中找到：[OpenCV中的深度学习](https://github.com/opencv/opencv/wiki/Deep-Learning-in-OpenCV)。
    2. OpenCV现在可以使用标志ENABLE_CXX11构建为C ++ 11库。添加了C ++ 11程序员的一些很酷的功能。
    3. 由于“动态调度”功能，我们还在OpenCV的默认版本中启用了不少AVX / AVX2和SSE4.x优化。DNN模块还具有一些AVX / AVX2优化。
Intel Media SDK现在可以被我们的videoio模块用来进行硬件加速的视频编码/解码。支持MPEG1 / 2，以及H.264。
    4. 嵌入OpenCV Intel IPP子集已从2015.12升级到2017.2版本，从而在我们的核心和imgproc perf测试中提高了15％的速度。
    5. 716拉请求已经合并，588我们的错误跟踪器中的问题已经关闭，因为OpenCV 3.2。另外，我们通过一些严格的静态分析仪工具运行OpenCV，并修复了检测到的问题。所以OpenCV 3.3应该是非常稳定和可靠的释放。
    6. 有关OpenCV 3.3的更改和新功能的更多详细信息，请访问https://github.com/opencv/opencv/wiki/ChangeLog。
    7. [下载OpenCV 3.3](https://github.com/opencv/opencv/releases/tag/3.3.0)
    8. [安装OpenCV 3.3](http://www.linuxfromscratch.org/blfs/view/cvs/general/opencv.html)
- OpenCV 4.0发布了 https://opencv.org/opencv-4-0-0.html

## 怎样翻墙？使用Google搜索引擎，观看YouTube视频教程
- shadowsocks
    - 方便，随地随时翻墙
    - 手机使用4G信号上网，也可以。
    - 强烈推荐！
    - 购物国外服务器，搭建也很容易
        - 参考 https://isweic.com/build-shadowsocks-python-server/
        - pip install shadowsocks
        - 运行
            - shell窗口运行
                - ssserver -p 8388 -k password -m aes-256-cfb
                - 8388是端口号，password是密码，aes-256-cfb是加密类型，通过Ctrl+C结束
            - 后台运行
                - ssserver -p 8388 -k password -m aes-256-cfb --user nobody -d start
                - 结束后台运行
                    - ssserver -d stop
            - 检查运行日志
                - less /var/log/shadowsocks.log
- [Lantern蓝灯](https://github.com/getlantern/lantern/releases/tag/latest)
    - 本人不使用蓝灯了。
    1. 可以免费使用，但用完800m流量后会限速，还能正常使用，就是有点慢
    2. 专业版不贵，2年336元，每天0.46元。[Lantern蓝灯专业版购买流程](https://github.com/getlantern/forum/issues/3863)
    3. 邀请好友来获得更多的专业版使用时间。我的邀请码：GW2362
    
## 更新
- [破解验证码](my06-验证码识别/solving_captchas_code_examples/README.md)
    
## 捐赠打赏  
- OpenCV问答群1,QQ群号:187436093
- 微信  
    - <img src="data/wechat_donate.jpg" width = "200" height = "200" alt="wechat_donate"  />


- 支付宝
    - <img src="data/alipay_donate.jpg" width = "200" height = "200" alt="alipay_donate"  />
 
- 福利
    - 免费国内服务器，但需要交押金，随时全额原路退还
        - 有需要的朋友请加入QQ群，发【手机号】给群主
        - ![free_server](data/free_server.jpeg)