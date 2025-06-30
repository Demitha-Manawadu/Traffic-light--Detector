# 🚦 Traffic Light Detector — YOLOv8

A machine learning project to **detect traffic lights and classify their colors** (red, yellow, green) using a custom-trained YOLOv8 model.

This project:
✅ Uses a **custom dataset**  
✅ Was **trained on Google Colab**  
✅ Runs locally on **PyCharm**  
✅ Supports external GPU to accelerate inference and reduce runtime

---

## 📸 Demo Images

Here’s a glimpse of the project in action:

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/9d3675f7-9a50-4706-b5ab-fa528a1a919b/4c6cd9d3-020d-4995-8a60-215946b45c6c.png" width="300"/></td>
    <td><img src="https://github.com/user-attachments/assets/f922bfc3-f22c-4af3-bda0-5574d255da83/a9da273f-62bd-481e-97b5-28e671b7851d.png" width="300"/></td>
  </tr>
  <tr>
    <td align="center">Training Loss Graph</td>
    <td align="center">mAP Curve during Training</td>
  </tr>
</table>

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/2dff8f84-5033-4b9b-985e-2c85b8ec1b1c/WhatsApp%20Image%202025-06-30%20at%2016.50.43_f518e8f6.jpg" width="300"/></td>
    <td><img src="https://github.com/user-attachments/assets/7efbfb99-e38d-4f28-85d9-29a356a46024/WhatsApp%20Image%202025-06-30%20at%2016.51.59_976077a3.jpg" width="300"/></td>
  </tr>
  <tr>
    <td align="center">Detection Example 1</td>
    <td align="center">Detection Example 2</td>
  </tr>
</table>

Replace the image URLs above with your own images from GitHub uploads if the links change.

---

## 🚀 Project Workflow

### 1. Data Collection & Annotation

- Images of traffic lights captured from streets and public datasets.
- Classes labeled:
  - red_light
  - green_light
  - yellow_light

Annotations created using **Roboflow** and exported in YOLOv8 format.

---

### 2. Model Training (Google Colab)

The model was trained in Google Colab using:

```bash
yolo detect train model=yolov8l.pt \
    data=/content/traffic-lights/data.yaml \
    epochs=50 imgsz=640
