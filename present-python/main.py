from present import Present

# Encrypting with a 80-bit key:
# ------------------------------
key   = "00000000000000000000"
plain = "0000000000000000"

cipher = Present(key)

encrypted = cipher.encrypt(plain)
print("Encrypted", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Decrypted", decrypted)

# Encrypting with a 128-bit key:
# -------------------------------
key = "0123456789abcdef0123456789abcdef"
plain = "0123456789abcdef"

cipher = Present(key)

encrypted = cipher.encrypt(plain)
print("Encrypted", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Decrypted", decrypted)
