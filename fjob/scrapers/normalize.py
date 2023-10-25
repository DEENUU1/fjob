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


class Normalize:
    @staticmethod
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

    @staticmethod
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

        if "senior" in text or "starszy" in text:
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

        if (
            "director" in text
            or "dyrektor" in text
            or "president" in text
            or "prezes" in text
        ):
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def is_remote(text: str) -> bool:
        if not text:
            return False

        if "remote" in text or "zdalna" in text or "zdalnie" in text:
            return True

        return False

    @staticmethod
    def is_hybrid(text: str) -> bool:
        if not text:
            return False

        if "hybrid" in text or "hybryd" in text:
            return True

        return False
