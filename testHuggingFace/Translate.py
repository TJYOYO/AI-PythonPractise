from transformers import pipeline
import sys

def translate_text(text):
    try:
        translator = pipeline("translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh", device=0)
        return translator(text)
    except ValueError as e:
        print("Error: Make sure to install sentencepiece first:")
        print("pip install sentencepiece")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    result = translate_text("Hello, how are you?")
    print(result)
