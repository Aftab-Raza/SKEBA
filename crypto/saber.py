"""
Official Saber Implementation
"""

from crypto.kem import KEM


class Saber(KEM):

    def keypair(self):
        raise NotImplementedError

    def encaps(self, public_key):
        raise NotImplementedError

    def decaps(self, ciphertext, private_key):
        raise NotImplementedError