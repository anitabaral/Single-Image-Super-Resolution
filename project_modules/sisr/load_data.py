import os

from pathlib import Path

import cv2

from utils.variables import var
from utils.logger import logger


class LoadData:
    def __init__(self):
        pass

    def __repr__(self):
        return "{self.__class__.__name__}({self.path})".format(self=self)

    def load_data():
        train_path = Path(var.train_data_path)
        train_images = []
        if os.path.isdir(train_path):
            train_data = os.listdir(train_path)
            if len(train_data) == 0:
                raise ValueError("There are no images in training folder.")
        else:
            raise ValueError("The training folder path doesn't exist")

        train_data = os.listdir(train_path)

        for sample in train_data:
            img_path = train_path / str(sample)
            #raise exception incase unable to read the image
            train_hr_images = cv2.imread(str(img_path))
            train_images.append(train_hr_images)
        
        return train_images