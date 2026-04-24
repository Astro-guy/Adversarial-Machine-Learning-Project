# model.py

import torch.nn as nn

def get_model(num_classes=5):
    model = nn.Sequential(
        nn.Conv2d(3, 32, 3, padding=1),
        nn.BatchNorm2d(32),
        nn.ReLU(),
        nn.MaxPool2d(2),

        nn.Conv2d(32, 64, 3, padding=1),
        nn.BatchNorm2d(64),
        nn.ReLU(),
        nn.MaxPool2d(2),

        nn.Conv2d(64, 128, 3, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU(),

        nn.AdaptiveAvgPool2d((4,4)),

        nn.Flatten(),
        nn.Linear(128*4*4, 128),
        nn.ReLU(),
        nn.Dropout(0.5),

        nn.Linear(128, num_classes)
    )

    return model
