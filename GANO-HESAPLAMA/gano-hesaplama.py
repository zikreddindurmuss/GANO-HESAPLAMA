# GANO HESAPLAMA PROGRAMI
# Bu program öğrencilerin vize ve final notlarından yola çıkarak GANO (Genel Akademik Not Ortalaması) hesaplamaktadır.

# Üniversitedeki tüm dersler için ders bilgilerini içeren sözlük
# Her ders kodu için ders adı, kredi ve AKTS bilgileri yer almaktadır
ders_bilgileri = {
    "ATA115": {
        "ders_adi": "Atatürk İlkeleri ve İnkılap Tarihi I",
        "kredi": 2,
        "akts": 2
        },
    "FZM0105": {
        "ders_adi": "Fizik I",
        "kredi": 3,
        "akts": 4,
        },
    "FZM0151": {
        "ders_adi": "Fizik Laboratuvarı I",
        "kredi": 1,
        "akts": 2,
        },
    "MAT0143": {
        "ders_adi": "Matematik I",
        "kredi": 4,
        "akts": 5,
        },
    "SECYAB1YY": {
        "ders_adi": "Seçmeli Yabancı Dil Bahar Yarıyılı Dersi 1",
        "kredi": 4,
        "akts": 2,
        },
    "TDİ107": {
        "ders_adi": "Türk Dili I",
        "kredi": 2,
        "akts": 2,
    },
    "UYM101": {
        "ders_adi": "Üniversite Yaşamına Uyum",
        "kredi": 0,
        "akts": 0,
    },
    "YMH111": {
        "ders_adi": "Algoritma Ve Programlamaya Giriş I",
        "kredi": 4,
        "akts": 6,
    },
    "YMH113": {
        "ders_adi": "Bilgisayar Bilimlerine Giriş",
        "kredi": 3,
        "akts": 4,
    },
    "YMH115": {
        "ders_adi": "Yazılım Mühendisliğine Uyum",
        "kredi": 1,
        "akts": 3,
    },
    # "": {
    #     "ders_adi": "",
    #     "kredi": ,
    #     "akts":
    # },
    # "": {
    #     "ders_adi": "",
    #     "kredi": ,
    #     "akts":
    # },
    # "": {
    #     "ders_adi": "",
    #     "kredi": ,
    #     "akts":
    # },
    # "": {
    #     "ders_adi": "",
    #     "kredi": ,
    #     "akts":
    # },
    # "": {
    #     "ders_adi": "",
    #     "kredi": ,
    #     "akts":
    # },
    # "": {
    #     "ders_adi": "",
    #     "kredi": ,
    #     "akts":
    # },
}

# Ders kodları ve isimleri eşleştirme sözlüğü (hızlı erişim için)
ders_adlari = {
    "ATA115": "Atatürk İlkeleri ve İnkılap Tarihi I",
    "FZM0105": "Fizik I",
    "FZM0151": "Fizik Laboratuvarı I",
    "MAT0143": "Matematik I",
    "SECYAB1YY": "Seçmeli Yabancı Dil Bahar Yarıyılı Dersi 1",
    "TDİ107": "Türk Dili I",
    "UYM101": "Üniversite Yaşamına Uyum",
    "YMH111": "Algoritma Ve Programlamaya Giriş I",
    "YMH113": "Bilgisayar Bilimlerine Giriş",
    "YMH115": "Yazılım Mühendisliğine Uyum",
}

# Sistem 1: AA, BA, BB, CB, CC, DC, DD, FD, FF harf notlarına karşılık gelen 4'lük sistem değerleri
not_karsiliklari1 = {
    4.00 : "AA",
    3.50 : "BA",
    3.00 : "BB",
    2.50 : "CB",
    2.00 : "CC",
    1.50 : "DC",
    1.00 : "DD",
    0.50 : "FD",
    0.00 : "FF",
}

# Sistem 2: A, B1, B2, B3, C1, C2, C3, F1, F2, F3, F4 harf notlarına karşılık gelen 4'lük sistem değerleri
not_karsiliklari2 = {
    4.00 : "A",
    3.50 : "B1",
    3.25 : "B2",
    3.00 : "B3",
    2.75 : "C1",
    2.50 : "C2",
    2.00 : "C3",
    1.50 : "F1",
    0.50 : "F2",
    0.25 : "F3",
    0.00 : "F4",
}

# Öğrencinin girdiği notları depolamak için boş sözlük
ogrenci_notlari = {}

# Ders listesini kullanıcıya göster
print("=" * 60)
print("GANO HESAPLAMA PROGRAMINA HOŞ GELDİNİZ")
print("=" * 60)
print("\nMevcut Dersler:")
for ders in ders_adlari: # ders_adlari sözlüğündeki tüm ders kodlarını ve adlarını yazdırır
    print(f"{ders}: {ders_adlari[ders]}")

# Kullanıcıdan not sistemi ve ders sayısı bilgisini al
print("\n" + "=" * 60)
print("Not Sistemleri:")
print("1. Sistem: AA, BA, BB, CB, CC, DC, DD, FD, FF")
print("2. Sistem: A, B1, B2, B3, C1, C2, C3, F1, F2, F3, F4")
print("=" * 60)

# Kullanıcıdan hangi not sistemini kullanacağını sor
not_sistem = input("\nHangi not sistemini kullanmak istiyorsunuz? (1 veya 2): ")

# Kullanıcıdan kaç ders için GANO hesaplamak istediğini sor (hata kontrolü ile)
while True:
    try:
        ders_sayisi = int(input("Kaç ders için GANO hesaplamak istiyorsunuz?: "))
        if ders_sayisi <= 0:
            print("Lütfen 0'dan büyük bir sayı giriniz.")
            continue
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

# Seçilen not sistemine göre uygun not karşılıklarını ata
if not_sistem == "1":
    not_karsiliklari = not_karsiliklari1
elif not_sistem == "2":
    not_karsiliklari = not_karsiliklari2
else:
    print("Geçersiz not sistemi seçimi. Lütfen 1 veya 2 giriniz.")

print("\n" + "=" * 60)
print("DERS VE NOT GİRİŞİ")
print("=" * 60)

# Belirtilen sayıda ders için not giriş döngüsü
sayac = 0
while sayac < ders_sayisi:
    ders_kodu = input("GANO'sunu hesaplamak istediğiniz dersin kodunu giriniz: ")
    
    # Girilen ders kodunun geçerli olup olmadığını kontrol et
    if ders_kodu in ders_bilgileri:
        vize_notu = input("Vize notunuzu giriniz (0-100): ")
        final_notu = input("Final notunuzu giriniz (0-100): ")
        
        # Girilen notların geçerli olup olmadığını kontrol et (0-100 arasında ve sayı olup olmadığını)
        if not vize_notu.isdigit() or not final_notu.isdigit() or not (0 <= int(vize_notu) <= 100) or not (0 <= int(final_notu) <= 100):
            print("Lütfen geçerli bir not giriniz.")
        else:
            vize_notu = int(vize_notu)
            final_notu = int(final_notu)
            # Dönem sonu notunu hesapla: Vize %40 + Final %60
            toplam_not = float(vize_notu * 0.4) + float(final_notu * 0.6)
            
            # Toplam nota göre harf notu atama işlemi
            # Not aralıklarına göre 4'lük sistem değeri belirlenip karşılık gelen harf notu atanır
            if 100 >= toplam_not >= 90:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(4.00)
                else:
                    harf_notu = not_karsiliklari.get(4.00)
            elif 90 > toplam_not >= 85:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(3.50)
                else:
                    harf_notu = not_karsiliklari.get(3.50)
            elif 85 > toplam_not >= 80:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(3.00)
                else:
                    harf_notu = not_karsiliklari.get(3.25)
            elif 80 > toplam_not >= 75:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(2.50)
                else:
                    harf_notu = not_karsiliklari.get(3.00)
            elif 75 > toplam_not >= 70:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(2.00)
                else:
                    harf_notu = not_karsiliklari.get(2.75)
            elif 70 > toplam_not >= 65:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(1.50)
                else:
                    harf_notu = not_karsiliklari.get(2.50)
            elif 65 > toplam_not >= 60:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(1.00)
                else:
                    harf_notu = not_karsiliklari.get(2.00)
            elif 60 > toplam_not >= 50:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(0.50)
                else:
                    harf_notu = not_karsiliklari.get(1.50)
            else:
                if not_sistem == "1":
                    harf_notu = not_karsiliklari.get(0.00)
                else:
                    harf_notu = not_karsiliklari.get(0.00)
            
            # Öğrencinin not ve harf notlarını görüntüle
            print(f"\n{ders_kodu} kodlu ders için hesaplanan Not: {toplam_not:.2f}, Harf Notu: {harf_notu}")
            
            # Öğrencinin notlarını sözlüğe kaydet
            ogrenci_notlari[ders_kodu] = {
                "vize": vize_notu,
                "final": final_notu,
                "toplam": toplam_not,
                "harf_notu": harf_notu
            }
            print("=" * 60)
            print("Notlar başarıyla kaydedildi.")
            print("=" * 60)
            sayac += 1
    else:
        # Geçersiz ders kodu girişinde hata mesajı göster
        print(f"{ders_kodu} geçersiz bir ders kodu. Lütfen tekrar deneyin.")
        break
        
# ========================================
# GANO HESAPLAMA BÖLÜMÜ
# ========================================
# GANO = Genel Akademik Not Ortalaması
# Tüm derslerin ağırlıklı ortalaması AKTS değerlerine göre hesaplanır
toplam_kredi = 0
toplam_akts = 0
toplam_puan = 0

# Her ders için AKTS ağırlıklandırılmış not puanlarını hesapla
for ders_kodu, notlar in ogrenci_notlari.items():
    kredi = ders_bilgileri[ders_kodu]["kredi"]
    akts = ders_bilgileri[ders_kodu]["akts"]
    # 100'lük sistemdeki notu 4'lük sisteme çevir: (not / 100) * 4
    gpa_degeri = (notlar["toplam"] / 100) * 4
    toplam_kredi += kredi
    toplam_akts += akts
    # 4'lük sistem değerini AKTS ile çarpıp toplama ekle
    toplam_puan += gpa_degeri * akts

# GANO sonucunu hesapla: (derslerin toplam ağırlıklı notu) / (toplam AKTS)
if toplam_akts > 0:
    gano = toplam_puan / toplam_akts
    # GANO'ya göre harf notu belirle (GANO şimdi 4'lük sistemde)

    
    # GANO sonucunu göster
    print("\n" + "=" * 60)
    print(f"GENEL AKADEMİK NOT ORTALAMANIZ (GANO): {gano:.2f}")
    print("=" * 60)    
