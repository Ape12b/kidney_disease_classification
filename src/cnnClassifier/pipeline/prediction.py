import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        model=load_model(os.path.join("artifacts", "model_training", "model.h5"))
        test_image=image.load_image(self.filename, target_size=(224, 224))
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image, axix=0)
        
        result=np.argmax(model.predict(test_image), axis=1)
        
        print(result)
        return [{"image": "Tumor" if result[0] == 1 else "Normal"}]