import blowfish
from cryptography.fernet import Fernet
import os
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

user = os.getlogin()
keys_folder = 'C:\\Users\\' + user + '\\KEYS'

def get_details(file):
	file = file.split('\\')
	length = len(file)
	filename = file[length-1]
	path = ''
	for i in range(length-1):
		path += file[i] + "\\"
	return [path, filename]

def encryptKey():
	key = os.urandom(512)
	f = open(keys_folder + '\\password.m0ng0l14n','wb')
	f.write(key)
	f.close()

	privateKey = rsa.generate_private_key(
		public_exponent=65537,
		key_size=4096,
		backend = default_backend()
		)
	pem_data = privateKey.private_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PrivateFormat.PKCS8,
		encryption_algorithm=serialization.BestAvailableEncryption(key)
		)
	f = open(keys_folder + '\\private.m0ng0l14n','wb')
	f.write(pem_data)
	f.close()


	publicKey = privateKey.public_key()
	pem_data = publicKey.public_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PublicFormat.SubjectPublicKeyInfo
		)
	f = open(keys_folder + '\\public.m0ng0l14n','wb')
	f.write(pem_data)
	
	f = open(keys_folder + '\\symmetricKey.key','rb')
	plain_text = f.read()
	f.close()

	cipher_text = publicKey.encrypt(
		plain_text,
		padding=padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
			)
		)
	os.remove(keys_folder + '\\symmetricKey.key')
	f = open(keys_folder + '\\symmetricKey.m0ng0l14n','wb')
	f.write(cipher_text)
	f.close()

#Asumming that this file is present at the same destination as other file...