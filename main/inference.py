# inference.py
from transformers import AutoModelForImageClassification, AutoFeatureExtractor
from PIL import Image
import torch


def predict(image_path, model, feature_extractor):
    image = Image.open(image_path)
    inputs = feature_extractor(images=image, return_tensors="pt").to(device)

    outputs = model(**inputs).logits
    predicted_class_idx = torch.argmax(outputs, dim=-1).item()

    return predicted_class_idx


if __name__ == "__main__":
    model = AutoModelForImageClassification.from_pretrained('./finetuned_mobilenetv2')
    feature_extractor = AutoFeatureExtractor.from_pretrained('./finetuned_mobilenetv2')

    image_path = 'path_to_new_image.jpg'
    predicted_class_idx = predict(image_path, model, feature_extractor)
    print(f"Predicted class: {predicted_class_idx}")
