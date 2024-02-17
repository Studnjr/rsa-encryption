import random
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
       prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
   for d in range(3, phi):
      if(d * e) % phi == 1:
         return d



p,q = generate_prime(1000, 5000), generate_prime(1000, 5000)

while(p == q):
   q = generate_prime(1000, 5000)

n = p * q
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n-1)
while math.gcd(e, phi_n) != 1:
   e = random.randint(3, phi_n-1)

d = mod_inverse(e, phi_n)

print("Public Key: " , e)
print("Private Key: " , d)
print("n: " , n)
print("Phi of n: " , phi_n)
print("p: " , p)
print("q: " , q)

message = input("Enter the message to be encrypted: ")

message_encoded = [ord(ch) for ch in message]

ciphertext = [pow(ch, e, n) for ch in message_encoded]

print(ciphertext)
message_encoded = [pow(ch, d, n) for ch in ciphertext]
message_bytes = bytearray()
for ch in message_encoded:
    message_bytes += ch.to_bytes((ch.bit_length() + 7) // 8, byteorder='big')
message = message_bytes.decode()

print(message)

