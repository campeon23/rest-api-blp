import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://red-cf4bm31gp3js6fj3uid0:6379")
QUEUES = ["emails", "default"]
