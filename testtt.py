from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()
if os.getenv('SQLITE'):
    print(1)
else:
    print(2)