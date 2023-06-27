mamalar = {
    "kedi": {
        "Felix": [
            {"paket": "80 gr", "fiyat": 5},
            {"paket": "400 gr", "fiyat": 20},
            {"paket": "2 kg", "fiyat": 80}
        ],
        "Whiskas": [
            {"paket": "100 gr", "fiyat": 7},
            {"paket": "500 gr", "fiyat": 30},
            {"paket": "3 kg", "fiyat": 90}
        ],
        "Purina": [
            {"paket": "85 gr", "fiyat": 6},
            {"paket": "450 gr", "fiyat": 25},
            {"paket": "2.5 kg", "fiyat": 100}
        ]
    },
    "köpek": {
        "Pedigree": [
            {"paket": "100 gr", "fiyat": 8},
            {"paket": "1 kg", "fiyat": 50},
            {"paket": "5 kg", "fiyat": 200}
        ],
        "Royal Canin": [
            {"paket": "150 gr", "fiyat": 10},
            {"paket": "2 kg", "fiyat": 80},
            {"paket": "10 kg", "fiyat": 300}
        ],
        "Pro Plan": [
            {"paket": "200 gr", "fiyat": 12},
            {"paket": "3 kg", "fiyat": 100},
            {"paket": "15 kg", "fiyat": 400}
        ]
    },
    "kuş": {
        "Versele-Laga": [
            {"paket": "1 kg", "fiyat": 10},
            {"paket": "2.5 kg", "fiyat": 20},
            {"paket": "5 kg", "fiyat": 35}
        ],
        "Vitakraft": [
            {"paket": "500 gr", "fiyat": 12},
            {"paket": "2.5 kg", "fiyat": 50},
            {"paket": "10 kg", "fiyat": 150}
        ],
        "Beaphar": [
            {"paket": "800 gr", "fiyat": 15},
            {"paket": "2 kg", "fiyat": 40},
            {"paket": "5 kg", "fiyat": 90}
        ]
    }
} # Bu karakteri ekledim

sepet = []
toplam_fiyat = 0

while True:
    hayvan_turu = input("Hangi hayvan türü için mama arıyorsunuz? (kedi/köpek/kuş): ")
    
    if hayvan_turu in mamalar:
        markalar = list(mamalar[hayvan_turu].keys())
        print("Aşağıdaki markalar", hayvan_turu, "maması satmaktadır:")
        for i in range(len(markalar)):
            print(f"{i+1}. {markalar[i]}")
        secilen_marka_no = input("Hangi markayı istersiniz? Lütfen yukarıdaki listeden bir numara seçin: ")
        if secilen_marka_no.isdigit() and int(secilen_marka_no) <= len(markalar):
            secilen_marka_index = int(secilen_marka_no) - 1
            secilen_marka = markalar[secilen_marka_index]
            urunler = mamalar[hayvan_turu][secilen_marka]
            print(f"\n{secilen_marka} markasının ürünleri:\n")
            for i, mama in enumerate(urunler, start=1):
                print(f"{i}. Paket: {mama['paket']} gram - Fiyat: {mama['fiyat']} TL")
            secilen_urunler = input("Hangi ürünleri sepete eklemek istersiniz? (Örneğin: 1 3): ")
            secilen_urunler = [int(urun_no) for urun_no in secilen_urunler.split() if urun_no.isdigit() and int(urun_no) <= len(urunler)]
            for urun_no in secilen_urunler:
                urun = urunler[urun_no - 1]
                sepete_ekle = input(f"{urun['paket']} gram - {urun['fiyat']} TL. Sepete eklemek istiyor musunuz? (E/H): ")
                if sepete_ekle.upper() == "E":
                    sepet.append(urun)
                    toplam_fiyat += urun["fiyat"]
                    print(f"Sepetinize {urun['paket']} gram {secilen_marka} maması eklendi.")
                else:
                    print(f"Sepetinize {urun['paket']} gram {secilen_marka} maması eklenmedi.")
        else:
            print("Lütfen geçerli bir numara girin.")
    else:
        print("Lütfen geçerli bir hayvan türü girin.")
    
    devam_et = input("Başka bir ürün aramak istiyor musunuz? (E/H): ")
    if devam_et.upper() == "H":
        break

print("\nSepetinizdeki ürünler:")
for i, urun in enumerate(sepet, start=1):
    print(f"{i}. Paket: {urun['paket']} gram - Fiyat: {urun['fiyat']} TL")

print(f"\nToplam fiyat: {toplam_fiyat} TL")