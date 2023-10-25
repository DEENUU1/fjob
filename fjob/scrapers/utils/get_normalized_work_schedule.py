from typing import Optional, List


def get_normalized_work_schedule(text: str) -> Optional[str]:
    result = None
    if not text:
        return result

    if "fulltime" in text:
        result = "fulltime"

    if "parttime" in text:
        result = "parttime"

    if "halftime" in text:
        result = "halftime"

    if "seasonal" in text:
        result = "seasonal"

    if "additional" in text:
        result = "additional"

    return result
