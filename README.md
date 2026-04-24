# Adversarial-Machine-Learning-Project - FRUITY
## 📌 Introduction
This is basic project on adversarial machine learning. A simple image classification model is created which identifies 5 types of fruits. the model shows decent accuracy on test dataset and custom input. But it fails while trying to classify specially crafted adversarial input images that look similar to their normal counterparts. It is a demonstration of the Carlini-Wagner attack which uses optimisation algorithms and adds perturbation to images which fool the model. Few adversarial samples and their normal counterparts aregiven in the samples foder. Those can be used to test how the model behavaes or custom input can also be used.


## 🚀 Features
Custom CNN model built with PyTorch  
Image classification (5 fruit classes)  
image user input  
Adversarial sample generation (CW attack)  


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


## ⚠️ Limitations
Model training was highly dependent on the dataset and limited computatioal power  
some adversarial examples have slightly noticable changes       
Very simple model for educational purpose  


## 📧 Contact
Feel free to connect or reach out for collaboration!
