from abc import ABC, abstractmethod

class Kaynak(ABC):
    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, value):
        self._kayitNo = value


class Kitap(Kaynak):
    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = value

    def __str__(self):
        return f"[Kitap] Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Yazar: {self.yazar} | Sayfa Sayısı: {self.sayfa_sayisi}"


class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    def __str__(self):
        return f"[Dergi] Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Yayın Dönemi: {self.yayin_donemi} | Sayı No: {self.sayi_no}"


class Islem(ABC):
    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass


class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def kitap_sayisi(self):
        return len(self.kitaplar)

    def ekle(self):
        print("\n--- Kitap Ekle ---")
        kayitNo = input("Kitabın kayıt numarasını girin: ").strip()
        
        for k in self.kitaplar:
            if k.kayitNo == kayitNo:
                print("Hata: Bu kayıt numarası zaten mevcut! Aynı kitap tekrar eklenemez.")
                return

        baslik = input("Kitabın başlığını girin: ").strip()
        yazar = input("Kitabın yazarını girin: ").strip()
        sayfa_sayisi = input("Kitabın sayfa sayısını girin: ").strip()

        yeni_kitap = Kitap(baslik, kayitNo, yazar, sayfa_sayisi)
        self.kitaplar.append(yeni_kitap)
        print("Kitap başarıyla eklendi.")
        print(f"Toplam Kitap Sayısı: {self.kitap_sayisi()}")

    def sil(self):
        print("\n--- Kitap Sil ---")
        if self.kitap_sayisi() == 0:
            print("Sistemde silinecek kitap bulunmamaktadır.")
            return
            
        kayitNo = input("Silmek istediğiniz kitabın Kayıt No'sunu girin: ").strip()
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                self.kitaplar.remove(kitap)
                print(f"{kayitNo} numaralı kitap başarıyla silindi.")
                return
        print("Belirtilen kayıt numarasına sahip kitap bulunamadı.")

    def guncelle(self):
        print("\n--- Kitap Güncelle ---")
        kayitNo = input("Güncellemek istediğiniz kitabın Kayıt No'sunu girin: ").strip()
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                print(f"Mevcut Bilgiler -> Başlık: {kitap.baslik}, Yazar: {kitap.yazar}")
                kitap.baslik = input("Yeni Başlık girin: ").strip()
                kitap.yazar = input("Yeni Yazar girin: ").strip()
                kitap.sayfa_sayisi = input("Yeni Sayfa Sayısı girin: ").strip()
                print("Kitap bilgileri başarıyla güncellendi.")
                return
        print("Belirtilen kayıt numarasına sahip kitap bulunamadı.")

    def listele(self):
        print("\n--- Kitap Listesi ---")
        if self.kitap_sayisi() == 0:
            print("Kayıt bulunamadı.")
        else:
            for kitap in self.kitaplar:
                print(kitap)


class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def dergi_sayisi(self):
        return len(self.dergiler)

    def ekle(self):
        print("\n--- Dergi Ekle ---")
        kayitNo = input("Derginin kayıt numarasını girin: ").strip()
        
        for d in self.dergiler:
            if d.kayitNo == kayitNo:
                print("Hata: Bu kayıt numarası zaten mevcut! Aynı dergi tekrar eklenemez.")
                return

        baslik = input("Derginin başlığını girin: ").strip()
        yayin_donemi = input("Yayın dönemini girin (Aylık/Haftalık vb.): ").strip()
        sayi_no = input("Dergi sayı numarasını girin: ").strip()

        yeni_dergi = Dergi(baslik, kayitNo, yayin_donemi, sayi_no)
        self.dergiler.append(yeni_dergi)
        print("Dergi başarıyla eklendi.")
        print(f"Toplam Dergi Sayısı: {self.dergi_sayisi()}")

    def sil(self):
        print("\n--- Dergi Sil ---")
        if self.dergi_sayisi() == 0:
            print("Sistemde silinecek dergi bulunmamaktadır.")
            return

        kayitNo = input("Silmek istediğiniz derginin Kayıt No'sunu girin: ").strip()
        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                self.dergiler.remove(dergi)
                print(f"{kayitNo} numaralı dergi başarıyla silindi.")
                return
        print("Belirtilen kayıt numarasına sahip dergi bulunamadı.")

    def guncelle(self):
        print("\n--- Dergi Güncelle ---")
        kayitNo = input("Güncellemek istediğiniz derginin Kayıt No'sunu girin: ").strip()
        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                print(f"Mevcut Bilgiler -> Başlık: {dergi.baslik}, Sayı No: {dergi.sayi_no}")
                dergi.baslik = input("Yeni Başlık girin: ").strip()
                dergi.yayin_donemi = input("Yeni Yayın Dönemi girin: ").strip()
                dergi.sayi_no = input("Yeni Sayı No girin: ").strip()
                print("Dergi bilgileri başarıyla güncellendi.")
                return
        print("Belirtilen kayıt numarasına sahip dergi bulunamadı.")

    def listele(self):
        print("\n--- Dergi Listesi ---")
        if self.dergi_sayisi() == 0:
            print("Kayıt bulunamadı.")
        else:
            for dergi in self.dergiler:
                print(dergi)


class Menü:
    def __init__(self):
        self.kitap_sistemi = KitapIslem()
        self.dergi_sistemi = DergiIslem()

    def menuyu_goster(self):
        while True:
            print("\n" + "="*30)
            print("KÜTÜPHANE YÖNETİM SİSTEMİ")
            print("="*30)
            print("1. Kitap Ekle")
            print("2. Kitap Sil")
            print("3. Kitap Güncelle")
            print("4. Kitapları Listele")
            print("5. Dergi Ekle")
            print("6. Dergi Sil")
            print("7. Dergi Güncelle")
            print("8. Dergileri Listele")
            print("9. Çıkış")
            print("="*30)
            
            secim = input("Yapmak istediğiniz işlemi seçin (1-9): ").strip()

            if secim == "1":
                self.kitap_sistemi.ekle()
            elif secim == "2":
                self.kitap_sistemi.sil()
            elif secim == "3":
                self.kitap_sistemi.guncelle()
            elif secim == "4":
                self.kitap_sistemi.listele()
            elif secim == "5":
                self.dergi_sistemi.ekle()
            elif secim == "6":
                self.dergi_sistemi.sil()
            elif secim == "7":
                self.dergi_sistemi.guncelle()
            elif secim == "8":
                self.dergi_sistemi.listele()
            elif secim == "9":
                print("\nSistemden çıkılıyor... İyi günler!")
                break
            else:
                print("\nGeçersiz seçim! Lütfen 1-9 arasında bir değer girin.")

if __name__ == "__main__":
    sistem = Menü()
    sistem.menuyu_goster()