import json
from PIL import Image
import numpy as np
from tqdm import tqdm

json_path = './result/result.json'
save_path = './result/0856640.json'

def change2submit_coor(box_dict, image_idx):
    path = "./test/" + str(image_idx) + ".png"
    img_shape = np.transpose(Image.open(path), (2, 1, 0)).shape
    img_width = img_shape[1]
    img_height = img_shape[2]
    
    xcenter = box_dict["center_x"]*img_width
    ycenter = box_dict["center_y"]*img_height
    height = box_dict["height"]*img_height
    width = box_dict["width"]*img_width
    
    x1 = int(round(xcenter - width*0.5))
    x2 = int(round(xcenter + width*0.5))
    y1 = int(round(ycenter - height*0.5))
    y2 = int(round(ycenter + height*0.5))
    
    return(y1, x1, y2, x2)
    

with open(json_path) as json_file: 
    results = json.load(json_file) 

for result_index in range(len(results)):
    del results[result_index]["frame_id"]
    results[result_index]["filename"] = int(results[result_index]["filename"].split("/")[-1].split(".")[0])
    
results = sorted(results, key=lambda x: x['filename'])

submit_list = []

for result in tqdm(results):
    submit_dict = {}
    bbox = []
    score = []
    label = []
    
    for obj_index in range(len(result["objects"])):
        score.append(result["objects"][obj_index]["confidence"])
        label.append(result["objects"][obj_index]["class_id"] if result["objects"][obj_index]["class_id"] != 0 else 10 )
        bbox.append(change2submit_coor(result["objects"][obj_index]["relative_coordinates"], result["filename"]))
        
    submit_dict["bbox"] = bbox
    submit_dict["score"] = score
    submit_dict["label"] = label
    
    submit_list.append(submit_dict)
    
with open(save_path, 'w') as js:
    json.dump(submit_list, js, ensure_ascii=False)
    