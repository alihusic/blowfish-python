
# Usage of blowfish:
# plaintext = "The quick brown fox jumped over the lazy dog."
# blowfish = new Blowfish("key", plaintext)
#
# cyphertext = blowfish.encrypt(plaintext)
# print(cyphertext)
# plaintext = blowfish.decrypt(cyphertext)
# print(plaintext)
from blowfish import Blowfish, to_bits

pt = "Test encryption 12345."

blowfish = Blowfish("key", pt)
ct = blowfish.encrypt(pt)
print(ct)
pt = blowfish.decrypt(ct)
print(pt)
