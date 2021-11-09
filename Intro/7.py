from pwn import * 
from Crypto.Util.number import * 

a = xor(b'label', 13) 

print(a)
