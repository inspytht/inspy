import random #Burada random modülünü yükledim. Bazı yerlerde aynı fonksiyonları kullandığım için açıklama yazmıyorum.
import time #Burada time modülünü yükledim.

print("Sayı tahmin oyunu InSpy")

rastgele = random.randint(1,100) #Randint parametesi ile 1 ve 100 arasında bir sayı oluşturmasını söyledim. Sayı değişkenini rastgele yaptım.
hak = 10 #Kullanıcıya 10 adet tahmin hakkı verdim.
while True: #Sonsuz döngü yarattım. Hak bittiği zaman duracaktır.

    dene = int(input("Bir sayı tahmin ediniz : ")) #Sayı olduğu için int fonksiyonunu kullandım. Girilen sayı değişkenimi dene olarak belirledim, kullanıcıdan sayı girmesini istedim.

    if (dene < rastgele): #İf fonksiyonu ile koşulu belirledim. Rastgele değişkeni ile girilen sayı eşleştirilecek.
        print("Kontrol ediliyor...") #Bunu yazmama gerek yok gibi :/
        time.sleep(1) #1 saniye beklemesini istedim.

        print("Çok düştün çık biraz")

        hak -= 1 #Burada her seferinde verilen haktan 1 düşmesini söyledim.
    elif (dene > rastgele): #elif ile zincirleme karşılaştırma yapmasını istedim. Klavyeden girilecek sayıyı rastgele değişkeni karşılaştıracak.
        print("Kontrol ediliyor...")
        time.sleep(1)

        print("Çok çıktın düş biraz")

        hak -= 1
    else: #Diğer koşullar çalışmaz ise klavyeden girilen sayı doğru olduğu zaman Doğru bildin (sayı) olarak işleyecek.
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Doğru bildin sayı : ",rastgele) #Sayı doğru girildiği zaman rastgele değişkenindeki ile eşleşip uyarı vermesini istedim.
        break #Sayı doğru ise döngü başa dönmeyecek işlemi sonlandıracak.
    if (hak == 0): #Hak değişkenindeki sayı bittiği zaman if fonksiyonu ile kontrol edilip uyarmasını istedim.
        print("Sana verdiğim tahmin hakkı bitti...")
        print("Doğru cevap : ",rastgele) #Verdiğim hak bittiği zaman uyaracak ve rastgele değişkeninden oluşan sayıyı söyleyecek.
        break #Hak bittikten sonra tekrar döngüyü başa dönderip 10 hak daha tanımayacak, işlemi sonlandıracak.