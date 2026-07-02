"""
Official Saber Python Interface
"""

import ctypes
from pathlib import Path

# Native library path
LIB_PATH = (
    Path(__file__).resolve().parent.parent
    / "native"
    / "libsaber.so"
)

# Load the shared library
lib = ctypes.CDLL(str(LIB_PATH))

print("[+] Official Saber library loaded successfully.")