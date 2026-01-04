from transformers import pipeline

qa = pipeline("question-answering")
print(qa({
    "question": "Who developed Transformers?",
    "context": "Transformers were developed by Hugging Face."
}))

qa = pipeline("question-answering")
print(qa({
    "question": "Who is musk?",
    "context": "Tesla was founded by Elon Musk."
}))
