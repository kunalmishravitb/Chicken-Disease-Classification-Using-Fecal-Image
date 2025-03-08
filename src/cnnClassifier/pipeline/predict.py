import numpy as np
from tensorflow.keras.models import load_model # Used to load the train model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename # This constructor will take the filename because user will upload one image and that image it will exist
    

    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts", "training", "model.h5")) # It is for running on the system
        #model = load_model(os.path.join("model", "model.h5")) # It is for running on AWS

        # Preprocessing the image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224)) # loading the image
        test_image = image.img_to_array(test_image) # Converting image to array
        test_image = np.expand_dims(test_image, axis=0) # Expanding the dimensions
        result = np.argmax(model.predict(test_image), axis=1) # After preprocessing the image at last I am giving to the model
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{ "image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]

