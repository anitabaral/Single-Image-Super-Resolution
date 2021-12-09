
import cv2
import PIL
import numpy as np
from PIL import Image

from project_modules.sisr.load_data import LoadData

class Preprocessing:
    def __init__(self):
        self.x_train = LoadData.load_data()

    def hr_images(self, images):
        images_hr = np.array(images)
        return images_hr

    def lr_images(self, images_real, downscale):
        images = []
        for img in range(len(images_real)):
            images.append(
                np.array(
                    PIL.Image.fromarray(images_real[img]).resize(
                        [
                            images_real[img].shape[1] // downscale,
                            images_real[img].shape[0] // downscale
                        ],
                        resample=PIL.Image.BICUBIC)))
        images_lr = np.array(images)
        # print('**** {}'.format(len(images_lr)))
        return images_lr

    def preprocess_HR(self, x):
        return (np.divide(np.array(x, dtype = np.float32), 127.5) -
            np.ones_like(x, dtype=np.float32))

    
    def deprocess_HR(self, input_data):
        input_data = (input_data + 1) * 127.5
        return input_data.astype(np.uint8)

    def preprocess_LR(self, x):
        return np.divide(x.astype(np.float32), 255.)

    def deprocess_LR(self, x):
        x = np.clip(x * 255, 0, 255)
        return x.astype(np.uint8)

    def resize_images(self, img):

        img_height = 340
        img_width = 480
        resized_images = []
        resized_images_rgb = []
        print(img.shape)
        for i in range(len(img)):
            resized_images.append(
                np.array(
                    PIL.Image.fromarray(img[i]).resize(
                        [img_width, img_height], resample=PIL.Image.BICUBIC)))
            resized_images_rgb.append(cv2.cvtColor(resized_images[i].copy(), cv2.COLOR_BGR2RGB))

        return resized_images_rgb

    def preprocessing(self):
        self.x_train = self.hr_images(self.x_train)
        x_train_hr_resized = self.resize_images(self.x_train)
        x_train_hr = self.preprocess_HR(x_train_hr_resized)

        x_train_lr = self.lr_images(x_train_hr_resized, 4)
        x_train_lr = self.preprocess_LR(x_train_lr)
        print(x_train_hr.shape, x_train_lr.shape)
        return x_train_lr, x_train_hr
