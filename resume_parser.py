import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(text):
    doc = nlp(text)
    tokens = [
        token.text.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)

