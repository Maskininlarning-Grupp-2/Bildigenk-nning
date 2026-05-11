from flask import Blueprint, request, jsonify
import torch
import torchvision.models as models
import torch.nn as nn
from torchvision import transforms
from PIL import Image

api_bp = Blueprint('api', __name__)

classes = ['butterfly', 'cat', 'chicken', 'cow', 'dog',
           'elephant', 'horse', 'sheep', 'spider', 'squirrel']

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 10)
model.load_state_dict(torch.load(
    'models/resnet18_animals.pth', map_location='cpu'))
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

@api_bp.route('/api/evaluate', methods=['POST'])
def evaluate_image():

    if 'file' not in request.files:
        return jsonify({"error": "Ingen fil hittades"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "Ingen fil är vald ännu"}), 400

    image = Image.open(file).convert('RGB')
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        predicted = outputs.argmax(1).item()
        confidence = torch.softmax(outputs, dim=1)[0][predicted].item()

    return jsonify({
        "success": True,
        "animal": classes[predicted],
        "accuracy": f"{confidence*100:.1f}%"
    })
