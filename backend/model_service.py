import os
import numpy as np
import random
import time

# Path to the pre-trained model
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'vgg16_malignant_benign.h5')

model = None


def load_ai_model():
    """Attempt to load the Keras model. Falls back to mock if TF is unavailable."""
    global model
    try:
        if os.path.exists(MODEL_PATH):
            from tensorflow.keras.models import load_model as keras_load
            model = keras_load(MODEL_PATH)
            print('[OK] AI model loaded successfully.')
        else:
            print(f'[INFO] Model file not found at {MODEL_PATH}. Using mock predictions.')
    except Exception as e:
        model = None
        print(f'[WARN] Could not load AI model ({e}). Using mock predictions.')


def predict(image_path):
    """
    Classify a skin lesion image as Benign or Malignant.
    Returns dict with 'label' and 'confidence' keys.
    """
    if model is not None:
        # ---- Real model inference ----
        from tensorflow.keras.preprocessing import image as keras_image
        img = keras_image.load_img(image_path, target_size=(224, 224))
        img_array = keras_image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_array)[0][0]

        if prediction > 0.5:
            return {'label': 'Malignant', 'confidence': round(float(prediction) * 100, 2)}
        else:
            return {'label': 'Benign', 'confidence': round((1 - float(prediction)) * 100, 2)}
    else:
        # ---- Mock prediction for demo ----
        time.sleep(1.5)
        is_malignant = random.choice([True, False])
        conf = round(random.uniform(60.0, 98.5), 2)
        return {'label': 'Malignant' if is_malignant else 'Benign', 'confidence': conf}
