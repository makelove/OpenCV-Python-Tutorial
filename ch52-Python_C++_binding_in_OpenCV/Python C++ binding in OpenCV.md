# Python C++ binding in OpenCV
http://docs.opencv.org/3.2.0/da/d49/tutorial_py_bindings_basics.html

## OpenCV-Python绑定如何工作？


### 学习目标：

* 如何生成OpenCV-Python绑定？
* 如何将新的OpenCV模块扩展到Python？

### 如何生成OpenCV-Python绑定？

在OpenCV中，所有算法都用C ++实现。但是这些算法可以从Python，Java等不同的语言使用。这可以通过绑定生成器来实现。这些生成器在C ++和Python之间创建了一个桥梁，使用户能够从Python调用C ++函数。要了解背景中发生的情况，需要熟悉Python / C API。官方Python文档[1]可以找到一个将C ++函数扩展为Python的简单示例。因此，通过手动编写其包装函数将OpenCV中的所有功能扩展到Python是一项耗时的任务。因此，OpenCV以更智能的方式实现。OpenCV使用位于modules / python / src2中的Python脚本从C ++头自动生成这些包装函数。我们将研究他们做什么。

首先，modules / python / CMakeFiles.txt是一个CMake脚本，它将模块扩展到Python。它将自动检查所有模块的扩展名并抓取其头文件。这些头文件包含该特定模块的所有类，函数，常量等的列表。

其次，这些头文件传递给Python脚本modules / python / src2 / gen2.py。这是Python绑定生成器脚本。它调用另一个Python脚本modules / python / src2 / hdr_parser.py。这是头解析器脚本。这个头文件解析器将完整的头文件分成小的Python列表。所以这些列表包含有关特定函数，类等的所有细节。例如，一个函数将被解析以获取包含函数名，返回类型，输入参数，参数类型等的列表。最终列表包含所有函数的详细信息，结构体，类别等。

但是头解析器不解析头文件中的所有函数/类。开发人员必须指定哪些函数应该导出到Python。为此，有一些宏添加到这些声明的开始，使头解析器能够识别要解析的函数。这些宏由编程特定功能的开发人员添加。简而言之，开发者决定哪些功能应该扩展到Python，哪些不是。这些宏的细节将在下一个会议中给出。

所以头解析器返回一个最后一个解析函数列表。我们的生成器脚本（gen2.py）将为头解析器解析的所有函数/ classes / enums / struct创建包装函数（您可以在build / modules / python /文件夹中编译时找到这些头文件作为pyopencv_generated _ * .h文件）。但是可能会有一些基本的OpenCV数据类型，如Mat，Vec4i，Size。他们需要手动扩展。例如，一个Mat类型应该扩展到Numpy数组，Size应该被扩展为一个两个整数的元组等等。类似地，可能有一些复杂的结构体/类/函数等需要手动扩展。所有这些手动包装器功能都放在modules / python / src2 / cv2.cpp中。

所以现在只剩下的是编译这些包装文件，这给我们提供了cv2模块。所以当你调用一个函数的时候，你可以用Python中的res = equalizeHist（img1，img2）来传递两个numpy数组，你会发现另外一个numpy数组作为输出。所以这些numpy数组被转换为cv :: Mat，然后调用C ++中的equalizeHist（）函数。最终的结果，res将被转换成一个Numpy数组。所以简而言之，几乎所有的操作都是用C ++完成的，这给了我们几乎与C ++相同的速度。

所以这是OpenCV-Python绑定生成的基本版本。

如何将新模块扩展到Python？

头文件解析器基于添加到函数声明中的一些包装器宏解析头文件。枚举常数不需要任何包装宏。它们被自动包装。但是剩下的函数，类等都需要包装宏。

使用CV_EXPORTS_W宏扩展函数。一个例子如下所示。
```C++
CV_EXPORTS_W  void  equalizeHist（InputArray src，OutputArray dst）;
```
标题解析器可以了解InputArray，OutputArray等关键字的输入和输出参数。但有时候，我们可能需要对输入和输出进行硬编码。为此，使用像CV_OUT，CV_IN_OUT等宏。
```
CV_EXPORTS_W  void  minEnclosingCircle（InputArray points，
                                     CV_OUT  Point2f＆center，CV_OUT  float＆radius）;
```
对于大班，也使用CV_EXPORTS_W。要扩展类方法，使用CV_WRAP。类似地，CV_PROP用于类字段。
```
class CV_EXPORTS_W CLAHE : public Algorithm
{
public:
    CV_WRAP virtual void apply(InputArray src, OutputArray dst) = 0;
    CV_WRAP virtual void setClipLimit(double clipLimit) = 0;
    CV_WRAP virtual double getClipLimit() const = 0;
}
```
可以使用CV_EXPORTS_AS扩展重载功能。但是我们需要传递一个新名称，以便每个函数都将被Python中的该名称调用。以下为积分函数。有三个功能可用，所以每个功能都用Python中的后缀命名。类似地，CV_WRAP_AS可用于包装重载方法。
```
CV_EXPORTS_W void integral( InputArray src, OutputArray sum, int sdepth = -1 );
CV_EXPORTS_AS(integral2) void integral( InputArray src, OutputArray sum,
                                        OutputArray sqsum, int sdepth = -1, int sqdepth = -1 );
CV_EXPORTS_AS(integral3) void integral( InputArray src, OutputArray sum,
                                        OutputArray sqsum, OutputArray tilted,
                                        int sdepth = -1, int sqdepth = -1 );
```
使用CV_EXPORTS_W_SIMPLE扩展小类/结构体。这些结构体通过值传递给C ++函数。示例是KeyPoint，Match等。它们的方法由CV_WRAP扩展，字段由CV_PROP_RW扩展。
```
class CV_EXPORTS_W_SIMPLE DMatch
{
public:
    CV_WRAP DMatch();
    CV_WRAP DMatch(int _queryIdx, int _trainIdx, float _distance);
    CV_WRAP DMatch(int _queryIdx, int _trainIdx, int _imgIdx, float _distance);
    CV_PROP_RW int queryIdx; // query descriptor index
    CV_PROP_RW int trainIdx; // train descriptor index
    CV_PROP_RW int imgIdx;   // train image index
    CV_PROP_RW float distance;
};
```
可以使用CV_EXPORTS_W_MAP导出一些其他小类/结构体，将其导出到Python本机字典。Moments（）是一个例子。
```
class CV_EXPORTS_W_MAP Moments
{
public:
    CV_PROP_RW double  m00, m10, m01, m20, m11, m02, m30, m21, m12, m03;
    CV_PROP_RW double  mu20, mu11, mu02, mu30, mu21, mu12, mu03;
    CV_PROP_RW double  nu20, nu11, nu02, nu30, nu21, nu12, nu03;
};
```
所以这些是OpenCV中可用的主要扩展宏。通常，开发人员必须将适当的宏放在适当的位置。休息由生成器脚本完成。有时，发生器脚本可能不能创建包装器的特殊情况。这样的功能需要手动处理，为此您可以编写自己的pyopencv _ *。hpp扩展头文件，并将它们放入模块的misc / python子目录中。但大多数情况下，根据OpenCV编码指南编写的代码将被生成器脚本自动包装。