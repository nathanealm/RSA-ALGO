import random
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def generate_keypair(bits=1024):
    p = q = 1
    while not is_prime(p):
        p = random.getrandbits(bits)
    while not is_prime(q) or p == q:
        q = random.getrandbits(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def encrypt(message, public_key):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

def decrypt(encrypted_msg, private_key):
    d, n = private_key
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in encrypted_msg])
    return decrypted_msg

# Example usage
public_key, private_key = generate_keypair()
message = "Hello, RSA encryption and decryption!"
print("Original Message:", message)

encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
