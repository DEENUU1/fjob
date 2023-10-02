from .olx import run as run_olx
from .pracujpl import run as run_pracujpl
from typing import List, Dict, Any
from celery import shared_task


@shared_task()
def run_scrapers() -> List[Dict[str, Any]]:
    olx_data = run_olx(False, False, "Zduńska Wola")
    pracujpl_data = run_pracujpl(False, False, "Zduńska Wola")
    return olx_data + pracujpl_data
