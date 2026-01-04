from transformers import pipeline

# Load a pre-trained text generation model
generator = pipeline("text-generation", model="gpt2")

# Generate text
result = generator("Once upon a time,", max_length=50, num_return_sequences=1)
print(result[0]["generated_text"])