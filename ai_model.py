# ai_model.py
from keras.models import load_model
import numpy as np
from PIL import Image, ImageOps

# 1️⃣ Modell laden
# Stelle sicher, dass keras_model.h5 im gleichen Ordner wie ai_model.py liegt
model = load_model("keras_model.h5", compile=False)

# 2️⃣ Labels einlesen
with open("labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

def predict(image: Image.Image):
    """
    Vorhersage für ein Bild
    - image: PIL Image
    Returns: (Klasse, Confidence)
    """
    # 1. Bild auf RGB konvertieren
    image = image.convert("RGB")
    
    # 2. Größe auf 224x224 anpassen (wie beim Training)
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    
    # 3. In numpy array umwandeln
    image_array = np.asarray(image).astype(np.float32)
    
    # 4. Normalisieren (wie beim Training, z.B. -1 bis 1)
    normalized = (image_array / 127.5) - 1
    
    # 5. Batch-Dimension hinzufügen
    data = np.expand_dims(normalized, axis=0)
    
    # 6. Vorhersage
    prediction = model.predict(data)
    
    # 7. Klasse mit höchster Wahrscheinlichkeit
    index = np.argmax(prediction)
    confidence = float(prediction[0][index])
    
    return class_names[index], confidence
