import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
import time
import RPi.GPIO as GPIO

# --- SETUP ---
MODEL_FILE = 'best_float32.tflite'
LABEL_FILE = 'labels.txt'

# --- ALARM SETUP ---
ALARM_PIN = 18 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ALARM_PIN, GPIO.OUT)
GPIO.output(ALARM_PIN, GPIO.LOW) # Start with alarm OFF
# ---------------------

# Load labels
with open(LABEL_FILE, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Load TFLite model
interpreter = tflite.Interpreter(model_path=MODEL_FILE)
interpreter.allocate_tensors()

# Get model input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("--- Starting Demo... Press 'q' to quit ---")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame")
        break

    # 1. Pre-process the image
    image_resized = cv2.resize(frame, (width, height))
    input_data = np.expand_dims(image_resized, axis=0)
    input_data = input_data.astype(np.float32) / 255.0

    # 2. Run Inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    scores = output_data[0]

    # 3. Get the Top Result
    top_class_index = np.argmax(scores)
    top_label = labels[top_class_index]
    top_score = scores[top_class_index]

    # 4. Implement Logic
    alarm_text = ""
    text_color = (0, 255, 0) # Green

    # Set a confidence threshold (e.g., 60%)
    if top_label == 'no_helmet' and top_score > 0.6:
        alarm_text = "!!! ALARM ON !!!"
        text_color = (0, 0, 255) # Red
        GPIO.output(ALARM_PIN, GPIO.HIGH) # --- ALARM ON ---
    else:
        alarm_text = f"{top_label}: {top_score*100:.0f}%"
        GPIO.output(ALARM_PIN, GPIO.LOW) # --- ALARM OFF ---
    
    # 5. Draw on the screen
    cv2.putText(frame, alarm_text, (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, text_color, 3)

    # Display the frame
    cv2.imshow('Helmet Detection Demo', frame)

    # 6. Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()
print("--- Demo Finished ---")