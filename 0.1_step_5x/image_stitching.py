import cv2
import numpy as np
import os

STEP_SIZE = 0.1   # in mm
print(int((STEP_SIZE*1000/50)*24))

folder_path = r'C:\Users\BARC\Desktop\FCRIT\FCRIT_SCANS\0.1_step_5x\5.00'
contents = os.listdir(folder_path)

prev_img = None
for i in range(len(contents)):
    path = os.path.join(folder_path, contents[i])
    
    if i == 0:
        base_img = cv2.imread(path)
        prev_img = base_img
    else:
        img = (cv2.imread(path))[:, -int((STEP_SIZE*1000/50)*24):]

        zeros_to_add = np.zeros((1024, 1040, 3), dtype=np.uint8)
        result = np.hstack((img, zeros_to_add))

        concatenated_image = cv2.hconcat([prev_img, result])
        concatenated_image = concatenated_image[:, :-1040]

        prev_img = concatenated_image

print(os.path.join(folder_path, "concatenated.png"))
cv2.imwrite(os.path.join(folder_path, "concatenated.png"), concatenated_image)
        

