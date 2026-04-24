import torch
from PIL import Image
from torchvision import transforms
from model import get_model

class_names = ["apple", "banana", "grapes", "mango", "strawberry"]

model = get_model()
model.load_state_dict(torch.load("model_weights.pth", map_location="cpu"))
model.eval()


test_transform = transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))
])


def predict(image_path):
    image = Image.open(image_path).convert("RGB")
    x = test_transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(x)
        _, pred = torch.max(output, 1)

    return class_names[pred.item()]


import sys

if __name__ == "__main__":
    image_path = sys.argv[1]
    result = predict(image_path)
    print("This is an image of", result)
