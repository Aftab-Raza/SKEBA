"""
Official Saber Wrapper
"""

import ctypes
from pathlib import Path

# ============================================================================
# Official Saber Sizes
# ============================================================================

PUBLIC_KEY_BYTES = 992
SECRET_KEY_BYTES = 2304 + 992 + 32 + 32
CIPHERTEXT_BYTES = 1088
SHARED_SECRET_BYTES = 32

# ============================================================================
# Load Shared Library
# ============================================================================

LIB_PATH = (
    Path(__file__).resolve().parent.parent
    / "native"
    / "libsaber.so"
)

lib = ctypes.CDLL(str(LIB_PATH))

# ============================================================================
# Function Signatures
# ============================================================================

lib.crypto_kem_keypair.restype = ctypes.c_int

lib.crypto_kem_enc.restype = ctypes.c_int

lib.crypto_kem_dec.restype = ctypes.c_int