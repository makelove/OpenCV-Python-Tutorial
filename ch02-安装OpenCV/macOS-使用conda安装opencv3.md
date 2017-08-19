https://solarianprogrammer.com/2016/11/29/install-opencv-3-with-python-3-on-macos/


在本文中，我将向您展示如何在MacOS Sierra上使用Python 3安装OpenCV 3。我在网上发现的大多数教程，包括OpenCV文档，似乎只涉及到Python 2.7。

默认情况下，MacOS默认使用Python 2.7，在这一点上，它仅接收错误修复，到2020年将是EOL。Python 3.x是未来，它受到所有主要Python库的支持。在本教程中，我们将使用最新的稳定的Python 3版本，Python 3.5.2。

在MacOS上安装Python 3有多种方法。根据我的经验，初学者最简单的方法是使用像Miniconda这样的软件包管理器。从Miniconda下载页面中选择3.5 bash安装程序。下载完成后，打开终端并启动安装程序：

cd Downloads/
bash Miniconda3-latest-MacOSX-x86_64.sh

在大多数情况下，您可以使用安装程序建议的默认值。如果您希望Miniconda加入您的PATH，请小心。如果您选择了yes，Miniconda Python将影响系统Python，因此当您在终端中编写python时，您将启动Python 3.5而不是默认的2.7。我的建议是将Miniconda添加到您的PATH中。如果在某个时候你想要恢复到2.7，那么就像你的.bash_profile文件中的Miniconda行一样简单。

安装完成后，假设您保留安装程序默认值，则需要启用新的PATH设置。这可以通过关闭并重新打开您的终端来实现，也可以通过写入：

* cd ~

* . .bash_profile

现在，你应该在你的PATH中提供conda命令。快速测试是运行conda info命令。这是我在我的情况下看到的

 1 ~ $ conda info
 2 Current conda install:
 3 
 4              platform : osx-64
 5         conda version : 4.1.11
 6     conda-env version : 2.5.2
 7   conda-build version : not installed
 8        python version : 3.5.2.final.0
 9      requests version : 2.10.0
10      root environment : /Users/sol/miniconda3  (writable)
11   default environment : /Users/sol/miniconda3
12      envs directories : /Users/sol/miniconda3/envs
13         package cache : /Users/sol/miniconda3/pkgs
14          channel URLs : https://repo.continuum.io/pkgs/free/osx-64/
15                         https://repo.continuum.io/pkgs/free/noarch/
16                         https://repo.continuum.io/pkgs/pro/osx-64/
17                         https://repo.continuum.io/pkgs/pro/noarch/
18           config file : None
19          offline mode : False
20     is foreign system : False
21 
22 ~ $
让我们遵循最佳做法并创建一个新的Python环境：

1 conda create -n myenv python = 3.5 
2 source activate myenv
此时，您的提示应该表明您正在使用myenv环境。环境允许您在同一台机器上具有不同版本的Python和库。举个例子，你可以有一个myenv环境，你已经安装了SciPy和一个播放环境，你已经安装了PyGame。环境是完全独立的。如果您想要实验Python或其他库的开发版本，同时保持稳定的版本分开，这是非常有用的。

一旦环境被激活，所有的安装命令将仅适用于当前的环境。默认情况下，如果关闭终端，则环境将被禁用。如果您想要使用它，请使用source activate myenv命令。

OpenCV取决于NumPy，可以安装：

1 conda install numpy
OpenCV并没有直接提供在Miniconda主存储库中，而是由第三方提供给主Anaconda仓库。我们需要安装anaconda-client命令实用程序才能搜索OpenCV二进制文件：

1 conda install anaconda-client
现在，使用下一个命令搜索OpenCV 3：

1 anaconda search -t conda opencv3
您应该看到有可用的OpenCV 3发行版的列表，如下图所示：

Anaconda OpenCV 3可用二进制文件列表

从上面的列表中，我将选择名为menpo / opencv3的包，因为它为所有主要操作系统提供二进制文件，最重要的是为osx-64提供二进制文件。您可以安装menpo / opencv3软件包：

conda install --channel https://conda.anaconda.org/menpo opencv3

在这一点上，您应该在Mac上安装OpenCV 3和Python。我们可以编写一个打印OpenCV版本的小型测试程序，从磁盘加载图像，将图像转换为灰色并显示结果。首先下载下一张图片：