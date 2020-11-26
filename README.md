# Visual-Recognition-HW2
NCTU Visual Recognition Homework 2

## Hardware
OS: Ubuntu 18.04.3 LTS

CPU: Intel(R) Xeon(R) W-2133 CPU @ 3.60GHz

GPU: 1x GeForce RTX 2080 TI

## Reproducing Submission
To reproduct my submission without retrainig, do the following steps:
1. [Installation](#installation)
2. [Dataset Preparation](#Dataset-Preparation)
3. [Training detail](#Training)
4. [Testing detail](#Testing)
5. [Reference](#Reference)

## Installation

this code was trained and tested on Ubuntu 18.04

```
conda activate yolo
pip install -r requirements.txt

sudo apt-get install libopencv-dev==3.2.0

check the Makefile
1. use cpu for training: GPU=0, CUDNN=0, OPENCV=1
2. use gpu for training: GPU=1, CUDNN=1, OPENCV=1

cd /path/to/your/darknet/
make

```

## Dataset Preparation
```
cs-t0828-2020-hw2

1. for data preparation
├── HW2
│   ├── train
│   │   ├── Put training images here
│   ├── test
│   │   ├── Put testing images here
│   ├── label
│   │   ├── Output YOLO type label will be here
│   ├── result
│   │   ├── Put output result.json here
│   ├── digitStruct.mat
│   ├── train_data.csv
│   ├── json2submit.py
│   ├── label2yolo.py
│   ├── train_val_txt.py

2. for model
├── yolov4
│   ├── darknet
│   │   ├── data
│   │   │   ├── Put your own .names here
│   │   ├── cfg
│   │   │   ├── Put your own .data and .cfg here
│   │   ├── yolov4_XXXXX.weights (testing weight)
│   │   ├── yolov4.weights (pretrain weight)
│   │   ├── Makefile
├── Visual_Recognition
│   ├── HW2
│   │   ├── train
│   │   │   ├── Put your training data and label here
│   │   ├── train
│   │   │   ├── Put your testing data here
│   │   ├── train.txt
│   │   ├── val.txt
│   │   ├── test.txt

```
I seperate the original training data (33402 images) into two part. One for training (30000 images) and one for evaluating(3402 images). 

## Training
To train models:

cd /path/to/your/darknet/

./darknet detector train cfg/my.data cfg/yolov4.cfg yolov4.weights -dont_show -mjpeg_port 8090 -map -clear -gpus 0

you can see the training loss: http://localhost:8090/

The expected training times are:
Model | GPUs | Image size | Training Iteration | Training Time
------------ | ------------- | ------------- | ------------- | -------------
darknet | 1x RTX 2080Ti | 608 x 608 | 67000 | 24 hours


## Testing
To test models:

cd /path/to/your/darknet/

./darknet detector test cfg/my.data cfg/yolov4.cfg yolov4_20000.weights -thresh 0.001 -ext_output -dont_show -out result.json < ../../HW2/test.txt



## Reference
1. [YOLO](https://github.com/AlexeyAB/darknet).
2. [.mat to .csv](https://github.com/pavitrakumar78/Street-View-House-Numbers-SVHN-Detection-and-Classification-using-CNN/blob/master/construct_datasets.py)
