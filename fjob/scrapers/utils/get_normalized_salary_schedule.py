from typing import Optional


def get_normalized_salary_schedule(text: str) -> Optional[int]:
    result = None
    if not text:
        return result

    text = text.lower()
    if "monthly" in text or "miesięcznie" in text:
        return 1
    if "yearly" in text or "rocznie" in text:
        return 2
    if "hourly" in text or "godzinowo" in text or "godzinowa" in text:
        return 3

    return result
