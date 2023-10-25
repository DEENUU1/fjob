from typing import List, Optional


def get_normalized_contract_type(text: str) -> Optional[str]:
    result = None
    if not text:
        return result

    if "selfemployment" in text:
        result = "B2B"

    if "zlecenie" in text:
        result = "Umowa zlecenie"

    if "contract" in text:
        result = "Umowa o pracę"

    return result
