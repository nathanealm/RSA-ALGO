import math

#choosing 2 prime numbers 

p = 3 
q = 7

n = p*q
print("n=", n)

phi = (p-1)*(q-1)
e = 2

while(e<phi):
	if(math.gcd(e,phi) == 1):
		break
	else:
		e += 1

print("e =", e)
k = 2 
d = ((k*phi)+1)/e
print("d =", d)
print(f'Public Key: {e, n}')
print(f'Private key: {d, n}')

msg = 11
print(f'Orginal message:{msg}')

#encryption

C = pow(msg, e)
C = math.fmod(C,n)
print(f'Encrypted msg: {C}')

#decryption

M = pow(C,d)
M = math.fmod(M,n)

print(f'Decrypted msg: {M}')
