import hashlib
hashGen = hashlib.sha512()
hashGen.update("sahar skandari".encode())
hash = hashGen.hexdigest()
print ("your hash is: ", hash)
print(len(hash))