#nesne tabanlı programlama sınıf oluşturup o sınıfaf obje eklemeden geçer
# def __init__(self) metoduyla istedigimiz şekilde objelerin içine farklı atamalar yapabiliriz

#init metodsuz oluşturma şu şekilde
class bilgisayar():
    renk = "siyah"
    marka = "Excalibur"
    fiyat = 7000
    özellik = "GTX"

#sınıfımızı bir objeye aktarıyoruz
sorgu1 = bilgisayar
#çagırıyoruz
print(sorgu1.marka)
#2. objeyi oluşturuyoruz
sorgu2 = bilgisayar
#çagırıyoruz
print(sorgu2.marka)

#console da göründügü gibi 2 ayrı obje oluşturmamıza ragmen aynı sonuçları veriyor eger biz
#farklı objelerde farklı cevaplar görmek istiyorsak init metodunu kullanmalıyız

class araba():
    def __init__(self,marka,renk,fiyat,güç):
        print("tanımlama başarılı")
        self.marka = marka
        self.renk = renk
        self.fiyat = fiyat
        self.güç = güç
tanım1 = araba("ford" , "sarı" , 40000 , 100)
tanım2 = araba("ferrari" , "siyah" , 800000 ,550)
print(tanım1.marka , tanım1.renk , tanım1.fiyat)
print(tanım2.marka , tanım2.renk , tanım2.fiyat )