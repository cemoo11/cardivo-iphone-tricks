"""Türkçe iPhone özellik bankası (slaytlar için).

Her öğe: id, tema, başlık, açıklama, ayar yolu (Türkçe iOS menü adlarıyla).
"""

THEMES_TR = {
    "camera": "kamera ",
    "keyboard": "klavye ",
    "settings": "",
    "battery": "pil ",
    "privacy": "gizlilik ",
    "messages": "",
    "productivity": "",
    "safety": "güvenlik ",
    "health": "sağlık ",
    "accessibility": "",
}

TIPS_TR = [
    # kamera
    ("quicktake", "camera", "Basılı tutmadan video çek", "Fotoğraf modunda deklanşöre bas ve sağa kaydır; video eller serbest devam eder.", "Kamera › Deklanşörü sağa kaydır"),
    ("grid-level", "camera", "Izgara ve terazi", "Izgarayı ve teraziyi aç, her fotoğrafın dümdüz çıksın.", "Ayarlar › Kamera › Izgara / Terazi"),
    ("volume-shutter", "camera", "Ses tuşuyla çek", "Ses açma tuşuna bas, fotoğraf çeksin. Basılı tutarsan video başlar.", "Kamera › Ses açma tuşuna bas"),
    ("burst", "camera", "Seri çekim", "Deklanşörü sola kaydır, saniyede onlarca fotoğraf çek.", "Kamera › Deklanşörü sola kaydır"),
    ("mirror-front", "camera", "Selfie'ler ters çıkmasın", "Ön kamera fotoğrafını önizlemede gördüğün gibi kaydet.", "Ayarlar › Kamera › Ön Kamerayı Yansıt"),
    ("live-text", "camera", "Gerçek dünyadan metin kopyala", "Kamerayı bir yazıya tut ve Canlı Metin simgesine dokunarak kopyala.", "Kamera › Canlı Metin simgesi"),
    ("scan-docs", "camera", "Gizli belge tarayıcı", "Kâğıt belgeleri Notlar içinden tertemiz PDF'e çevir.", "Notlar › Ataç › Belgeleri Tara"),
    ("magnifier", "camera", "Büyüteç", "iPhone'unu fenerli bir büyütece dönüştür.", "Uygulama Arşivi › Büyüteç"),
    ("measure", "camera", "Her şeyi ölç", "Kamerayla eşyaları, odaları hatta insanların boyunu ölç.", "Uygulama Arşivi › Ölçüm"),
    ("visual-lookup", "camera", "Bitkiyi, hayvanı tanı", "Fotoğrafı aç, bilgi simgesine dokun; bitkiyi, hayvanı ve yeri söylesin.", "Fotoğraflar › Fotoğrafı aç › Bilgi simgesi"),
    # klavye
    ("trackpad", "keyboard", "Klavye = trackpad", "Boşluk tuşuna basılı tut, klavye trackpad'e dönüşsün ve imleci kolayca taşı.", "Herhangi bir metin alanı › Boşluk tuşunu basılı tut"),
    ("text-replacement", "keyboard", "Metin değiştirme", "\"@@\" yaz, iPhone onu tam e-posta adresine çevirsin.", "Ayarlar › Genel › Klavye › Metin Değiştirme"),
    ("shake-undo", "keyboard", "Salla, geri al", "Yanlışlıkla bir şey mi sildin? Telefonu salla, geri gelsin.", "Ayarlar › Erişilebilirlik › Dokunma › Geri Almak İçin Salla"),
    ("one-hand-keyboard", "keyboard", "Tek elle klavye", "Klavyeyi bir yana küçült, tek elle rahat yaz.", "Emoji / dünya tuşunu basılı tut › Sol veya sağ"),
    ("calc-delete", "keyboard", "Hesap makinesinde sil", "Sayının üzerinde sağa ya da sola kaydır, son rakam silinsin.", "Hesap Makinesi › Ekranda kaydır"),
    ("three-finger-undo", "keyboard", "Üç parmakla geri al", "Üç parmakla sola kaydır geri al, sağa kaydır yinele.", "Herhangi bir uygulama › Üç parmakla kaydır"),
    ("double-space", "keyboard", "Çift boşluk = nokta", "Boşluk tuşuna iki kez dokun, otomatik nokta ve boşluk eklensin.", "Ayarlar › Genel › Klavye › \".\" Kestirmesi"),
    ("haptic-keyboard", "keyboard", "Titreşimli klavye", "Her tuşta hafif bir titreşim hisset, daha hızlı yaz.", "Ayarlar › Sesler ve Dokunuş › Klavye Geri Bildirimi"),
    # ayarlar
    ("back-tap", "settings", "Arkaya Dokunma", "Telefonun arkasına iki ya da üç kez vur; ekran görüntüsü alsın, uygulama açsın.", "Ayarlar › Erişilebilirlik › Dokunma › Arkaya Dokunma"),
    ("tap-top", "settings", "Tek dokunuşla en üste", "Ekranın en üstüne dokun, her listenin başına anında dön.", "Herhangi bir uygulama › Durum çubuğuna dokun"),
    ("reduce-white-point", "settings", "En düşükten de karanlık", "Ekranı en düşük parlaklıktan bile daha karanlık yap; gece göz yormaz.", "Ayarlar › Erişilebilirlik › Ekran ve Metin Puntosu › Beyaz Noktayı Azalt"),
    ("led-flash", "settings", "Bildirimde flaş yansın", "Arama veya bildirim gelince kamera flaşı yanıp sönsün.", "Ayarlar › Erişilebilirlik › İşitsel ve Görsel › Uyarılar İçin LED Flaş"),
    ("lock-apps", "settings", "Uygulamaları kilitle", "İstediğin uygulamayı Face ID ile kilitle ya da tamamen gizle.", "Uygulama simgesini basılı tut › Face ID İste"),
    ("drag-apps", "settings", "Çok uygulamayı birden taşı", "Bir uygulamayı sürüklerken başka parmakla diğerlerine dokun, hepsini birlikte taşı.", "Ana Ekran › Uygulamayı basılı tut › Diğerlerine dokun"),
    ("home-search", "settings", "Her yerden ara", "Ana Ekran'da aşağı kaydır; uygulama, mesaj, ayar, her şeyi ara.", "Ana Ekran › Aşağı kaydır"),
    ("dark-icons", "settings", "Koyu ve renkli simgeler", "Uygulama simgelerini koyu ya da duvar kâğıdına uygun renkte yap.", "Ana Ekran'ı basılı tut › Düzenle › Özelleştir"),
    ("action-button", "settings", "Eylem düğmesi", "Eylem düğmesini fener, kamera ya da kestirme olarak ayarla.", "Ayarlar › Eylem Düğmesi"),
    # pil
    ("charge-limit", "battery", "%80 şarj sınırı", "Şarjı %80'de durdur, pilin daha yavaş yıpransın.", "Ayarlar › Pil › Şarj Etme"),
    ("battery-percent", "battery", "Pil yüzdesi", "Tam pil yüzdesini durum çubuğunda göster.", "Ayarlar › Pil › Pil Yüzdesi"),
    ("low-power", "battery", "Düşük Güç Modu", "Arka plan işlemlerini kıs, pil biterken saatlerce daha dayan.", "Ayarlar › Pil › Düşük Güç Modu"),
    ("battery-health", "battery", "Pil sağlığını gör", "Pilinin maksimum kapasitesini ve döngü sayısını saniyeler içinde gör.", "Ayarlar › Pil › Pil Sağlığı"),
    ("bg-refresh", "battery", "Arka planda yenilemeyi kapat", "Az kullandığın uygulamalar arka planda pil yemesin.", "Ayarlar › Genel › Arka Planda Uygulama Yenileme"),
    # gizlilik
    ("stolen-device", "privacy", "Çalınan Aygıt Koruması", "Telefonun çalınsa bile önemli ayarlar Face ID ve bekleme süresi olmadan değişmez.", "Ayarlar › Face ID ve Parola › Çalınan Aygıt Koruması"),
    ("safety-check", "privacy", "Güvenlik Denetimi", "Kimin, hangi uygulamanın verine eriştiğini gör ve tek dokunuşla sıfırla.", "Ayarlar › Gizlilik ve Güvenlik › Güvenlik Denetimi"),
    ("privacy-report", "privacy", "Uygulama Gizlilik Raporu", "Hangi uygulama kameranı, mikrofonunu ve konumunu ne zaman kullandı, gör.", "Ayarlar › Gizlilik ve Güvenlik › Uygulama Gizlilik Raporu"),
    ("silence-callers", "privacy", "Bilinmeyen numaraları sustur", "Rehberinde olmayan numaralar doğrudan sesli mesaja düşsün.", "Ayarlar › Uygulamalar › Telefon › Bilinmeyen Arayanları Sustur"),
    ("hidden-album", "privacy", "Gizli albümü kilitle", "Gizli ve Son Silinenler albümleri Face ID olmadan açılmasın.", "Ayarlar › Uygulamalar › Fotoğraflar › Face ID'yi Kullan"),
    ("passwords-app", "privacy", "Parolalar uygulaması", "Tüm şifrelerin, geçiş anahtarların ve Wi-Fi şifrelerin tek yerde.", "Uygulama Arşivi › Parolalar"),
    ("share-wifi", "privacy", "Wi-Fi şifresini tek dokunuşla paylaş", "Kilidi açık iPhone'unu arkadaşının telefonuna yaklaştır, şifre otomatik gitsin.", "iPhone'u arkadaşının iPhone'una yaklaştır"),
    # mesajlar & fotoğraflar
    ("send-later", "messages", "Mesajı zamanla", "Mesajı şimdi yaz, istediğin saatte kendiliğinden gitsin.", "Mesajlar › + › Sonra Gönder"),
    ("undo-send", "messages", "Mesajı düzenle ya da geri al", "Gönderdiğin iMessage'daki hatayı düzelt ya da geri çek.", "Mesajlar › Mesajı basılı tut › Düzenle / Göndermeyi Geri Al"),
    ("lift-subject", "messages", "Fotoğraftan nesneyi kes", "Fotoğraftaki kişiye ya da nesneye basılı tut, arka planından ayırıp her yere yapıştır.", "Fotoğraflar › Nesneye basılı tut"),
    ("duplicates", "messages", "Kopya fotoğrafları birleştir", "Aynı fotoğrafları bul, birleştir ve yer aç.", "Fotoğraflar › Yardımcı Araçlar › Yinelenenler"),
    ("recently-deleted", "messages", "Silinen fotoğrafları geri getir", "Sildiğin fotoğraflar 30 gün boyunca Son Silinenler'de bekler.", "Fotoğraflar › Yardımcı Araçlar › Son Silinenler"),
    ("namedrop", "messages", "NameDrop", "İki iPhone'un üst kısmını birbirine yaklaştır, numaralar anında değişsin.", "iPhone'ları üstten birbirine yaklaştır"),
    # üretkenlik
    ("listen-page", "productivity", "Web sayfasını dinle", "Safari makaleyi sesli okusun, sen başka işine bak.", "Safari › Sayfa menüsü › Sayfayı Dinle"),
    ("hide-distracting", "productivity", "Reklamları ve pop-up'ları gizle", "Web sayfasındaki dikkat dağıtan öğeleri Safari'de tek dokunuşla kaldır.", "Safari › Sayfa menüsü › Dikkat Dağıtan Öğeleri Gizle"),
    ("math-notes", "productivity", "Notlar'da matematik", "Notlar'a \"=\" ile biten bir işlem yaz, sonuç anında gelsin.", "Notlar › 24*18= yaz"),
    ("unit-convert", "productivity", "Hesap makinesinde döviz çevir", "Döviz, uzunluk, ağırlık… hepsini Hesap Makinesi'nde çevir.", "Hesap Makinesi › Hesap makinesi simgesi › Dönüştür"),
    ("offline-maps", "productivity", "Çevrimdışı haritalar", "Haritayı indir, çekmeyen yerde bile yol tarifi al.", "Haritalar › Profil › Çevrimdışı Haritalar"),
    ("translate", "productivity", "Canlı sohbet çevirisi", "Başka dilde biriyle konuş, iki taraf da anında çevrilsin.", "Çeviri › Sohbet"),
    # güvenlik
    ("emergency-sos", "safety", "Acil Durum SOS", "Yan tuş ve ses tuşunu basılı tut, acil servisi hızla ara.", "Ayarlar › Acil Durum SOS"),
    ("crash-detection", "safety", "Kaza Algılama", "iPhone ciddi bir trafik kazasını algılayıp yardım çağırabilir.", "Ayarlar › Acil Durum SOS › Ciddi Kazadan Sonra Ara"),
    ("medical-id", "safety", "Kilit ekranında Tıbbi Kimlik", "Acil durumda ekipler kilidi açmadan alerjilerini ve acil kişilerini görebilir.", "Sağlık › Profil › Tıbbi Kimlik › Kilitliyken Göster"),
    # sağlık
    ("screen-distance", "health", "Ekran Mesafesi", "Telefonu gözüne 30 cm'den fazla yaklaştırınca iPhone seni uyarır.", "Ayarlar › Ekran Süresi › Ekran Mesafesi"),
    ("walking-steadiness", "health", "Yürüme Dengesi", "Cebindeki iPhone yürüme dengeni takip eder, düşerse seni uyarır.", "Sağlık › Göz At › Hareketlilik › Yürüme Dengesi"),
    ("loud-audio", "health", "Yüksek Sesi Azalt", "Kulaklık sesi belirlediğin seviyeyi geçince otomatik kısılır.", "Ayarlar › Sesler ve Dokunuş › Kulaklık Güvenliği"),
    ("motion-cues", "health", "Araç Hareketi İpuçları", "Ekrandaki hareketli noktalar arabada telefona bakarken mide bulantısını azaltır.", "Ayarlar › Erişilebilirlik › Hareket › Araç Hareketi İpuçları"),
    ("background-sounds", "health", "Arka Plan Sesleri", "Yağmur, okyanus, dere sesleriyle odaklan ya da rahatla.", "Ayarlar › Erişilebilirlik › İşitsel ve Görsel › Arka Plan Sesleri"),
    ("medications", "health", "İlaç hatırlatıcı", "İlaçlarını ve vitaminlerini kaydet, saati gelince hatırlatsın.", "Sağlık › Göz At › İlaçlar"),
    ("night-shift", "health", "Gece Vardiyası", "Gün batımından sonra ekran otomatik olarak sıcak renklere geçsin.", "Ayarlar › Ekran ve Parlaklık › Gece Vardiyası"),
    # erişilebilirlik
    ("sound-recognition", "accessibility", "Ses Tanıma", "Kapı zili, bebek ağlaması ya da yangın alarmı duyunca iPhone seni uyarsın.", "Ayarlar › Erişilebilirlik › Ses Tanıma"),
    ("eye-tracking", "accessibility", "Gözlerinle kontrol et", "iPhone'u sadece gözlerinle ve ön kamerayla kullan.", "Ayarlar › Erişilebilirlik › Göz Takibi"),
    ("live-listen", "accessibility", "Canlı Dinleme", "iPhone'u mikrofon gibi kullan, sesi AirPods'una aktarsın.", "Denetim Merkezi › İşitme › Canlı Dinleme"),
    ("assistive-access", "accessibility", "Ailen için sade iPhone", "Büyük düğmeler ve sadece gereken uygulamalarla basit bir iPhone hazırla.", "Ayarlar › Erişilebilirlik › Yardımcı Erişim"),
]
