"""
Authentication Server
"""

from config.constants import (
    HASH_ALGORITHM,
    SECURITY_LEVEL,
    PROTOCOL_NAME,
    VERSION,
)


class Server:

    def __init__(self):

        # System Information
        self.protocol = PROTOCOL_NAME
        self.version = VERSION
        self.hash_algorithm = HASH_ALGORITHM
        self.security_level = SECURITY_LEVEL

        # Saber Keys
        self.public_key = None
        self.private_key = None

        # User Database
        self.database = {}

        # Status
        self.initialized = False

    def setup(self):
        """
        Initializes the authentication server.

        Saber Key Generation
        will be added in the next step.
        """

        print("[+] Initializing Authentication Server")

        self.initialized = True