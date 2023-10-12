def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def rsa_key_generation(p, q, e):
    N = p * q
    phi_N = (p - 1) * (q - 1)
    
    while True:
        if 1 < e < phi_N and gcd(e, phi_N) == 1:
            break
        e = int(input("Enter a valid encryption key (1 < e < phi(N) and gcd(e, phi(N)) = 1): "))
    
    d = mod_inverse(e, phi_N)
    
    return ((e, N), (d, N))

def encrypt(plain_text, public_key):
    e, N = public_key
    cipher_text = pow(plain_text, e, N)
    return cipher_text

def decrypt(cipher_text, private_key):
    d, N = private_key
    plain_text = pow(cipher_text, d, N)
    return plain_text

p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
e = int(input("Enter an encryption key (1 < e < phi(N) and gcd(e, phi(N)) = 1): "))

public_key, private_key = rsa_key_generation(p, q, e)

message = int(input("Enter a number to encrypt: "))
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decryption key:", private_key[0])
print("Decrypted message:", decrypted_message)
