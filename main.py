# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from random import randint
import json
class Sistem():
    def __init__(self):
        self.durum=True
        self.veriler=self.verial()

    def calistir(self):
        self.menu_goster()
        secim=self.secim()

        if secim==1:
            self.giris()
        if secim==2:
            self.kaydol()
        if secim==3:
            self.sifremi_unuttum()
        if secim==4:
            self.cikis()
    def secim(self):
        while True:
            try:
                secim=int(input("Yapmak istediğniz işlemi seçiniz:"))
                if secim>=1 and secim<=4:
                    return secim
                else:
                    print("Lütfen 1-4 arsında seçim yapınız!")
            except ValueError:
                print("Lütfen 1-4 arsında seçim yapınız!")
    def menu_goster(self):
        print("""***Toprak Kayıt Sistemine Hoşgeldiniz***
        1-Giriş
        2-Kayıt Ol
        3-Şifremi Unuttum
        4-Çıkış
        """)
    def giris(self):
        kadi=input("Kullanıcı adı giriniz:")
        sifre=input("Şifrenizi Giriniz:")
        durum = self.kontrol_et(kadi,sifre)
        if durum:
            self.giris_bli()
        else:
            self.giris_bsiz("Hatalı Deneme")


    def kaydol(self):
        kadi=input("Kullanıcı Adı Belirleyiniz:")
        while True:
            sifre=input("Şİfre belirleyiniz:")
            tsifre=input("Belirlediğiniz şifreyi tekrar giriniz:")

            if sifre==tsifre:
                break
            else:
                print("Şifreler uyuşmuyor")
        mail=input("e-mail giriniz:")
        durum=self.kayit_varmi(kadi,mail)
        if durum:
            print("Bu kullanıcı zaten kayıtlı.")
        else:
            gonder_aktivasyon=self.aktivasyonkodgonder()
            aktvdurum=self.aktivasyonKontrol(gonder_aktivasyon)

            if aktvdurum:
                self.kaydet(kadi,sifre,mail)
            else:
                print("Aktivasyon kodu yanlış!")

    def sifremi_unuttum(self):
        mail=input("e-posta adresinizi giriniz:")
        if self.mail_kontrol(mail):
           with open("aktivasyonkoduu.txt","w") as dosya:
               gaktivasyon=str(randint(1000,9999))
               dosya.write(gaktivasyon)

           aktvgir = input("Aktivasyon kodu giriniz")

           if gaktivasyon == aktvgir:
               while True:
                   ysifre = input("Yeni şifrenizi giriniz:")
                   tsifre = input("Şifrenizi tekrar giriniz:")
                   if ysifre == tsifre:
                       break
                   else:
                       print("Girdiğiniz şifreler uyuşmuyor!")

           self.veriler=self.verial()

           for kullanici in self.veriler["kullanicilar"]:
               if kullanici["mail"]==mail:
                   kullanici["sifre"]=str(ysifre)

           with open("kullanicilar.json","w") as dosya:
               json.dump(self.veriler,dosya)
               print("Şifre başarıyla değiştirildi!")
        else:
            print("Böyle bir e-posta bulunamadı!")


    def mail_kontrol(self,mail):
        self.veriler=self.verial()
        for kullanici in self.veriler["kullanicilar"]:
            if kullanici["mail"]==mail:
                return True

        return False

    def cikis(self):
        self.durum=False
    def verial(self):
        try:
            with open("kullanicilar.json","r") as dosya:
                veriler=json.load(dosya)
        except FileNotFoundError:
            with open("kullanicilar.json","w") as dosya:
                dosya.write("{}")

            with open("kullanicilar.json","r") as dosya:
                veriler=json.load(dosya)

        return veriler
    def giris_bli(self):
        print("Giriş Başarılı")
    def giris_bsiz(self,sebep):
        print(sebep)

    def kontrol_et(self,kadi,sifre):
        self.veriler=self.verial()
        for kullanici in self.veriler["kullanicilar"]:

            if kullanici["kadi"]==kadi and kullanici["sifre"]==sifre and kullanici["akitvasyon"]=="Y":
                return True

        return False

    def kayit_varmi(self,kadi,mail):
        self.veriler=self.verial()
        try:
            for kullanici in self.veriler["kullanicilar"]:
                if kullanici["kadi"]==kadi and kullanici["mail"]==mail:
                    return True
        except KeyError:
            return False
        return False
    def kaydet(self,kadi,sifre,mail):
        self.veriler=self.verial()
        try:
            self.veriler["kullanicilar"].append({"kadi": kadi, "sifre": sifre, "mail": mail,"akitvasyon":"Y"})
        except KeyError:
            self.veriler["kullanicilar"]=[]
            self.veriler["kullanicilar"].append({"kadi":kadi,"sifre":sifre,"mail":mail,"akitvasyon":"Y"})

        with open("kullanicilar.json","w") as dosya:
            json.dump(self.veriler,dosya)
            print("Kaydınız oluşturuldu.")


    def aktivasyonkodgonder(self):
        with open("aktivasyonkoduu.txt","w") as dosya:
            gonder_aktivasyon=str(randint(1000,9999))
            dosya.write(gonder_aktivasyon)

        return gonder_aktivasyon

    def aktivasyonKontrol(self,aktivasyon):
        aktivasyona_Al=input("Aktivasyon Kodunuzu giriniz:")
        if aktivasyona_Al==aktivasyon:
            return True
        else:
            return False



sistem=Sistem()
while sistem.durum:
    sistem.calistir()
