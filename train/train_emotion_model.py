import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnx

# Simulated dataset (you can replace this with your actual data)
X = np.random.rand(1000, 300)  # Example text embeddings
y = np.random.choice([0, 1, 2], size=1000)  # Example emotion labels: Happy, Sad, Neutral

# Train-test split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForest model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Convert the trained model to ONNX format
initial_type = [('float_input', FloatTensorType([None, X_train.shape[1]]))]
onnx_model = convert_sklearn(clf, initial_types=initial_type)

# Save the ONNX model to a file
onnx.save_model(onnx_model, "emotion_model.onnx")

print("Model saved as emotion_model.onnx")
