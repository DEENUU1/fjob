from .olx import run as run_olx
from .pracujpl import run as run_pracujpl


# Add celery later
def task_run_olx():
    run_olx()  # Add delay


# Add celery later
def task_run_pracujpl():
    run_pracujpl()  # Add delay
