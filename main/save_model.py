# save_model.py
from transformers import AutoModelForImageClassification


def save_model(model, save_path='./finetuned_mobilenetv2'):
    model.save_pretrained(save_path)
    print(f"Model saved at {save_path}")


if __name__ == "__main__":
    # 假设模型已经微调完成并传递到此处
    model = AutoModelForImageClassification.from_pretrained("google/mobilenet_v2_1.0_224")
    save_model(model)
