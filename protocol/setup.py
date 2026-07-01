"""
System Setup Phase

Responsible for initializing
the authentication server.
"""

from entities.server import Server


class Setup:

    def __init__(self):

        self.server = Server()

    def initialize(self):

        print("Initializing SKEBA Server...")

        return self.server