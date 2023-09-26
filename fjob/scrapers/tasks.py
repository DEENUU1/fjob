from .olx import run as run_olx
from .pracujpl import run as run_pracujpl


# Add celery later
def task_run_olx(city: str) -> None:
    run_olx(city)  # Add delay


# Add celery later
def task_run_pracujpl(query: str, region: str, city: str) -> None:
    run_pracujpl(query, region, city)  # Add delay
