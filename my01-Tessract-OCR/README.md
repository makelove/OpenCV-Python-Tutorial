参考：
http://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/


## 安装
* macOS: brew install tesseract --all-languages
* ubuntu: sudo apt-get install tesseract-ocr
* pip install pillow
* pip install pytesseract


## 运行


* 标准输出，不用输出到TXT文件:
tesseract images/example_01.png stdout
* py ocr.py -i  example_01.png -p blur