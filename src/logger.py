# import logging
# import os
# from datetime import datetime

# # Generate a unique log file name with a timestamp
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# # Define the logs directory relative to the script location
# logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "logs")

# # Create the logs directory if it doesn't exist
# os.makedirs(logs_dir, exist_ok=True)

# # Full path for the log file
# LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# # Configure logging
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# # Optional: Add log rotation if required
# # from logging.handlers import RotatingFileHandler
# # handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=10*1024*1024, backupCount=5)
# # logging.getLogger().addHandler(handler)

# if __name__ == "__main__":
#     logging.info(f"Log file created at: {LOG_FILE_PATH}")
#     logging.info("Logging has started")



import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)
