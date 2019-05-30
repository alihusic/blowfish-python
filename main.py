
# Usage of blowfish:
# plaintext = "The quick brown fox jumped over the lazy dog."
# blowfish = new Blowfish("key", plaintext)
#
# cyphertext = blowfish.encrypt(plaintext)
# print(cyphertext)
# plaintext = blowfish.decrypt(cyphertext)
# print(plaintext)
from blowfish import Blowfish

pt = "Nedim"

print('The plaintext is: {}'.format(pt))

blowfish = Blowfish("dsadasdasda", pt)
ct = blowfish.encrypt(pt)
print('The ciphertext is: {}'.format(ct))
pt = blowfish.decrypt(ct)
print('The decrypted ciphertext is: {}'.format(pt))
