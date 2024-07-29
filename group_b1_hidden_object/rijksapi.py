import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import requests
import json
import wget

from segment_anything import sam_model_registry, SamPredictor
from ultralytics import YOLO
from PIL import Image
from openai import OpenAI



def importing_art(API_key, object_ids):
    """
    Function to get URL and additional artwork information, such as:
        - type(s) of artwork
        - title of artwork
        - artist and creation date
        - artwork description
    """
    
    artwork_info = {}
    
    for object_id in object_ids:
    
        # get object data for each painting
        response = requests.get(f"https://www.rijksmuseum.nl/api/en/collection/{object_id}?key={API_key}")
        data = response.json()

       # specify useful identifiers 
        image_url = data['artObject']['webImage']['url']
        types = data["artObject"]["objectTypes"]
        title = data["artObject"]["title"]
        info = data["artObject"]["label"]["makerLine"]
        description = data["artObject"]["label"]["description"]

        artwork_info[object_id] = (image_url, types, title, info, description)
    
    return artwork_info
