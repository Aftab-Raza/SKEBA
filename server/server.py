from crypto.hash_utils import sha3_256
from crypto.random_utils import random_hex

class Server:

    def __init__(self):

        self.server_secret = random_hex()

        self.public_key = "PUBLIC_KEY_PLACEHOLDER"

    def register_user(self, user_id, beta):

        gamma = sha3_256(self.server_secret + user_id)

        lambda_value = sha3_256(beta + gamma)

        return lambda_value, gamma, self.public_key