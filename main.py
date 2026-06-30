from user.registration import User
from server.server import Server
from smartcard.smartcard import SmartCard

from crypto.hash_utils import sha3_256

print("="*60)
print("SKEBA Registration Phase")
print("="*60)

user = User(
    "vickey123",
    "MyPassword@123"
)

server = Server()

card = SmartCard()

beta = user.generate_beta()

print("\nBeta Generated")

lambda_value, gamma, pk = server.register_user(
    user.user_id,
    beta
)

card.lambda_value = lambda_value

card.public_key = pk

card.eta = sha3_256(user.user_id + user.password)

card.zeta = sha3_256(card.eta + gamma)

card.display()

print("\nRegistration Successful")