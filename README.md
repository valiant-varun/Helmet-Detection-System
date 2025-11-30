# ⛑️ Real-Time Helmet Detection System

> **A computer vision prototype that monitors rider safety in real-time using Edge AI.**

This project implements a custom-trained **YOLOv8** model deployed on a **Raspberry Pi 3 B+** to detect helmet compliance. Unlike standard object detection demos, this system features **hardware integration**: it triggers a physical alarm circuit (LED/Buzzer) via GPIO pins immediately when a rider is detected without a helmet.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `run_demo.py` | **Main Script.** Loads the TFLite model, runs inference on the webcam, and controls the GPIO alarm. |
| `best_float32.tflite` | **The Brain.** Custom YOLOv8 classification model optimized for Edge devices. |
| `collect_images.py` | **Data Tool.** Custom script used to capture and organize the training dataset. |
| `requirements.txt` | List of Python dependencies (OpenCV, NumPy, TFLite-Runtime). |
| `labels.txt` | Dictionary file mapping model outputs to "helmet" or "no_helmet". |
| `Helmet_detection_Project Report.pdf` | Full documentation of research, methodology, and results. |
| `raspberry pi helmet... .mp4` | Video demonstration of the working prototype. |

---

## 🛠️ Tech Stack & Hardware

### Hardware
* **Raspberry Pi 3 Model B+** (Controller)  
* **USB Webcam** (Input)  
* **LED & 220Ω Resistor** (Output Alarm)  
* **Jumper Wires** (Female-to-Female)  

### Software
* **Model Training:** YOLOv8 (Ultralytics) on Google Colab (T4 GPU).  
* **Inference Engine:** TensorFlow Lite Runtime.  
* **Image Processing:** OpenCV (`cv2`).  
* **Language:** Python 3.11.  

---

## ⚙️ Circuit Diagram (GPIO)

The system uses a visual/audible alarm triggered by **GPIO Pin 18**.

* **Pin 18** → Resistor → LED (+) Long Leg  
* **GND Pin** → LED (-) Short Leg  

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/valiant-varun/Helmet-Detection-System.git
cd Helmet-Detection-System
```

### 2. Set Up Virtual Environment

*Note: This step is critical to avoid NumPy/OpenCV version conflicts on Raspberry Pi OS.*

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

## 🎥 How to Run

1. Connect your webcam and LED circuit.

2. Make sure you are inside the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Run the main script:

   ```bash
   python3 run_demo.py
   ```

**System Logic:**

* **Green Text:** Helmet Detected → Circuit OFF (Safe).
* **Red Text + LED ON:** No Helmet Detected → Alarm Triggered (Unsafe).

---

## 🧠 Methodology

1. **Data Collection:** Used `collect_images.py` to capture ~400 images of "helmet" vs "no_helmet" states to fix background bias issues.
2. **Training:** Trained a YOLOv8-Nano Classification model on Google Colab for 50 epochs.
3. **Optimization:** Exported the model to `.tflite` (Float32) for compatibility with the Raspberry Pi's ARM architecture.
4. **Deployment:** Wrote `run_demo.py` to handle the inference loop and hardware interrupts.

---

## 📈 Future Scope

* Integration with a GSM module to send SMS alerts.
* 3D-printed enclosure for a standalone "Smart Bike" unit.
* Training on night-vision data for low-light performance.

---

**Author:** Varun

```
```
