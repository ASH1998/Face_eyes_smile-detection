# Face_eyes_smile-detection
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)  [![HitCount](http://hits.dwyl.io/ASH1998/android-digit-recogniser.svg)](http://hits.dwyl.io/ASH1998/android-digit-recogniser)   
This is an OpenCV application for face, eyes, smile detection. It uses haarcascade provided by OpenCV

## Requirements :
1. The PC should have a working Webcam(mainwebcam 0, other cams 1 or further numbers)
2. Must allow third party connection with WebCam

## Dependencies :
1. Python     
2. Opencv-Python
3. Download the required haars from [here](https://github.com/opencv/opencv/tree/master/data/haarcascades).     
4. cx_freeze(if you want to run `setup.py` for making a windows binary(.exe) file).

## Usage:
After successful installation of opencv-python and downloading the haars, run the script and change in the haar name in `cv2.CascadeClassifier` in the program `FACE_EYES_SMILE_DETECTION.PY`

## Windows Binary : 
The script `setup.py` uses `cx_freeze` module make sure to install it.    
Then open cmd in the specified folder, and run the commands below :
```
python setup.py build
python setup.py bdist_msi
```
### Note : 
I have uploaded my windows binary file too...if in any case you cant build it, feel free to download mine!!     
You can find in my [releases](https://github.com/ASH1998/Face_eyes_smile-detection/releases) under this project [here](https://github.com/ASH1998/Face_eyes_smile-detection/releases/download/V1.01/Face.Eyes.Smile.Detection-0.1-amd64.msi)      
or from my [google drive](https://drive.google.com/open?id=0B1wREOeURNTcUjNCWXhHaGtPTlE)
