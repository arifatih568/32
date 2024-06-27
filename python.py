from builtins import input

import time

print("... Basit Hesap Makinesine Hoşgeldiniz ...")
print(" ")
while(True):
        sec1 = int(input("Hesaplanacak 1. Sayiyi Giriniz: ")) 
        sec2 = int(input("Hesaplanacak 2. Sayiyi Giriniz: "))
        print(" ")
        op = input("Lütfen Bir İşlem Seç ( +,-,*,/ ): ")
        print(" ")
        print("İşlem Hesaplaniyor")
        time.sleep(2)
        if op == "+":
            print(sec1, "+", sec2, "=", sec1 + sec2)

        if op == "-":
            print(sec1, "-", sec2, "=", sec1 - sec2)

        if op == "*":
            print(sec1, "*", sec2, "=", sec1 * sec2)

        if op == "/":
            print(sec1, "/", sec2, "=", sec1 / sec2)
        
        time.sleep(2)
        print(" ")
        
        print("Çikiş yapmak İçin herhan gibi Bir Harfre Tikla")