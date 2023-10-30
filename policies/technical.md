## Dispatch Technical Policy
This document details how Dispatchx works under the hood, and how user data is protected.
### What is encrypted/hashed
Things that are encrypted or hashed are listed in the privacy policy.
### How encryption works
We use the Python `cryptography.fernet` module for encryption of user data. It is common for storing small amounts of data. The keys are securely stored in an encrypted DB. It leverages several common cryptographic primitives, specifically `AES-128` in `CBC` mode using `PKCS7` padding, and `HMAC` and `SHA256` for authentication. It relies on `os.urandom`, and our server runs on `Ubuntu 22.04`, at last check using kernel version `6.2.0`.
### How hashing works
We use the Python module `bcrypt` to hash passwords. `bcrypt` is among the most secure password hashing solutions, as it uses salts, is intentionally slow (making attacks computationally expensive). Behind the scenes, it uses `Blowfish` for the hashing and `KDF` functions. For the work factor, we use 12, a balance between security and performance (and the industry standard).