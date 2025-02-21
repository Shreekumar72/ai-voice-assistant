def process_text(text):
    """
    Simple keyword-based NLP function.
    - Converts text to lowercase.
    - Matches keywords like 'hello' and 'weather'.
    """
    text = text.lower()
    if "hello" in text:
        return "Hi! How can I help you?"
    elif "weather" in text:
        return "Please provide a location to check the weather."
    else:
        return "Sorry, I didn't understand that."
