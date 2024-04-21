import os

MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DB = os.environ.get("MONGO_DB")

if MONGO_URI is None or MONGO_DB is None:
    raise ValueError("MONGO_URI or MONGO_DB is not set")
