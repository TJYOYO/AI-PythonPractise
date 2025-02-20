# model_evaluation.py
import torch
from torch.utils.data import DataLoader
from transformers import AutoModelForImageClassification
from data_preprocessing import load_data  # 导入数据加载函数


def evaluate_model(model, test_loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)

            outputs = model(inputs).logits
            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = correct / total
    print(f'Accuracy: {accuracy * 100:.2f}%')


if __name__ == "__main__":
    _, test_loader = load_data('path_to_train_data', 'path_to_test_data')
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = AutoModelForImageClassification.from_pretrained('./finetuned_mobilenetv2')
    evaluate_model(model, test_loader, device)
