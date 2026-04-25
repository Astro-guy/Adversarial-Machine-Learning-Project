# Adversarial-Machine-Learning-Project - FRUITY
## 📌 Introduction
This project demonstrates a practical security weakness in machine learning systems using Adversarial Machine Learning.  
A simple CNN based image classification model is deveoped which identifies 5 types of fruits. The model shows decent accuracy on test dataset and custom input. But it fails while trying to classify specially crafted adversarial input images that look similar to their normal counterparts. It is a demonstration of the Carlini-Wagner attack. This highlights a critical concern in real-world ML systems - models can be fooled without obvious changes to input data. Few adversarial samples and their normal counterparts are given in the samples foder. Those can be used to test how the model behavaes or custom input can also be used.


## 🚀 Features
Custom CNN model built with PyTorch  
Image classification (5 fruit classes)  
Support for user input  
Adversarial sample generation (CW attack)  
Demonstration of model vulnerability to adversarial inputs  


## 📊 Model Details
Test Accuracy: ~0.71–0.74  
Dataset: fruit dataset (5 classes, ~2000 images each)  
Input size: 128×128 RGB images  


## ⚙️ Installation
```bash
git clone https://github.com/Astro-guy/Adversarial-Machine-Learning-Project.git
cd Adversarial-Machine-Learning-Project
pip install -r requirements.txt
```

## 🖼️ Usage
python prediction.py path/to/your/image.jpg


## 📥 Model Weights
model_weights.pth


## 🧠 Adversarial ML Perspective
Adversarial Machine Learning focuses on exploiting weaknesses in models by introducing small perturbations to inputs.  
- The CW attack uses optimization techniques to generate minimal but effective perturbations  
- Generated adversarial samples can bypass model predictions  
- Demonstrates how ML systems can be security-sensitive in deployment  


## ⚠️ Limitations
Model training was highly dependent on the dataset and limited computatioal power  
Some adversarial perturbations may be slightly noticeable  
Model is intentionally simple for demonstration purposes  


## 📧 Contact
Feel free to connect or reach out for collaboration!
