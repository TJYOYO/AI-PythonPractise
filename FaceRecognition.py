from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import torch

# 加载预训练的MobileNetV2模型和特征提取器
model_name = "google/mobilenet_v2_1.0_224"
model = AutoModelForImageClassification.from_pretrained(model_name)
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)