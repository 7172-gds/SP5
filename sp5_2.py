import hashlib
import string
import os
import threading

def hash_file():
	threads = []
	filename=input("File name: ")
	with open(filename, 'rb') as file:
		data = file.read()
		n= hashlib.md5(data).hexdigest()
	print ('Hash file: ')
	print(n)
	print(os.getppid())

	t=threading.Thread(target=hash_file)
	threads.append(t)
	t.start()
	print(threads)

hash_file()
