import os
import numpy as np

img = os.listdir("./train")

img = np.random.permutation(img)

train = img[0:30000].copy()
val = img[30000:].copy()

with open("./" + "train.txt" ,"w") as f:
    for i in range(len(train)):
        f.write("/data2/chihjen/Visual_Recognition/HW2/train/" + str(train[i]))
        f.write("\n")
        
with open("./" + "val.txt" ,"w") as f:
    for i in range(len(val)):
        f.write("/data2/chihjen/Visual_Recognition/HW2/train/" + str(val[i]))
        f.write("\n")