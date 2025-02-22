"""
What is Logging in Python?
Logging in Python is a way to track events that happen during a program's execution. Instead of using print() for debugging, the logging module provides a structured and configurable way to capture information about the program’s behavior.

Why Use Logging Instead of print()?
More Control: Logs can be categorized (info, warning, error, etc.).
Persistent Records: Logs can be saved to files for later debugging.
Configurable Output: Logs can be sent to console, files, or even remote servers.
Better Debugging: Helps analyze issues without modifying code.


Wheneer there is a excepton is raised thn that will be lof=gged here, steps to creaste the logs: 
1.  Create datetime objet.
2.  create the name of the file to be urrent time. 
3.  Under the curernt time and current folder, make the directory callsed the logs in it
4. inside the logs, inside the file make teh basic configuaration o format

These all things are available in the folder. 
"""
import logging
from datetime import datetime
import os

# ✅ Corrected timestamp format
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# ✅ Create only the 'logs' directory (not the file path itself)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# ✅ Correct log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# ✅ Fixed incorrect logging format (Replaced %(names)s with %(name)s)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started\n")


