import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from sympy import isprime, primerange

# 選擇一個大質數p和基數g
def choose_large_prime_and_base():
    primes = list(primerange(1000, 5000))
    p = random.choice(primes)
    g = random.randint(2, p-1)
    return p, g

# Diffie-Hellman Key Exchange Function
def diffie_hellman_key_exchange():
    p, g = choose_large_prime_and_base()
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)
    alice_public_key = pow(g, a, p)
    bob_public_key = pow(g, b, p)
    # 交換並計算共享秘密
    alice_secret = pow(bob_public_key, a, p)
    bob_secret = pow(alice_public_key, b, p)
    
    print(f"Alice 的公鑰: {alice_public_key}")
    print(f"Bob 的公鑰: {bob_public_key}")
    print(f"Alice 的秘密: {alice_secret}")
    print(f"Bob 的秘密: {bob_secret}")
    
    assert alice_secret == bob_secret, "秘密不匹配，有錯誤發生！"
    dh_secret = alice_secret
    return dh_secret, alice_public_key, bob_public_key, p, g, a, b

# Compute shared secret using another party's public key
def compute_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)

# RSA Key Generation
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# RSA Encryption
def rsa_encrypt(message, public_key):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# RSA Decryption
def rsa_decrypt(encrypted, private_key):
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message.decode()

# RSA Sign Message
def sign_message(message, private_key):
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Verify Signature
def verify_signature(message, signature, public_key):
    public_key.verify(
        signature,
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return True

# Main Interactive Session
def main():
    print("Starting secure communication simulation...")

    # Diffie-Hellman Key Exchange
    dh_secret, alice_public_key, bob_public_key, p, g, a, b = diffie_hellman_key_exchange()
    print(f"Diffie-Hellman Shared Secret: {dh_secret}")

    # Compute shared secret using Bob's public key and Alice's private key
    alice_computed_secret = compute_shared_secret(bob_public_key, a, p)
    print(f"Recomputed Shared Secret using Bob's public key: {alice_computed_secret}")

    # Compute shared secret using Alice's public key and Bob's private key
    bob_computed_secret = compute_shared_secret(alice_public_key, b, p)
    print(f"Recomputed Shared Secret using Alice's public key: {bob_computed_secret}")

    # RSA Encryption/Decryption
    private_key, public_key = generate_rsa_keys()
    message = input("Enter a message to encrypt: ")
    encrypted_message = rsa_encrypt(message, public_key)
    decrypted_message = rsa_decrypt(encrypted_message, private_key)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

    # Digital Signature
    signature = sign_message(message, private_key)
    verification = verify_signature(message, signature, public_key)
    print("Signature Verified:", verification)

if __name__ == "__main__":
    main()
