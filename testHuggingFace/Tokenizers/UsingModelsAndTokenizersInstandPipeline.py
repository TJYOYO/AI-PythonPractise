from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load tokenizer and model intand of using pipeline
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Encode input text
inputs = tokenizer("Hugging Face is amazing!", return_tensors="pt")

# Run inference
outputs = model(**inputs)
logits = outputs.logits
pred = torch.argmax(logits, dim=1)

print(pred)  # 1 means positive
