from .dynamic.olx import run as run_olx
from .dynamic.pracujpl import run as run_pracujpl
from typing import List, Dict, Any
from celery import shared_task


@shared_task()
def run_scrapers() -> List[Dict[str, Any]]:
    olx_data = run_olx("Zduńska Wola")
    pracujpl_data = run_pracujpl("Zduńska Wola")
    return olx_data + pracujpl_data
