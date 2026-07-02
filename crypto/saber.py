"""
Official Saber Python Wrapper
"""

import ctypes
from pathlib import Path

# ============================================================================
# Official Saber Parameters
# ============================================================================

PUBLIC_KEY_BYTES = 992
SECRET_KEY_BYTES = 3360
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

lib.crypto_kem_keypair.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]

lib.crypto_kem_keypair.restype = ctypes.c_int


class Saber:

    def keypair(self):
        """
        Generate a Saber public/private key pair.
        """

        public_key = ctypes.create_string_buffer(PUBLIC_KEY_BYTES)

        secret_key = ctypes.create_string_buffer(SECRET_KEY_BYTES)

        result = lib.crypto_kem_keypair(
            public_key,
            secret_key
        )

        if result != 0:
            raise RuntimeError("Saber Key Generation Failed")

        return (
            bytes(public_key.raw),
            bytes(secret_key.raw),
        )