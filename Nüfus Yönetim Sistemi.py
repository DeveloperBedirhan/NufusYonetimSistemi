import Proje

dosyaAd = 'kisiler.json'
Proje.kisiAdeti(dosyaAd)

while True:
    print("\nLütfen yapmak istediğiniz işlemi seçiniz \n"
          "0. Çıkış \n"
          "1. Yeni Kayıt\n"
          "2. Arama ve Listeleme\n"
          "3. Kişi Güncelleme\n"
          "4. Kişi Silme\n"
          "5. Tüm Veritabanını Listeleme\n")

    islev = input("Seçiminiz: ")

    if islev not in ["0","1","2","3","4","5"]:
        print("Hatalı giriş !!!")
    elif islev=="0":
        print("Çıkış seçildi")
        exit(0)
    elif islev =="1":
        Proje.yeniKayit(dosyaAd)
    elif islev =="2":
        Proje.arama(dosyaAd)
    elif islev =="3":
        Proje.kisiGuncelleme(dosyaAd)
    elif islev =="4":
        Proje.kisiSilme(dosyaAd)
    elif islev =="5":
        Proje.listeleme(dosyaAd)
