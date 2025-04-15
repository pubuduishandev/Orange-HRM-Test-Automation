import os
from datetime import datetime

LOG_DIR = "Logs"
os.makedirs(LOG_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = os.path.join(LOG_DIR, f"test_{timestamp}_log_report.txt")

execution_log = []

def initialize_log():
    with open(LOG_FILE, "w") as f:
        f.write("Test Case ID".ljust(15) + "Description".ljust(30) + "Started".ljust(25) +
                "End".ljust(25) + "Duration\n")

def record_test_start():
    return datetime.now()

def record_test_end(test_id, desc, start_time, end_time=None):
    if end_time is None:
        end_time = datetime.now()
    duration = round((end_time - start_time).total_seconds(), 2)
    start_str = start_time.strftime("%Y-%m-%d %H:%M:%S")
    end_str = end_time.strftime("%Y-%m-%d %H:%M:%S")

    # Avoid duplicate logs for same test_id
    if test_id not in [entry[0] for entry in execution_log]:
        execution_log.append((test_id, desc, start_str, end_str, duration))

        with open(LOG_FILE, "a") as f:
            f.write(f"{test_id:<15}{desc:<30}{start_str:<25}{end_str:<25}{duration:.2f}s\n")
