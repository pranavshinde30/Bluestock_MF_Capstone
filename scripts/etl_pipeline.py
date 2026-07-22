import subprocess
import sys
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent

# ETL scripts in execution order
scripts = [
    "data_ingestion.py",
    "clean_nav_history.py",
    "clean_scheme_performance.py",
    "clean_investor_transactions.py",
    "load_to_sqlite.py",
    "verify_sqlite_data.py"
]

print("=" * 60)
print("Starting Mutual Fund ETL Pipeline")
print("=" * 60)

for script in scripts:
    print(f"\nRunning: {script}")

    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / script)]
    )

    if result.returncode != 0:
        print(f"\nERROR: {script} failed.")
        sys.exit(1)

    print(f"{script} completed successfully.")

print("\n" + "=" * 60)
print("ETL Pipeline Completed Successfully!")
print("=" * 60)