import openvino.runtime as ov
import numpy as np

model_path = "./model/emotion_model.xml"
core = ov.Core()
model = core.read_model(model_path)
compiled_model = core.compile_model(model, "CPU")
input_layer = compiled_model.input(0)
output_layer = compiled_model.output(0)

def predict_emotion(text):
    # Simulate encoding the text into a numerical format (e.g., embeddings)
    text_embedding = np.random.rand(1, 300).astype(np.float32)
    result = compiled_model([text_embedding])[output_layer]
    emotion_index = np.argmax(result)
    emotions = ["Happy", "Sad", "Neutral"]
    return emotions[emotion_index]

def get_emotional_response(emotion):
    responses = {
        "Happy": "That's great to hear! How can I assist you today?",
        "Sad": "I'm here for you. Can you tell me more about what's bothering you?",
        "Neutral": "Thank you for sharing. Let me know how I can help."
    }
    return responses.get(emotion, "Thank you for sharing.")

def chatbot_response(message):
    emotion = predict_emotion(message)
    return f"I detected that you are feeling {emotion}. Let's talk about it."
