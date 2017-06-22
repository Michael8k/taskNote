from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


# key generation Alisa
privatekey = RSA.generate(2048)
f = open('c:\cipher\\alisaprivatekey.txt','wb')
f.write(bytes(privatekey.exportKey('PEM'))); f.close()
publickey = privatekey.publickey()
f = open('c:\cipher\\alisapublickey.txt','wb')
f.write(bytes(publickey.exportKey('PEM'))); f.close()
# key generation Bob
privatekey = RSA.generate(2048)
f = open('c:\cipher\\bobprivatekey.txt','wb')
f.write(bytes(privatekey.exportKey('PEM'))); f.close()
publickey = privatekey.publickey()
f = open('c:\cipher\\bobpublickey.txt','wb')
f.write(bytes(publickey.exportKey('PEM'))); f.close()
