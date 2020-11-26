import pandas as pd
import numpy as np
from PIL import Image
from tqdm import tqdm

csv_path = './train_data.csv'

img = pd.read_csv(csv_path)
    
img2 = np.squeeze(img.values)

pre_img = None
label_total = []
for temp in tqdm(img2):
    
    if pre_img == temp[1]:
        pass
    elif pre_img == None:
        path = "./train/" + temp[1]
        img_shape = np.transpose(Image.open(path), (2, 1, 0)).shape
        img_width = img_shape[1]
        img_height = img_shape[2]
        
        label_list = []
        label_list.append(temp[1])
        
    else:
        path = "./train/" + temp[1]
        img_shape = np.transpose(Image.open(path), (2, 1, 0)).shape
        img_width = img_shape[1]
        img_height = img_shape[2]
        label_total.append(label_list)
        label_list = []
        label_list.append(temp[1])
        
    cur_label = []
    
    yolo_class = temp[2]
    if yolo_class == 10:
        yolo_class = 0.0
    
    yolo_width = temp[5]
    yolo_width_norm = yolo_width / img_width
    
    yolo_height = temp[0]
    yolo_height_norm = yolo_height / img_height
    
    yolo_xcenter = (temp[3] + temp[7]) / 2
    yolo_xcenter_norm = yolo_xcenter / img_width
    
    yolo_ycenter = (temp[4] + temp[6]) / 2
    yolo_ycenter_norm = yolo_ycenter / img_height
    
    cur_label.append(int(yolo_class))
    cur_label.append(yolo_xcenter_norm)
    cur_label.append(yolo_ycenter_norm)
    cur_label.append(yolo_width_norm)
    cur_label.append(yolo_height_norm)
    
    label_list.append(cur_label)
    
    pre_img = temp[1]

label_total.append(label_list)
    
for label_index in tqdm(range(len(label_total))):
    
    label = label_total[label_index]
    img_index = label[0].split(".")[0]
    
    with open("./label/" + str(img_index) + ".txt" ,"w") as f:
        for i in range(1, len(label)):
            for j in range(5):
                f.write(str(label[i][j]))
                f.write(" ")
            f.write("\n")

    