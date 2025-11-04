# streamlit_job_scheduler/tests/test_ui.py
import pytest
from ..scheduler import SchedulerConfig

def import_scheduler_ui():
    from streamlit_job_scheduler.ui import job_scheduler
    return job_scheduler

def test_ui_runs_cron_job(monkeypatch):
    """Smoke test: ensure the cron UI runs and returns a valid result without errors."""
    config = SchedulerConfig(schedule_type="cron", pre_config={"frequency": "Daily"})
    result = import_scheduler_ui()(config)
    assert isinstance(result, dict)
    assert "type" in result
    assert result["type"] == "cron"


def test_ui_runs_one_time(monkeypatch):
    """Smoke test: ensure one-time UI runs and returns expected structure."""
    config = SchedulerConfig(schedule_type="one-time")
    result = import_scheduler_ui()(config)
    assert isinstance(result, dict)
    assert result["type"] == "one-time"
    # should contain date/time fields
    assert "schedule_time" in result
    assert result["schedule_time"] is not None


def test_ui_invalid_config(monkeypatch):
    """Ensure invalid or empty config does not crash the UI."""
    config = SchedulerConfig(schedule_type=None)
    result = import_scheduler_ui()(config)
    assert isinstance(result, dict)
    assert "type" in result
