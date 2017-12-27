- 参考
    - 原文:[How to break a CAPTCHA system in 15 minutes with Machine Learning](https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710)
    - 源代码下载:https://s3-us-west-2.amazonaws.com/mlif-example-code/solving_captchas_code_examples.zip
    - 翻译:[仅需15分钟，使用OpenCV+Keras轻松破解验证码](https://www.jiqizhixin.com/articles/2017-12-14-2)

- 修改:
    - 训练过程改为1次
    - 识别验证码,添加input中断循环


### Before you get started

To run these scripts, you need the following installed:

1. Python 3
2. OpenCV 3 w/ Python extensions
 - I highly recommend these OpenCV installation guides: 
   https://www.pyimagesearch.com/opencv-tutorials-resources-guides/ 
3. The python libraries listed in requirements.txt
 - Try running "pip3 install -r requirements.txt"

### Step 1: Extract single letters from CAPTCHA images

Run:

python3 extract_single_letters_from_captchas.py

The results will be stored in the "extracted_letter_images" folder.


### Step 2: Train the neural network to recognize single letters

Run:

python3 train_model.py

This will write out "captcha_model.hdf5" and "model_labels.dat"


### Step 3: Use the model to solve CAPTCHAs!

Run: 

python3 solve_captchas_with_model.py