import pickle
import librosa
import numpy as np
import time

with open(r"C:\Users\Decent\Desktop\ML Project\deepfake_gui\models\voice_model.pkl", "rb") as f:
    voice_model = pickle.load(f)
with open(r"C:\Users\Decent\Desktop\ML Project\deepfake_gui\models\voice_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def process_audio(path, callback):
    callback("Predicting deepfake probability...", 90)
    callback("Scaling features...", 60)
    y, sr = librosa.load(path, sr=None)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=26).T, axis=0)
    X = scaler.transform([mfcc])

    callback("Predicting deepfake probability...", 90)

    # Get both class probabilities
    probs = voice_model.predict_proba(X)[0]

    # Safely detect class labels (some models use 0/1, some use 'Fake'/'Real')
    classes = voice_model.classes_.tolist()
    if isinstance(classes[0], str):
        fake_index = classes.index("Fake")
        real_index = classes.index("Real")
    else:
        fake_index = classes.index(1)
        real_index = classes.index(0)

    fake_prob = probs[fake_index]
    real_prob = probs[real_index]

    # Determine the label
    label = "Fake" if fake_prob > real_prob else "Real"

    callback(f"Fake Confidence: {fake_prob * 100:.2f}% | Real Confidence: {real_prob * 100:.2f}%", 95)
    callback(f"Audio classified as: {label}", 100)

    return label, fake_prob


