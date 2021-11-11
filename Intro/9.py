from pwn import * 
from Crypto.Util.number import * 

datakey = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")


output = b'crypto{'
print(datakey)

sdk = datakey[0:7]

#print(sdk)

key=(xor(sdk,output))
#print(key)

print(xor(datakey, b'myXORkey'))
