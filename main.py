from crypto.hash_utils import sha3_256, sha3_512
from crypto.random_utils import random_hex, random_int

print("=" * 50)
print("SKEBA Project")
print("=" * 50)

message = "Hello Vickey"

print("\nSHA3-256")
print(sha3_256(message))

print("\nSHA3-512")
print(sha3_512(message))

print("\nRandom Hex")
print(random_hex())

print("\nRandom Integer")
print(random_int())