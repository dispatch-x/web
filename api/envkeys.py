from cryptography.fernet import Fernet
from replit import db


def generate_key():
  return Fernet.generate_key()


def key_to_string(key):
  return key.hex()


def string_to_key(key_string):
  return bytes.fromhex(key_string)


def encrypt(plaintext, key):
  cipher = Fernet(key)
  ciphertext = cipher.encrypt(plaintext.encode())
  return ciphertext.decode()


def decrypt(ciphertext, key):
  cipher = Fernet(key)
  plaintext = cipher.decrypt(ciphertext.encode())
  return plaintext.decode()


def generate(uuid):
  db[f"room_{uuid}_key"] = key_to_string(generate_key())


def retrieve(uuid):
  return db[f"room_{uuid}_key"]


# Example usage
key = generate_key()
key_string = key_to_string(key)
print("Key as string:", key_string)

message = "Hello, World!"

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

reconstructed_key = string_to_key(key_string)
print("Reconstructed key:", reconstructed_key)
