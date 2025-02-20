import torch
from torch import nn, optim

from FaceRecognition import model
from data_preprocessing import train_dataset, train_loader

# 冻结除最后一层外的所有层
for param in model.parameters():
    param.requires_grad = False

# 替换最后一层
model.classifier[1] = nn.Linear(model.classifier[1].in_features, len(train_dataset.classes))

# 使用Adam优化器
optimizer = optim.Adam(model.parameters(), lr=0.0001)

# 损失函数
criterion = nn.CrossEntropyLoss()

# 微调模型
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
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
