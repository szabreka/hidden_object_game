from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import cv2
import requests
import json
import pandas as pd

from segment_anything import sam_model_registry, SamPredictor
from PIL import Image

# load in historical context csv as pandas dataframe
context_df = pd.read_csv('his_context_db_brief.csv', sep=",")

# load pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# define remote image
source = 'static/SK-A-4821.jpg'

# run inference on the source using YOLO
results = model(source, conf=0.1, save=False, augment=True)  # list of Results objects

# showing the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    #im.show()  # show image


item_names = []
object_all = []
object_data = []

# Part 1: Extract information of objects
for result in results:
    for box in result.boxes:
        class_id = int(box.data[0][-1])
        item_names.append(model.names[class_id])

for result in results:
    for i in range(len(result.boxes)):
        names = item_names[i]  
        conflvl = float(result.boxes.conf[i])
        xyxy = result.boxes.xyxy[i]  
        object_all.append((names, conflvl, xyxy))

# Calculate middle coordinates for each bounding box
object_data = [(name, conflvl, ((box[0] + box[2]) / 2).item(), ((box[1] + box[3]) / 2).item()) for name, conflvl, box in object_all]

# calculate top left and bottom right coords for each box
coord_data = [(name, conflvl, box[0].item(), box[2].item(), box[1].item(), box[3].item()) for name, conflvl, box in object_all]

# sort based on confidence levels (in descending order)
sorted_object_data = sorted(object_data, key=lambda x: x[1], reverse=True)

# filter out objects with the same label and ensure separation
unique_labels = set()
filtered_object_data = []

for name, conflvl, x_mid, y_mid in object_data:
    is_unique = True
    for existing_name, _, existing_x_mid, existing_y_mid in filtered_object_data:
        # threshold for proximity
        proximity_threshold = 100.0  # 10 pixels

        # check if coordinates are close
        if abs(x_mid - existing_x_mid) < proximity_threshold and abs(y_mid - existing_y_mid) < proximity_threshold:
            is_unique = False
            break

    if is_unique and name not in unique_labels:
        filtered_object_data.append((name, conflvl, x_mid, y_mid))
        unique_labels.add(name)

# sort based on confidence levels (in descending order) for filtered data
sorted_filtered_object_data = sorted(filtered_object_data, key=lambda x: x[1], reverse=True)

coord_data_filtered = [(name, conflvl, box[0].item(), box[2].item(), box[1].item(), box[3].item()) for name, conflvl, box in object_all if any(name == x[0] and conflvl == x[1] for x in sorted_filtered_object_data)]

# select the top 5 entries
top_5_entries2 = sorted_filtered_object_data[:5]
top_5_coords2 = coord_data_filtered[:5]

image = cv2.imread(source)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

top_5_coordinates2= []
def get_xy_data2(object_data):
    for n in range(0,5):
        label_data = object_data[n][0]
        x_data = object_data[n][2]
        y_data = object_data[n][3]
        top_5_coordinates2.append((label_data, x_data,y_data))

def get_image_shape2():
    shape = image.shape
    return(shape)

top_5_corners2= []
def get_corner_data2(coord_data):
    for n in range(0,5):
        top_left_x = coord_data[n][2]
        top_left_y = coord_data[n][4]
        bottom_right_x = coord_data[n][3]
        bottom_right_y = coord_data[n][5]
        top_5_corners2.append((top_left_x, top_left_y,bottom_right_x, bottom_right_y))