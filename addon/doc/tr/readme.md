# mp3DirectCut #

* Yazarlar: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* [kararlı  sürüm][1] indir
* [geliştirme sürümü][2] indir

# Sunum #

Bu eklenti, NVDA ile mp3DirectCut yazılımının erişilebilirliğini
iyileştirir.

212'den 223'e kadar olan mp3DirectCut sürümleriyle test edilmiştir.

## Klavye kısayolları ##

Bu eklenti aşağıdaki komutları sunar:

* B

    * B seçiminin başlangıcındaki işaretçinin doğru yerleşimini onaylamak
      için kullanılır.

* Ctrl+Shift+B

    * B seçiminin başlangıcındaki işaretçinin konumunu belirtmek için
      kullanılır.
    * Çift basım, size seçim süresini vermenizi sağlar.

* Ctrl+Shift+D

    * Dosyanın başlangıcından oynatma imlecinin geçerli konumuna kadar olan
      süreyi verir.
    * İki kez basıldığında size toplam süreyi verir.

* Ctrl+R

    * Seçimin iptal edildiğini onaylar.

* Ctrl+Shift+R

    * Oynatma imlecinin mevcut konumundan dosyanın sonuna kadar kalan süreyi
      verir.

* Ctrl+Shift+E

    * N seçiminin sonundaki işaretçinin konumunu belirtmek için kullanılır.
    * İki kez basıldığında, özet B ve N konumlarını ve seçimin süresini
      verir.

* Ctrl+Shift+P

    * Mevcut dosyadaki gerçek parçanın pozisyonunu ve toplam parça sayısını
      verir.

* Ctrl+Shift+boşluk çubuğu

    * Kayıt sırasında vu-metrenin mevcut seviyesini belirlemek için
      kullanılır.
    * İki kez basıldığında seviye sıfırlanır.

* Aşağı ok

    * Oynatma üst bilgisinin geçerli konumunu görmenizi sağlar.
    * Bu komut ayrıca, bir seçim yapılmışsa bu işaretçinin konumunu
      verirken, imleci N seçiminin sonundaki işaretçinin konumuna da
      konumlandırır.
    * Ses seviyesi iletişim kutusunda, genellikle aşağı ok ile ulaşılabilen
      bir sonraki değeri seslendirir.
    * Bu değer varsayılan olarak seslendirilmez.

* End

    * Çalma imlecini geçerli dosyanın sonuna taşır ve toplam süreyi verir.

* Home

    * Çalma imlecini geçerli dosyanın başına taşır.

* Sol ok

    * Oynatma sırasında mevcut süreyi verirken bir saniyelik kısa bir geri
      dönüş yapmanızı sağlar.
    * Bu süre, mp3directcut seçeneklerinde yapılandırılabilir.

* N

    * N seçiminin sonundaki işaretçinin doğru yerleşimini onaylamak için
      kullanılır.

* Page Down

    * Oynatma sırasında mevcut süreyi verirken ileri doğru 10 saniyelik bir
      sıçrama yapar.
    * Bu süre, mp3directcut seçeneklerinde yapılandırılabilir.

* Page Up

    * Oynatma sırasında mevcut süreyi verirken 10 saniye geriye doğru
      sıçrama yapar.
    * Bu süre, mp3directcut seçeneklerinde yapılandırılabilir.

* R

    * Boşluk çubuğuna basarak başlayabileceğiniz kayıt hazırlık penceresini
      açmanızı sağlar.

* Sağ ok

    * Oynatma sırasında mevcut süreyi verip parçayı bir saniye ileri sarar.
    * Bu süre, mp3directcut seçeneklerinde yapılandırılabilir.

* Ctrl+sağ ok

    * Geçerli süreyi veririp bir sonraki bölme noktasına gider.

* Ctrl+Sol ok

    * Geçerli süreyi verirken önceki bölme noktasına gider.

* Shift+sağ ok

    * Mevcut süreyi verip, oynatma sırasında saniyenin yüzde dördü kadar
      ileri sarar.

* Shift+Sol ok

    * Oynatma sırasında mevcut süreyi verip saniyenin yüzde dördü kadar geri
      gider.

* S

    * Okumayı durdurmak ve mevcut süreyi vermek için kullanılır.

* Boşluk çubuğu

    * Kayıt hazırsa, bu kaydı başlatır.
    * Bir kayıt devam ediyorsa, imleci başa getirerek kaydı durdurur.
    * Bir dosya yüklenmişse, okumaya başlatır.
    * Devam eden bir okuma varsa o anki süreyi vererek duraklama yapılmasını
      sağlar.
    * Okuma duraklatılmışsa, okumanın geçerli konumdan yeniden
      başlatılmasını sağlar.

* Yukarı Ok

    * Oynatma üst bilgisinin geçerli konumunu görmenizi sağlar.
    * Bu komut ayrıca, bir seçim yapılmışsa bu işaretçinin konumunu
      verirken, imleci B seçiminin başlangıcındaki işaretçinin konumunda
      konumlandırır.
    * Ses seviyesi iletişim kutusunda, genellikle yukarı ok ile ulaşılabilen
      bir önceki değeri seslendirir.
    * Bu değer varsayılan olarak seslendirilmez.

* NVDA+H

    * Mevcut eklentinin yardımını açar.

## Uyumluluk ##

* Bu eklenti, NVDA'nın 2019.3 ve sonrası sürümleriyle uyumludur.

## 20231007.0.0 için değişiklikler ##

* Kesim noktaları yerleştirildikten ve kesim özellikleri penceresi
  açıldıktan sonra "Ctrl+N" ile bu pencerenin başlığına parça indeksi
  belirtilerek erişilebilirlik eklenir.
* Okuma modunda, seçimlerin başlangıç ​​veya bitiş işaretlerini alfanümerik
  tuş takımının 1'den 6'ya kadar olan tuşlarıyla hareket ettirdikten sonra,
  yeni konumdan otomatik okuma başlangıcının eklenmesi;
* Parçanın başlangıcından itibaren "control+shift+r" ile kalan süreye
  bakılırken oluşan bir hata düzeltildi.

## 20230728.0.0 için değişiklikler ##

* Flake8 ve mypy kuralları koda uygulandı;
* Python 3'te tanıtılan ek açıklamaları desteklemek için desteklenen minimum
  NVDA sürümü 2019.3 olarak değiştirildi.

## 20230508.0.0 ve sonrası için değişiklikler ##

* • Mağaza kurallarına/gereksinimlerine göre sürüm numarası, minimum NVDA
  sürümü ve indirme bağlantısı değiştirildi.

## 20.12 sürümü için değişiklik ##

* En son mp3directcut sürümleri için kayıt ve okuma sırasında konuşmayı
  durdurur;
* Python 3 kullanan yeni NVDA sürümleri için kalan okuma süresinin okunması
  sorunu düzeltildi.

## 19.02 sürümü için değişiklik ##

* Eklenti yapılandırması, nvda 2018.2'den itibaren mevcut olan ayarlar
  paneline eklendi;
* Yıl.ay kullanılarak değiştirilen sürüm numaralandırması. (2 basamaklı yıl,
  ardından nokta, ardından 2 basamaklı ay);
* Nvda 2019.1'den bu yana ortaya çıkan eklentinin yeni sürüm oluşturma
  biçimiyle uyumluluk eklendi.

## 4.0 sürümü için değişiklikler ##

* Eklenti hem Python 2.7 hem de 3 ile uyumlu hale getirildi;
* ASCII olmayan karakterler içeren eklenti yollarıyla ilgili bir hata
  düzeltildi.

## 3.0 sürümü için değişiklikler ##

* Eklentinin yapılandırma iletişim kutusunun doğru görünümünü sağlamak için
  gui.guiHelper modülünü kullandı;
* Biçimlendirilmiş stringler için %s yerine format kullanıldı;
* Uygulama için yönergelere uygunluk kullanıldı.

## 2.3 sürümü için değişiklikler ##

* Eklentiye GPL lisansı eklendi;
* Ctrl + Shift + N, mp3DirectCut'un en son sürümleriyle çalışmadığından,
  sonuna dek seçmeyi sağlayan komut dosyasının kısayolu Ctrl + Shift + N'den
  Ctrl + Shift + E'ye değiştirildi;
* Seçimin 'Ctrl+r' ile iptal edildiğini onaylamak için bir script eklendi;
* AppModule 'mp3directcut.py' kodunda bazı düzeltmeler yapıldı.

## 2.2 sürümü için değişiklikler ##

* Seçim işaretçilerinin konumlarını veren script dosyalarının düzeltilmesi.

## 2.1.1 sürümü için değişiklikler ##

* Toplam süreyi veren script kaldırıldı ve bu bilgiler geçen süreyi veren
  scripte eklendi;
* Modülün yapılandırma seçeneklerinde boşluk tuşu ile ilgili duyuruları
  diğer duyurulardan ayrı olarak etkinleştirme veya devre dışı bırakma
  özelliği eklendi;
* Modülün yapılandırma seçeneklerinde seçim çerçevesinin yerleşim duyurusunu
  etkinleştirme veya devre dışı bırakma özelliği eklendi;
* Kesişim sınırlarından geçerken mevcut parçanın duyrulması eklendi;
* Dikey harflerle ilgili duyuruların düzeltilmesi;
* 'NVDA+H' ile mevcut eklentinin yardımını açmak için bir komut eklendi;
* Eklentinin yapılandırma menüsünün Araçlar menüsünden NVDA'nın Tercihler
  menüsüne kaydırılması.

## 2.1 sürümü için değişiklikler ##

* Control+Sağ Ok ile sonraki bölme noktasına geçişi seslendirmek için bir
  script eklendi;
* Control+Sol Ok ile önceki bölme noktasına geçişi seslendirmek için bir
  script eklendi;
* Shift+Sağ Ok ile saniyenin yüzde 4'ü kadar ileri kaymayı seslendiren bir
  script eklendi;
* Saniyenin yüzde dördü kadar geri kaymayı Shift+Sol Ok ile seslendiren bir
  komut eklendi;
* Eklenti özetinin gösteriminin 'mp3DirectCut için'den 'mp3DirectCut'a
  düzeltildi.

## Sürüm 2.0 için değişiklikler ##

* 'Control Shift R' ile kalan süreyi öğrenebilmek için bir komut eklendi;
* Saatlerinde dahil edildiği okuma süeleri düzeltildi;
* Saniyenin binde birini veya yüzde birini ayırt etme yeteneği eklendi.

## 1.1 sürümü için değişiklikler ##

* Girdi Hareketlerine mp3DirectCut kategorisini dahil etme yeteneği eklendi;

    * Yalnızca mp3DirectCut yazılımının kullanımı sırasında görünür
      olacaklardır.

* NVDA'nın araçlar menüsünde 'mp3DirectCut konfigürasyonu' öğesinde otomatik
  mesajları etkinleştirme veya devre dışı bırakma özelliği eklendi;

## 1.0 sürümü için değişiklikler ##

* İlk sürüm.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mp3DirectCut


[2]: https://www.nvaccess.org/addonStore/legacy?file=mp3DirectCut
