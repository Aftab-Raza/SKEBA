"""
Authentication Server Entity
"""

class Server:

    def __init__(self):

        self.public_key = None

        self.private_key = None

        self.database = {}

        self.initialized = False