rehber= {}
rehber_a={}
#TEXTS ARE TURKISH
def menu():
    print('1. Rehberi yazdir.')
    print('2. Rehbere numara ekle.')
    print('3. Rehberden numara sil.')
    print('4. Rehberden numara ara.')
    print('5. Rehberi Kaydet.')
    print('0. Islemi bitir.')
    
def rehber_yazdir():
    print("1. Kaydedilmis kisiler")
    print("2. Kaydedilmemis kisiler")
    sec=int(input("Secim: "))
    if sec==1:
        kisiler=list(rehber_a.keys())
        numaralar=list(rehber_a.values())
        if(len(kisiler))==0:
            print("Rehberde kayitli numara yok")
        else:
            for x in range (len(rehber_a)):
                print(kisiler[x] + " : " + numaralar[x])
    elif sec==2:
        kisiler=list(rehber.keys())
        numaralar=list(rehber.values())
        if (len(kisiler))==0:
            print("Rehberde kaydedilmemis numara yok!")
        else:
            for x in range (len(rehber)):
                print(kisiler[x] + " : " + numaralar[x])
        
        
def rehber_ekle():
    isim= input("Isim: ")
    while True:
        try:
            telno=int(input("Telefon no: "))
            break
        except:
            print("Lutfen telefon numarasi giriniz!")
    
    telno=str(telno)
    rehber[isim]=telno
    print(isim + " adli kisi basariyla rehbere eklenmistir.")
    
def rehber_kaydet():
    kisiler=list(rehber.keys())
    numaralar=list(rehber.values())
    f=open("rehber.txt",'a')
    for i in range(len(rehber)):
        f.write(kisiler[i] + " : " + numaralar[i] + "\n")
    f.close()
    rehber.clear()
    print(str(len(kisiler)) + " kisi basariyla rehbere kaydedilmistir.")
    num_yukle()


def rehber_sil():
    isim= input("Silinecek kisinin ismi: ")
    rehber1=list(rehber_a.keys())
    if(isim in rehber1):
        del rehber_a[isim]
        print(isim + " adli kisi basariyla silinmistir.")
        
    else:
        print("Rehberde "+ isim + " adli kisi bulunmamaktadir.")
    
def rehber_ara():
    print("1. Isime gore ara")
    print("2. Numaraya gore ara")
    print("3. GSM Operatorune gore ara")
    sec=int(input("Secim: "))
    if sec==1:
        isim=input("Kisinin ismi: ")
        if isim in rehber_a:
            print(isim+ " : "+ rehber[isim])
        else:
            print("Rehberde boyle biri bulunmamaktadir")
    elif sec==2:
        numara=input("Kisinin numarasi: ")
        kisiler=list(rehber_a.keys())
        numaralar=list(rehber_a.values())
        if numara in numaralar:
            print(kisiler[(numaralar.index(numara))]+ " : "+ numara)
        else:
            print("Rehberde boyle bir numara bulunmamaktadir")
    elif sec==3:
        print("Turk Telekom, Turkcell, Vodafone seklinde giriniz")
        gsm=input("GSM numarasi: ")
        if gsm=="Turkcell":
            ara_turkcell()
        elif gsm=="Turk Telekom":
            ara_tt()
        elif gsm=="Vodafone":
            ara_vodafone()
            
def ara_turkcell():
    numaralar=list(rehber_a.values())
    kisiler=list(rehber_a.keys())
    print("Turkcell numaralari:")
    for x in range(530,540):
        for i in range (len(numaralar)):
            s=numaralar[i]
            t=str(x)
            if s.startswith(t):
                print(kisiler[i]+" : "+numaralar[i])

def ara_tt():
    numaralar=list(rehber_a.values())
    kisiler=list(rehber_a.keys())
    print("Turk Telekom numaralari:")
    for x in range(500,510):
        for i in range (len(numaralar)):
            s=numaralar[i]
            t=str(x)
            if s.startswith(t):
                print(kisiler[i]+" : "+numaralar[i])
    for x in range(550,560):
        for i in range (len(numaralar)):
            s=numaralar[i]
            t=str(x)
            if s.startswith(t):
                print(kisiler[i]+" : "+numaralar[i])

def ara_vodafone():
    numaralar=list(rehber_a.values())
    kisiler=list(rehber_a.keys())
    print("Vodafone numaralari:")
    for x in range(540,550):
        for i in range (len(numaralar)):
            s=numaralar[i]
            t=str(x)
            if s.startswith(t):
                print(kisiler[i]+" : "+numaralar[i])

def num_yukle():
    f = open("rehber.txt", "r")
    while True:
        rehber_b = f.readline()
        if not rehber_b:
            break
        rehber_b = rehber_b[:-1]
        name,number = rehber_b.split(" : ")
        rehber_a[name] = number
    f.close()

num_yukle()
menu()
while True:
    secim=int(input("Secim: "))
    if secim==1:
        rehber_yazdir()
    elif secim==2:
        rehber_ekle()
    elif secim==3:
        rehber_sil()
    elif secim==4:
        rehber_ara()
    elif secim==5:
        rehber_kaydet()
    elif secim==0:
        break
    else:
        print("Hatali islem sayisi girdiniz.")