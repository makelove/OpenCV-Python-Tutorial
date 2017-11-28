# 使用CUDA进行GPU加速

- 参考
    - [Compiling OpenCV with CUDA support](https://www.pyimagesearch.com/2016/07/11/compiling-opencv-with-cuda-support/)
    - [CUDA文档](https://opencv.org/platforms/cuda.html)
    
- 验证安装
```python
import cv2
print(cv2.getBuildInformation())
#Use Cuda:                    YES (ver 8.0)
#表示成功
```    
- 代码sample
```bash
nvidia@gpu:/usr/share/OpenCV/samples/gpu$ ls
alpha_comp.cpp                    hog.cpp                     pyrlk_optical_flow.cpp
bgfg_segm.cpp                     houghlines.cpp              stereo_match.cpp
cascadeclassifier.cpp             morphology.cpp              stereo_multi.cpp
cascadeclassifier_nvidia_api.cpp  multi.cpp                   super_resolution.cpp
driver_api_multi.cpp              opengl.cpp                  surf_keypoint_matcher.cpp
driver_api_stereo_multi.cpp       optical_flow.cpp            video_reader.cpp
farneback_optical_flow.cpp        opticalflow_nvidia_api.cpp  video_writer.cpp
generalized_hough.cpp             performance

```
- 代码C++
```cython
#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/gpu/gpu.hpp"
using namespace std;
using namespace cv;
using namespace cv::gpu;  

int main (int argc, char* argv[])
{
    try
    {
        cv::Mat src_host = cv::imread("file.png", CV_LOAD_IMAGE_GRAYSCALE);
        cv::gpu::GpuMat dst, src;
        src.upload(src_host);

        cv::gpu::threshold(src, dst, 128.0, 255.0, CV_THRESH_BINARY);

        cv::Mat result_host;
        dst.download(result_host);

        cv::imshow("Result", result_host);
        cv::waitKey();
    }
    catch(const cv::Exception& ex)
    {
        std::cout << "Error: " << ex.what() << std::endl;
    }
    return 0;
}
```
- 编译
    - 失败：g++ `pkg-config --cflags --libs opencv` -lopencv_gpu  cuda_test.cpp -o cuda_test