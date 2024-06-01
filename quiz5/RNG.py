import secrets

def generate_secure_random_bytes(num_bytes: int = 10050000) -> bytes:
    """Generate num_bytes of cryptographically secure random bytes."""
    return secrets.token_bytes(num_bytes)

# Generate 1M bytes of secure random data
secure_random_bytes = generate_secure_random_bytes(10050000)

# If you need to save this data to a file, you can do so like this:
with open("random.bin", "wb") as f:
    f.write(secure_random_bytes)
