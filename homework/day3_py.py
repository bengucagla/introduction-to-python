# -*- coding: utf-8 -*-
"""day3.py


complete = False
user = {"python" : "12345","java":"78945" }
print ("Python şifre ve kullanıcı adı girme programına hoşgeldiniz.")
 
while not complete:
    username = input("Username: ")
    password = input("Password: ")
    if username == user and password == password:
        continue
    elif username not in user:
        print("Kullanıcı adınızı yanlış girdiniz.")
        continue
    elif password != user[username]:
        print(f"Şifrenizi yanlış girdiniz {username}. ")
        continue
    elif password == user[username]:
        print(f"Hoşgeldiniz {username} ")
        print(f"Giriş yaptığınız için teşekkürler. ")
        complete = True