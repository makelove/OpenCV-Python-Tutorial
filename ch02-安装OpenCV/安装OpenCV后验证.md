##安装OpenCV后验证

- pkg-config
```bash
pkg-config --modversion opencv
3.3.0
```

```python
import cv2
print(cv2.getBuildInformation())
#
'''
General configuration for OpenCV 3.3.0 =====================================
  Version control:               3.3.0

  Platform:
    Timestamp:                   2017-11-26T11:05:49Z
    Host:                        Linux 4.4.38-tegra aarch64
    CMake:                       3.5.1
    CMake generator:             Unix Makefiles
    CMake build tool:            /usr/bin/make
    Configuration:               Release

  CPU/HW features:
    Baseline:                    NEON FP16
      required:                  NEON
      disabled:                  VFPV3

  C/C++:
    Built as dynamic libs?:      YES
    C++ Compiler:                /usr/bin/c++  (ver 5.4.0)
    C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
    C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
    C Compiler:                  /usr/bin/cc
    C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
    C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections    -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
    Linker flags (Release):
    Linker flags (Debug):
    ccache:                      NO
    Precompiled headers:         NO
    Extra dependencies:          gtk-x11-2.0 gdk-x11-2.0 pangocairo-1.0 atk-1.0 cairo gdk_pixbuf-2.0 gio-2.0 pangoft2-1.0 pango-1.0 fontconfig freetype gthread-2.0 /usr/lib/aarch64-linux-gnu/libwebp.so /usr/lib/aarch64-linux-gnu/libpng.so /usr/lib/aarch64-linux-gnu/libz.so /usr/lib/aarch64-linux-gnu/libtiff.so /usr/lib/aarch64-linux-gnu/libjasper.so /usr/lib/aarch64-linux-gnu/libjpeg.so gstbase-1.0 gstreamer-1.0 gobject-2.0 glib-2.0 gstvideo-1.0 gstapp-1.0 gstriff-1.0 gstpbutils-1.0 avcodec-ffmpeg avformat-ffmpeg avutil-ffmpeg swscale-ffmpeg dl m pthread rt /usr/lib/aarch64-linux-gnu/libtbb.so cudart nppc nppi npps cufft -L/usr/local/cuda-8.0/lib64
    3rdparty dependencies:

  OpenCV modules:
    To be built:                 cudev core cudaarithm flann imgproc ml objdetect video cudabgsegm cudafilters cudaimgproc cudawarping dnn imgcodecs photo shape videoio cudacodec highgui ts features2d calib3d cudafeatures2d cudalegacy cudaobjdetect cudaoptflow cudastereo stitching superres videostab python2 python3
    Disabled:                    world
    Disabled by dependency:      -
    Unavailable:                 java viz

  GUI:
    QT:                          NO
    GTK+ 2.x:                    YES (ver 2.24.30)
    GThread :                    YES (ver 2.48.1)
    GtkGlExt:                    NO
    OpenGL support:              NO
    VTK support:                 NO

  Media I/O:
    ZLib:                        /usr/lib/aarch64-linux-gnu/libz.so (ver 1.2.8)
    JPEG:                        /usr/lib/aarch64-linux-gnu/libjpeg.so (ver )
    WEBP:                        /usr/lib/aarch64-linux-gnu/libwebp.so (ver encoder: 0x0202)
    PNG:                         /usr/lib/aarch64-linux-gnu/libpng.so (ver 1.2.54)
    TIFF:                        /usr/lib/aarch64-linux-gnu/libtiff.so (ver 42 - 4.0.6)
    JPEG 2000:                   /usr/lib/aarch64-linux-gnu/libjasper.so (ver 1.900.1)
    OpenEXR:                     NO
    GDAL:                        NO
    GDCM:                        NO

  Video I/O:
    DC1394 1.x:                  NO
    DC1394 2.x:                  NO
    FFMPEG:                      YES
      avcodec:                   YES (ver 56.60.100)
      avformat:                  YES (ver 56.40.101)
      avutil:                    YES (ver 54.31.100)
      swscale:                   YES (ver 3.1.101)
      avresample:                NO
    GStreamer:
      base:                      YES (ver 1.8.3)
      video:                     YES (ver 1.8.3)
      app:                       YES (ver 1.8.3)
      riff:                      YES (ver 1.8.3)
      pbutils:                   YES (ver 1.8.3)
    OpenNI:                      NO
    OpenNI PrimeSensor Modules:  NO
    OpenNI2:                     NO
    PvAPI:                       NO
    GigEVisionSDK:               NO
    Aravis SDK:                  NO
    UniCap:                      NO
    UniCap ucil:                 NO
    V4L/V4L2:                    NO/YES
    XIMEA:                       NO
    Xine:                        NO
    Intel Media SDK:             NO
    gPhoto2:                     NO

  Parallel framework:            TBB (ver 4.4 interface 9002)

  Trace:                         YES ()

  Other third-party libraries:
    Use Intel IPP:               NO
    Use Intel IPP IW:            NO
    Use VA:                      NO
    Use Intel VA-API/OpenCL:     NO
    Use Lapack:                  NO
    Use Eigen:                   YES (ver 3.2.92)
    Use Cuda:                    YES (ver 8.0)
    Use OpenCL:                  NO
    Use OpenVX:                  NO
    Use custom HAL:              YES (carotene (ver 0.0.1))

  NVIDIA CUDA
    Use CUFFT:                   YES
    Use CUBLAS:                  NO
    USE NVCUVID:                 NO
    NVIDIA GPU arch:             62
    NVIDIA PTX archs:
    Use fast math:               NO

  Python 2:
    Interpreter:                 /usr/bin/python2.7 (ver 2.7.12)
    Libraries:                   /usr/lib/aarch64-linux-gnu/libpython2.7.so (ver 2.7.12)
    numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.11.0)
    packages path:               lib/python2.7/dist-packages

  Python 3:
    Interpreter:                 /usr/bin/python3 (ver 3.5.2)
    Libraries:                   /usr/lib/aarch64-linux-gnu/libpython3.5m.so (ver 3.5.2)
    numpy:                       /usr/lib/python3/dist-packages/numpy/core/include (ver 1.11.0)
    packages path:               lib/python3.5/dist-packages

  Python (for build):            /usr/bin/python2.7

  Java:
    ant:                         NO
    JNI:                         NO
    Java wrappers:               NO
    Java tests:                  NO

  Matlab:                        Matlab not found or implicitly disabled

  Documentation:
    Doxygen:                     NO

  Tests and samples:
    Tests:                       YES
    Performance tests:           YES
    C/C++ Examples:              YES

  Install path:                  /usr

  cvconfig.h is in:              /home/nvidia/opencv/build
-----------------------------------------------------------------
'''
```