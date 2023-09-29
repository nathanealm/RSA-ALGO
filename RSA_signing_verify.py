import rsa

with open("public.pem", "rb") as f:
	public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
	private_key = rsa.PrivateKey.load_pkcs1(f.read())

msg = "I have a nutshell @game"
#signature = rsa.sign(msg.encode(), private_key, "SHA-256")

with open("signature", "rb") as f:
	signature = f.read()

print(rsa.verify(msg.encode(), signature, public_key))
