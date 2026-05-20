from abc import ABC, abstractmethod


class Kaynak(ABC):
    def __init__(self, baslik, kayit_no):
        self._baslik = baslik
        self._kayit_no = kayit_no

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayit_no(self):
        return self._kayit_no

    @kayit_no.setter
    def kayit_no(self, value):
        self._kayit_no = value


class Kitap(Kaynak):
    def __init__(self, baslik, kayit_no, yazar, sayfa_sayisi):
        super().__init__(baslik, kayit_no)
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
        return (
            f"[Kitap] Kayit No: {self.kayit_no} | "
            f"Baslik: {self.baslik} | "
            f"Yazar: {self.yazar} | "
            f"Sayfa Sayisi: {self.sayfa_sayisi}"
        )


class Dergi(Kaynak):
    def __init__(self, baslik, kayit_no, yayin_donemi, sayi_no):
        super().__init__(baslik, kayit_no)
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
        return (
            f"[Dergi] Kayit No: {self.kayit_no} | "
            f"Baslik: {self.baslik} | "
            f"Yayin Donemi: {self.yayin_donemi} | "
            f"Sayi No: {self.sayi_no}"
        )


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


def int_giris(mesaj):
    """Kullanicidan gecerli bir tam sayi alana kadar tekrar sorar."""
    while True:
        deger = input(mesaj).strip()
        if deger.isdigit():
            return int(deger)
        print("Hata: Lutfen gecerli bir sayi girin.")


class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def kitap_sayisi(self):
        return len(self.kitaplar)

    def _kayit_no_var_mi(self, kayit_no):
        return any(k.kayit_no == kayit_no for k in self.kitaplar)

    def ekle(self):
        print("\n--- Kitap Ekle ---")
        kayit_no = input("Kitabin kayit numarasini girin: ").strip()

        if self._kayit_no_var_mi(kayit_no):
            print("Hata: Bu kayit numarasi zaten mevcut! Ayni kitap tekrar eklenemez.")
            return

        baslik = input("Kitabin basligini girin: ").strip()
        yazar = input("Kitabin yazarini girin: ").strip()
        sayfa_sayisi = int_giris("Kitabin sayfa sayisini girin: ")

        yeni_kitap = Kitap(baslik, kayit_no, yazar, sayfa_sayisi)
        self.kitaplar.append(yeni_kitap)
        print("Kitap basariyla eklendi.")
        print(f"Toplam Kitap Sayisi: {self.kitap_sayisi()}")

    def sil(self):
        print("\n--- Kitap Sil ---")
        if self.kitap_sayisi() == 0:
            print("Sistemde silinecek kitap bulunmamaktadir.")
            return

        kayit_no = input("Silmek istediginiz kitabin Kayit No'sunu girin: ").strip()
        for kitap in self.kitaplar:
            if kitap.kayit_no == kayit_no:
                self.kitaplar.remove(kitap)
                print(f"{kayit_no} numarali kitap basariyla silindi.")
                return
        print("Belirtilen kayit numarasina sahip kitap bulunamadi.")

    def guncelle(self):
        print("\n--- Kitap Guncelle ---")
        kayit_no = input("Guncellemek istediginiz kitabin Kayit No'sunu girin: ").strip()
        for kitap in self.kitaplar:
            if kitap.kayit_no == kayit_no:
                print(f"Mevcut Bilgiler -> Baslik: {kitap.baslik} | Yazar: {kitap.yazar} | Sayfa Sayisi: {kitap.sayfa_sayisi}")
                kitap.baslik = input("Yeni Baslik girin: ").strip()
                kitap.yazar = input("Yeni Yazar girin: ").strip()
                kitap.sayfa_sayisi = int_giris("Yeni Sayfa Sayisi girin: ")
                print("Kitap bilgileri basariyla guncellendi.")
                return
        print("Belirtilen kayit numarasina sahip kitap bulunamadi.")

    def listele(self):
        print("\n--- Kitap Listesi ---")
        if self.kitap_sayisi() == 0:
            print("Kayit bulunamadi.")
        else:
            for kitap in self.kitaplar:
                print(kitap)


class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def dergi_sayisi(self):
        return len(self.dergiler)

    def _kayit_no_var_mi(self, kayit_no):
        return any(d.kayit_no == kayit_no for d in self.dergiler)

    def ekle(self):
        print("\n--- Dergi Ekle ---")
        kayit_no = input("Derginin kayit numarasini girin: ").strip()

        if self._kayit_no_var_mi(kayit_no):
            print("Hata: Bu kayit numarasi zaten mevcut! Ayni dergi tekrar eklenemez.")
            return

        baslik = input("Derginin basligini girin: ").strip()
        yayin_donemi = input("Yayin donemini girin (Aylik/Haftalik vb.): ").strip()
        sayi_no = int_giris("Dergi sayi numarasini girin: ")

        yeni_dergi = Dergi(baslik, kayit_no, yayin_donemi, sayi_no)
        self.dergiler.append(yeni_dergi)
        print("Dergi basariyla eklendi.")
        print(f"Toplam Dergi Sayisi: {self.dergi_sayisi()}")

    def sil(self):
        print("\n--- Dergi Sil ---")
        if self.dergi_sayisi() == 0:
            print("Sistemde silinecek dergi bulunmamaktadir.")
            return

        kayit_no = input("Silmek istediginiz derginin Kayit No'sunu girin: ").strip()
        for dergi in self.dergiler:
            if dergi.kayit_no == kayit_no:
                self.dergiler.remove(dergi)
                print(f"{kayit_no} numarali dergi basariyla silindi.")
                return
        print("Belirtilen kayit numarasina sahip dergi bulunamadi.")

    def guncelle(self):
        print("\n--- Dergi Guncelle ---")
        kayit_no = input("Guncellemek istediginiz derginin Kayit No'sunu girin: ").strip()
        for dergi in self.dergiler:
            if dergi.kayit_no == kayit_no:
                print(f"Mevcut Bilgiler -> Baslik: {dergi.baslik} | Sayi No: {dergi.sayi_no}")
                dergi.baslik = input("Yeni Baslik girin: ").strip()
                dergi.yayin_donemi = input("Yeni Yayin Donemi girin: ").strip()
                dergi.sayi_no = int_giris("Yeni Sayi No girin: ")
                print("Dergi bilgileri basariyla guncellendi.")
                return
        print("Belirtilen kayit numarasina sahip dergi bulunamadi.")

    def listele(self):
        print("\n--- Dergi Listesi ---")
        if self.dergi_sayisi() == 0:
            print("Kayit bulunamadi.")
        else:
            for dergi in self.dergiler:
                print(dergi)


class Menu:
    def __init__(self):
        self.kitap_sistemi = KitapIslem()
        self.dergi_sistemi = DergiIslem()

    def goster(self):
        while True:
            print("\n" + "=" * 30)
            print("KUTUPHANE YONETIM SISTEMI")
            print("=" * 30)
            print("1. Kitap Ekle")
            print("2. Kitap Sil")
            print("3. Kitap Guncelle")
            print("4. Kitaplari Listele")
            print("5. Dergi Ekle")
            print("6. Dergi Sil")
            print("7. Dergi Guncelle")
            print("8. Dergileri Listele")
            print("9. Cikis")
            print("=" * 30)

            secim = input("Yapmak istediginiz islemi secin (1-9): ").strip()

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
                print("\nSistemden cikiliyor... Iyi gunler!")
                break
            else:
                print("\nGecersiz secim! Lutfen 1-9 arasinda bir deger girin.")


if __name__ == "__main__":
    sistem = Menu()
    sistem.goster()
