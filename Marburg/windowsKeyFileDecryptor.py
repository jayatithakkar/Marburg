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

def decryptKey():
	f = open(keys_folder + '\\private.m0ng0l14n','rb')
	pemdata = f.read()
	f.close()

	f = open(keys_folder + '\\password.m0ng0l14n','rb')
	password = f.read()
	f.close()

	privateKey = serialization.load_pem_private_key(
		data=pemdata,
		password=password,
		backend=default_backend()
	)

	f = open(keys_folder + '\\symmetricKey.m0ng0l14n','rb')
	data = f.read()
	f.close()
	plain_text = privateKey.decrypt(
		data,
		padding=padding.OAEP(mgf=padding.MGF1(
				algorithm=hashes.SHA256()
			),
			algorithm=hashes.SHA256(),
			label=None
		)
	)
	os.remove(keys_folder + '\\symmetricKey.m0ng0l14n')
	f = open(keys_folder + '\\symmetricKey.key','wb')
	f.write(plain_text)
	f.close()

	os.remove(keys_folder + '\\private.m0ng0l14n')
	os.remove(keys_folder + '\\public.m0ng0l14n')
	os.remove(keys_folder + '\\password.m0ng0l14n')