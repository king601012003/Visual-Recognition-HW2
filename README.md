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

check the Makefile
1. use cpu for training: GPU=0, CUDNN=0, OPENCV=1
2. use gpu for training: GPU=1, CUDNN=1, OPENCV=1

sudo apt-get install libopencv-dev==3.2.0

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
│   │   ├── yolov4_XXXXX.weights (pretrain weight)
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
I seperate the original training data (11185 images) into two part. One for training (10000 images) and one for evaluating(1185 images). 

## Training
To train models:

Open the **model.py** with your own IDE and directly run it. 
There are several hyperparameters in the code **156 ~ 163**.

The expected training times are:
Model | GPUs | Image size | Training Epochs | Training Time
------------ | ------------- | ------------- | ------------- | -------------
efficientnet | 1x RTX 2080Ti | 224 x 224 | 100 | 180 minutes

*  model_state = "train"
*  batch_size = 25
*  network = 8


## Testing
To test models:

Open the **model.py** with your own IDE and directly run it. 
There are several hyperparameters in the code **156 ~ 163**.

*  model_state = "eval" 
*  batch_size = 25
*  network = 8
*  ckpt_path = "/PATH/TO/YOUR/WEIGHT/FILE"
*  model_weight = ""epoch_XX.pkl""

## Reference
1. [YOLO](https://github.com/AlexeyAB/darknet).
2. [.mat to .csv](https://github.com/pavitrakumar78/Street-View-House-Numbers-SVHN-Detection-and-Classification-using-CNN/blob/master/construct_datasets.py)
