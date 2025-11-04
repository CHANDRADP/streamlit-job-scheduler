# Streamlit Job Scheduler

A simple and interactive Streamlit-based UI to configure and manage scheduled jobs — either **one-time** or **cron-based**.

### 🚀 Features
- One-time scheduling (date + time)
- Cron scheduling with flexible frequency (daily, weekly, monthly, etc.)
- Multi-hour and multi-day support in a single cron expression
- Human-readable cron descriptions
- Pytest unit tests

### 🧩 Usage

```bash
pip install streamlit-job-scheduler
```
 ### Run as Streamlit App

 ```bash
 streamlit run -m streamlit_job_scheduler/ui.py
 ```