
#kalıtım oluşan bir sınıftaki objeleri başka bir sınıfa çekmeye verilen ad dır.

class çalışanlar():
    def __init__(self , ad , maaş , departman , konum):
        print("eklendi")

        self.ad = ad
        self.maaş = maaş
        self.departman = departman
        self.konum = konum
    def bilgilerigöster(self):
        print(""" AD: {}\n Maaş: {} \n Deparman: {} \n Konum: {}
         """.format(self.ad,self.maaş,self.departman,self.konum))

    def departmandegişti(self , yenidepartman):
        print("departman degişti")
        self.departman = yenidepartman

    def konumdegişti(self , yenikonum):
        print("konum değişti")
        self.konum = yenikonum

    # Kalıtımı gerçekleştiriyoruz.

#class Yönetici (çalışanlar):
      #pass # pass deme sebebimiz hata vermesin diye sonradan ekleme yapıcaz demek.
#yönetici = Yönetici("Fatih Karatekin" , "10000" , "ÜstDüzey Yönetici" , "Yazılım Uzmanı")
#print(yönetici.konumdegişti("CEO"))


#override(overriding) metodu ise yönetici sınıfında  yeni bir parametre eklemek istediginizde
#çalışan sınıfındaki aynı metodu kullansanız bile yeni eklediginiz parametre veya özellik oldugu zaman
#artık çalışanlar sınıfındaki degil yönetici sınıfındaki metodunuz çalışmış olacak
class Yönetici(çalışanlar):
    def __init__(self, ad , maaş , departman , konum , sorumluoldugukişi):
        print("init çalıştı")
        self.ad = ad
        self.maaş = maaş
        self.departman = departman
        self.konum = konum
        self.sorumluoldugukişi= sorumluoldugukişi
    def bilgilerigöster(self):
        print(""" AD: {}\n Maaş: {} \n Deparman: {} \n Konum: {} , \n Sorumluoldugukişi : {}
         """.format(self.ad,self.maaş,self.departman,self.konum,self.sorumluoldugukişi))

yönetim= Yönetici("Fatih Karatekin",20000,"Yönetim" , "CEO" , 500)
print(yönetim.bilgilerigöster())

#diyelimki çalışanlar kısmından 3 tane parametre almak istiyorsunuz
#ve yönetici kısmında buna 1 özellik daha eklemek istiyorsunuz
# super().__init__(ad,maaş,deparman,konum) diyerek çalışanlar sınıfından alabilirsin
# alta tanımlamak istedigin yeni özelligi tanımlayarak devam edebilirsin override gibi uğraştırmaz




