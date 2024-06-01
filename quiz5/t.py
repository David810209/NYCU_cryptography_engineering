import secrets

# Generate a cryptographically secure random number
secure_num = secrets.randbelow(100)
print(secure_num)

# Generate a secure random hexadecimal token
token = secrets.token_hex(16)
print(token)