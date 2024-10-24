from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

use = Fernet(key)

m = use.encrypt(b"hello hey")

print(m)

# decrypt
s_key = b'2p1TuWnonAbJJ0B6_c8i_PfBCZnBXwJSwI4pOVDyOa8='

f = Fernet(s_key)

n = f.decrypt(b'gAAAAABnGPvXtYWxcRiOuVIiypRZ8QLRbSC3mkYzo8EPAWXK346BalfALi92kuSOozb7Degf8lvwlBWbE-4hbwP-aefzqiKIyg==')

print(f"\n{n}")