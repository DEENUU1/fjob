from typing import List, Optional


class EXPERIENCES:
    JUNIOR = "Junior"
    MIDDLE = "Middle"
    SENIOR = "Senior"
    LEAD = "Lead"
    MANAGER = "Manager"
    DIRECTOR = "Director"
    C_LEVEL = "C-Level"
    PRINCIPAL = "Principal"


def get_normalized_experience_level(text: str) -> List[Optional[str]]:
    result = []
    if not text:
        return result

    text = text.lower()
    if "junior" in text or "młodszy" in text or "entry" in text:
        result.append(EXPERIENCES.JUNIOR)

    if (
        "mid" in text
        or "intermediate" in text
        or "regular" in text
        or "experienced" in text
    ):
        result.append(EXPERIENCES.MIDDLE)

    if "senior" in text or "starszy":
        result.append(EXPERIENCES.SENIOR)

    if (
        "lead" in text
        or "lider" in text
        or "kierownik" in text
        or "brygadzista" in text
    ):
        result.append(EXPERIENCES.LEAD)

    if "manager" in text or "menedżer" in text:
        result.append(EXPERIENCES.MANAGER)

    if "director" in text or "dyrektor" in text or "president" or "prezes":
        result.append(EXPERIENCES.DIRECTOR)

    if (
        "c-level" in text
        or "ceo" in text
        or "cfo" in text
        or "cto" in text
        or "chief" in text
    ):
        result.append(EXPERIENCES.C_LEVEL)

    if (
        "principal" in text
        or "przedstawiciel" in text
        or "specjalista" in text
        or "ekspert" in text
        or "expert" in text
        or "specjalist" in text
    ):
        result.append(EXPERIENCES.PRINCIPAL)

    return result
