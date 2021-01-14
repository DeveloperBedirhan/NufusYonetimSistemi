import json

def kisiAdeti(dosyaAd):
    with open(dosyaAd) as f:
        dosya = json.load(f)

    kisiSayisi = 0
    for i in range(len(dosya)):
        kisiSayisi += 1
    print(f"Veri tabanında {kisiSayisi} kişi vardır.")

def yeniKayit(dosyaAd):
    with open(dosyaAd) as f:
        dosya = json.load(f)

    yeniKimlikNo = input("Vatandaşın kimlik numarasını yazınız: ")

    sayac = 0
    for i in range(len(dosya)):
        if yeniKimlikNo == dosya[i]["KimlikNo"]:
            print("Girmiş olduğunuz kimlik nolu 1 kişi zaten mevcuttur.")
            sayac += 1
            break

    if sayac == 0:
        yeniAd = input("Vatandaşın adını yazınız: ")
        yeniSoyad = input("Vatandaşın soyadını yazınız: ")
        yeniBabaAdi = input("Vatandaşın baba adını yazınız: ")
        yeniAnneAdi = input("Vatandaşın anne adını yazınız: ")
        yeniDogumYeri = input("Vatandaşın doğum yerini yazınız: ")
        yeniMedeniDurumu = input("Vatandaşın medeni durumunu yazınız: ")
        yeniKanGrubu = input("Vatandaşın kan grubunu yazınız: ")
        yeniKutukSehir = input("Vatandaşın kütük şehrini yazınız: ")
        yeniKutukIlce = input("Vatandaşın kütük ilçesini yazınız: ")
        yeniIkametgahSehir = input("Vatandaşın ikametgah şehrini yazınız: ")
        yeniIkametgahIlce = input("Vatandaşın ikametgah ilçesini yazınız: ")
        dosya.append({
            "KimlikNo": yeniKimlikNo,
            "Adi": yeniAd,
            "Soyadi": yeniSoyad,
            "BabaAdi": yeniBabaAdi,
            "AnneAdi": yeniAnneAdi,
            "DogumYeri": yeniDogumYeri,
            "MedeniDurumu": yeniMedeniDurumu,
            "KanGrubu": yeniKanGrubu,
            "KutukSehir": yeniKutukSehir,
            "KutukIlce": yeniKutukIlce,
            "IkametgahSehir": yeniIkametgahSehir,
            "IkametgahIlce": yeniIkametgahIlce
        })
        with open(dosyaAd, "w") as f:
            json.dump(dosya, f)
        print(f"{yeniKimlikNo} kimlik nolu vatandaş {dosyaAd} adlı dosyaya eklendi ve kaydedildi.")

def arama(dosyaAd):
    with open(dosyaAd) as f:
        dosya = json.load(f)

    kimlikNo = input("Vatandaşın kimlik numarasını yazınız: ")

    sayac = 0
    for i in range(len(dosya)):
        if kimlikNo == dosya[i]["KimlikNo"]:
            sayac += 1
            print(f"{kimlikNo} kimlik nolu vatandaşın bilgileri:\t{dosya[i]}")

    if sayac == 0:
        print(f"{kimlikNo} kimlik nolu bir vatandaş bulunmamaktadır.")

def kisiGuncelleme(dosyaAd):
    with open(dosyaAd) as f:
        dosya = json.load(f)

    ID = input("Güncellemek istediğiniz kişinin kimlik numarasını giriniz: ")
    key = input(f"{ID} kimlik nolu kişinin güncellemek istediğiniz (Adi/Soyadi/"
                f"BabaAdi/AnneAdi/DogumYeri/MedeniDurumu/KanGrubu/KutukSehir/KutukIlce/"
                f"IkametgahSehir/IkametgahIlce) bilgilerinden birini yazınız : ")
    word = input(f"Güncellemek istediğiniz {key} değerini giriniz: ")

    if key not in ["Adi","Soyadi","BabaAdi","AnneAdi","DogumYeri","MedeniDurumu",
                   "KanGrubu","KutukSehir","KutukIlce","IkametgahSehir","IkametgahIlce"]:
        print("Hatalı giriş !!!")

    else:
        sayac = 0
        for i in range(len(dosya)):
            if ID == dosya[i]["KimlikNo"]:
                dosya[i][key] = word
                print(f"{ID} kimlik nolu vatandaşın {key} bilgisi güncellendi.")
                sayac += 1
                break

        if sayac == 0:
            print(f"{ID} kimlik nolu bir vatandaş bulunmamaktadır.")

        with open(dosyaAd, "w") as f:
            json.dump(dosya, f)

def kisiSilme(dosyaAd):
    with open(dosyaAd) as f:
        dosya = json.load(f)

    silinecekID = input("Silmek istediğiniz kişinin kimlik numarasını giriniz: ")

    sayac = 0
    for i in range(len(dosya)):
        if silinecekID == dosya[i]["KimlikNo"]:
            dosya.remove(dosya[i])
            print(f"{silinecekID} kimlik nolu vatandaş {dosyaAd} dosyasından silindi.")
            sayac += 1
            break

    if sayac == 0:
        print(f"{silinecekID} kimlik nolu bir vatandaş bulunmamaktadır.")

    with open(dosyaAd, "w") as f:
        json.dump(dosya, f)

def listeleme(dosyaAd):
    with open(dosyaAd) as f:
        dosya = json.load(f)
    print(dosya)
