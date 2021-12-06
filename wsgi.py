import sys

home = "A:\webapp"
if home not in sys.path:
    sys.path.append(home)

from app import app as application
