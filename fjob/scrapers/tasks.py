from .olx import run as run_olx
from .pracujpl import run as run_pracujpl


# Add celery later
def task_run_olx(city: str, query: str = None) -> None:
    run_olx(city=city, query=query)  # Add delay


# Add celery later
def task_run_pracujpl(city: str, query: str = None, region: str = None) -> None:
    run_pracujpl(query=query, region=region, city=city)  # Add delay
