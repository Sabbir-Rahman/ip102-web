import io
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision
from torchvision import models
from PIL import Image

# load model
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.input_size = input_size
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size, num_classes)  
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        # no activation and no softmax at the end
        return out

input_size = 784 # 28x28
hidden_size = 500 
num_classes = 10
model = models.resnet152(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 102)

PATH = "resnet152.pt"
model.load_state_dict(torch.load(PATH))
model.eval()

# image -> tensor
def  transform_image(image_bytes):
  transform = transforms.Compose([
        transforms.Resize((299,299)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

  image = Image.open(io.BytesIO(image_bytes))
  return transform(image).unsqueeze(0)

# predict
def get_prediction(image_tensor):
  outputs = model(image_tensor)
  # max returns
  _, predicted = torch.max(outputs.data, 1)
  return predicted

