import hashlib
filename=input("File name: ")
with open(filename, 'rb') as file:
	data = file.read()
	n= hashlib.md5(data).hexdigest()
print ('Hash file: ')
print(n)
