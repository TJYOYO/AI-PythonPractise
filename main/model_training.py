# model_training.py
import torch
from torch import nn, optim
from transformers import AutoModelForImageClassification
from data_preprocessing import load_data  # 导入数据加载函数


def train_model(train_loader, device):
    model = AutoModelForImageClassification.from_pretrained("google/mobilenet_v2_1.0_224")

    # 冻结除最后一层外的所有层
    for param in model.parameters():
        param.requires_grad = False

    # 替换最后一层
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, len(train_loader.dataset.classes))

    # 使用Adam优化器
    optimizer = optim.Adam(model.parameters(), lr=0.0001)
    criterion = nn.CrossEntropyLoss()

    model.to(device)

    num_epochs = 5
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()

            outputs = model(inputs).logits
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        print(f"Epoch {epoch + 1}, Loss: {running_loss / len(train_loader)}")

    return model


if __name__ == "__main__":
    train_loader, _ = load_data('D:/datasets/train', 'D:/datasets/test')
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = train_model(train_loader, device)
