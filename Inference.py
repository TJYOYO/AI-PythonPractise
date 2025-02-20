# 加载微调后的模型
import torch
from transformers import AutoModelForImageClassification, AutoFeatureExtractor

from FineTuning import device
from data_preprocessing import train_dataset

model = AutoModelForImageClassification.from_pretrained('./finetuned_mobilenetv2')
feature_extractor = AutoFeatureExtractor.from_pretrained('./finetuned_mobilenetv2')

# 推理一个新的图像
from PIL import Image

image = Image.open('path_to_new_image.jpg')
inputs = feature_extractor(images=image, return_tensors="pt").to(device)

outputs = model(**inputs).logits
predicted_class_idx = torch.argmax(outputs, dim=-1).item()

# 输出预测类别
print(f'Predicted class: {train_dataset.classes[predicted_class_idx]}')
