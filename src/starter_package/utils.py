import os
import time
from datetime import datetime as dt
from pathlib import Path

USER = "hallamlab" # github id
MODULE_ROOT = Path("/".join(os.path.realpath(__file__).split('/')[:-1]))
NAME = MODULE_ROOT.name.lower()
# can add additional entry points here, like abbreviations
# ex. ENTRY_POINTS = [NAME, "spk"]
ENTRY_POINTS = [NAME]

def _get_version() -> str:
    with open(MODULE_ROOT.joinpath("version.txt")) as v:
        return v.readline()
VERSION = _get_version()

class StdTime:
    FORMAT = '%Y-%m-%d_%H-%M-%S'

    @classmethod
    def Timestamp(cls, timestamp: dt|None = None):
        ts = dt.now() if timestamp is None else timestamp
        return f"{ts.strftime(StdTime.FORMAT)}"
    
    @classmethod
    def Parse(cls, timestamp: str|int):
        if isinstance(timestamp, str):
            return dt.strptime(timestamp, StdTime.FORMAT)
        else:
            return dt.fromtimestamp(timestamp/1000)
    
    @classmethod
    def CurrentTimeMillis(cls):
        return round(time.time() * 1000)