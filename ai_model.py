import numpy as np
from PIL import ImageOps
from tensorflow.keras.models import load_model

model = load_model("keras_model.h5", compile=False)
labels = ["Schuh", "Hose", "Shirt"]  # Einfaches Beispiel, oder labels.txt laden

def predict(image):
    image = ImageOps.fit(image, (224,224))
    arr = np.asarray(image).astype(np.float32)/127.5 - 1
    data = np.expand_dims(arr, 0)
    prediction = model.predict(data)
    index = np.argmax(prediction)
    return labels[index]
