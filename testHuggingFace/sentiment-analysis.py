from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("I love Hugging Face!"))


print(classifier("I hate waiting in long lines."))