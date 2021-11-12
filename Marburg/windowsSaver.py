import windowsKeyFileDecryptor
import windowsFileDecryptor

def main():
	try:
		windowsKeyFileDecryptor.decryptKey()
		windowsFileDecryptor.doit()
	except:
		print("S0M3TH1NG W3NT WR0NG")

if __name__ == '__main__':
	main()