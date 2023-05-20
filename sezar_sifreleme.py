import os
def caesar_sifreleme(metin, kaydirma_miktari):
    sifreli_metin = ""
    for harf in metin:
        if harf.isalpha():
            ascii_kod = ord(harf)
            ascii_kod += kaydirma_miktari

            if harf.isupper():
                if ascii_kod > ord("Z"):
                    ascii_kod -= 26
                elif ascii_kod < ord("A"):
                    ascii_kod += 26
            else:
                if ascii_kod > ord("z"):
                    ascii_kod -= 26
                elif ascii_kod < ord("a"):
                    ascii_kod += 26

            sifreli_metin += chr(ascii_kod)
        else:
            sifreli_metin += harf

    return sifreli_metin

def caesar_sifre_coz(metin, kaydirma_miktari):
    return caesar_sifreleme(metin, -kaydirma_miktari)

while True:
    os.system("figlet Sezar sifrelemesi ")
    print("\nLütfen aşağıdaki seçeneklerden birini seçin:")
    print("1-) şifreleme yap")
    print("2-) şifre çözme")
    print("3-) Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        metin = input("Lütfen şifrelemek istediğiniz metni girin: ")
        kaydirma_miktari = int(input("Lütfen kaydırma miktarını girin: "))
        sifreli_metin = caesar_sifreleme(metin, kaydirma_miktari)
        print("Şifreli metin:", sifreli_metin)
    elif secim == "2":
        metin = input("Lütfen çözmek istediğiniz şifreli metni girin: ")
        kaydirma_miktari = int(input("Lütfen kaydırma miktarını girin: "))
        cozulmus_metin = caesar_sifre_coz(metin, kaydirma_miktari)
        print("Orijinal metin:", cozulmus_metin)
    elif secim == "3":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
