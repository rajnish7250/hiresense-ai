#preprocessing.py
import re
from typing import Dict
import string

def clean_text(text: str, preserve_structure: bool = True) -> str:
    """
    Clean and normalize text while preserving important resume structure.

    Args:
        text (str): Raw input text
        preserve_structure (bool): If True, keeps sections and formatting

    Returns:
        str: Cleaned text
    """

    if not text:
        return ""

    # Normalize unicode (remove weird chars but keep meaning)
    text = text.encode("ascii", "ignore").decode()

    # Lowercase (optional — good for embeddings)
    text = text.lower()
    
    text = text.translate(str.maketrans('', '', string.punctuation))

    if preserve_structure:
        # Keep section breaks and bullets
        text = re.sub(r"[•●▪►]", "-", text)

        # Preserve emails, URLs, and tech terms
        # Keep: letters, numbers, space, ., @, +, -, :, /
        text = re.sub(r"[^a-z0-9\s\.\@\+\-\:\/]", " ", text)

        # Normalize spacing but keep line breaks
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n+", "\n", text)

    else:
        # For embeddings (more aggressive cleaning)
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        text = re.sub(r"\s+", " ", text)

    return text.strip()
