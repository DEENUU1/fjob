from typing import Optional


def get_normalized_type(text: str) -> Optional[int]:
    result = None
    if not text:
        return result

    text = text.lower()

    if text == "brutto":
        result = 1
    elif text == "netto":
        result = 2

    return result
