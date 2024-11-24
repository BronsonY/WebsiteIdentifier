import re

def clean_text(text):
    """
    Cleans up the given text by removing HTML tags, URLs, special characters,
    extra whitespace, and trimming it.
    """
    text = re.sub(r'<[^>]*?>', '', text)  # Remove HTML tags
    text = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)  # Remove special characters
    text = re.sub(r'\s{2,}', ' ', text)  # Replace multiple spaces with one
    text = text.strip()  # Trim leading/trailing whitespace
    return ' '.join(text.split())  # Normalize spaces
