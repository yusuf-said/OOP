##Multiple Inheritance ile alakalı alıştırmalar oluşturdum.
#banka bireysel musteri sirket musterisi ve hem bireysel sirket hesapları

class Musteri():
    def __init__(self,ad, soyad, hesapNo, yil):

        self.ad = ad
        self.soyad = soyad
        self.hesapNo = hesapNo
        self.yil = yil
    def hesapBilgi(self):
        return f'''Ad: {self.ad},
        Soyad: {self.soyad}
        HesapNo: {self.hesapNo}
        '''

class BireyselMusteri(Musteri):

    def __init__(self,ad, soyad, hesapNo, yil):

        super().__init__(ad,soyad,hesapNo,yil)
        self.para_cekim_komisyon = 0.15
        self.faiz = 4.59

    def ParaCekmeBilgi(self,miktar):
        self.miktar = miktar
        return f"odenecek komisyon {miktar * self.para_cekim_komisyon}"
    
    def KrediMaliyet(self,miktar,vade):
        return vade * miktar * self.faiz
    


class SirketMusteri(Musteri):
    
    def __init__(self,sirket_isim, hesapNo, yil):
        super().__init__(hesapNo,yil)
        self.sirket_isim = sirket_isim
        self.faiz = 3.56
        self.para_cekim_komisyon = 0.05



    def ParaCekmeBilgi(self,miktar):
        return f"odenecek komisyon {miktar * self.para_cekim_komisyon}"

    def KrediMaliyet(self,miktar,vade):
        return vade * miktar * self.faiz
    
    def hesapBilgi(self):
        return f''' Şirket İsim: {self.sirket_isim},
        HesapNo: {self.hesapNo}
        '''
        









