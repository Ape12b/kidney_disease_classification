import numpy as np
from tensorflow.keras.models import load_model
from keras.utils import load_img, img_to_array
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        model=load_model(os.path.join("model", "model.h5"))
        test_image=load_img(self.filename, target_size=(224, 224))
        test_image=img_to_array(test_image)
        test_image=np.expand_dims(test_image, axis=0)
        
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]