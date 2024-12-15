import random
import string
# string.punctuation + string.digits + string.ascii_letters
# list(variable) ## lists all of the characters

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
#random.shuffle(key)
ters = key[::-1]
# her açtığınızda değişmesini isterseniz ters yazdığınız her yere key yazıp
# random.shuffle(key) yazıp çalıştırabilirsiniz.

print(ters)
print(chars)
#şifrelemer


cipher_text = ""
plain_text = input("Şifrelemek istediğiniz metini giriniz: ")
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += ters[index]

print(f"Mesajınız : {plain_text}")
print(f"Şifrelenmiş hali : {cipher_text}")

#çözme
plain_text = ""
cipher_text = input("Şifrelemek istediğiniz metini giriniz: ")
for letter in cipher_text:
    index = ters.index(letter)
    plain_text += chars[index]


print(f"Şifrelenmiş hali : {cipher_text}")
print(f"Mesajınız : {plain_text}")

