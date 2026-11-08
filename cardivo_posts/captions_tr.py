"""Türkçe TikTok açıklama üreticisi: viral giriş + iPhone taktikleri + Cardivo tanıtımı + indirme adımları."""
import random

HOOKS = [
    "iPhone'unda bunları bilmiyorsan çok şey kaçırıyorsun 😳",
    "Apple'ın sana söylemediği iPhone özellikleri 🤫",
    "Bunu öğrendikten sonra iPhone'unu bambaşka kullanacaksın 📱",
    "iPhone kullanıyorsan bunu hemen kaydet 📌",
    "iPhone kullanıcılarının %99'u bunları bilmiyor 👀",
    "iPhone'unda hemen açman gereken ayarlar ⚙️",
    "Yıllardır iPhone kullanıp bunları bilmeyenler buraya 🙋",
    "Keşke daha önce bilseydim dediğin iPhone taktikleri 😩",
    "Bunu bilen iPhone kullanıcısı çok az 🤫",
    "iPhone hileleri Bölüm {n} 🔥",
    "Telefonun sandığından çok daha akıllı 🧠",
    "Bu iPhone özelliklerini görünce şok olacaksın 😮",
    "Arkadaşların bunu bilmiyor, sen öğren 😎",
    "iPhone'un gizli kalmış en iyi özellikleri ✨",
    "Bunları bilmeden iPhone kullanma 🚫",
    "Her iPhone kullanıcısının bilmesi gerekenler 📲",
    "iPhone'unda saklı kalan taktikler 🔍",
    "Son madde herkesi şaşırtıyor 👇",
]

SUB_HOOKS = [
    "Kaydet, sonra lazım olacak 📌",
    "Hangisini bilmiyordun? Yorumlara yaz 👇",
    "Bilmeyen bir arkadaşına gönder 📤",
    "Her gün yeni iPhone taktiği için takip et ➕",
    "Kaçıncı maddede şaşırdın? Yorumda söyle 👀",
    "Sonuna kadar kaydır, en iyisi sonda 👉",
    "Bölüm {n} — serinin devamı için takipte kal 🔔",
]

TRICK_INTROS = [
    "🔥 Bonus iPhone taktikleri:",
    "📱 Bunları da dene:",
    "✨ Daha fazla gizli özellik:",
    "💡 Ekstra iPhone hileleri:",
]

CAPTION_TRICKS = [
    "Telefonun arkasına iki kez vur → ekran görüntüsü al (Arkaya Dokunma)",
    "Boşluk tuşuna basılı tut → klavye trackpad'e dönüşür",
    "Hesap makinesinde sayının üstünde kaydır → son rakam silinir",
    "Ekranın en üstüne dokun → listenin başına anında dön",
    "Fotoğraftaki kişiye basılı tut → arka planından ayır",
    "Ana Ekran'da aşağı kaydır → her şeyi ara",
    "Telefonu salla → yazdığını geri al",
    "Mesajlar'da + › Sonra Gönder → mesajı zamanla",
    "Gönderdiğin iMessage'ı basılı tut → düzenle ya da geri al",
    "Ses açma tuşu → fotoğraf, basılı tut → video",
    "Kamerayı yazıya tut → Canlı Metin ile kopyala",
    "Notlar'da belge tara → anında PDF",
    "Notlar'a 24*18= yaz → sonuç anında gelir",
    "Hesap Makinesi'nde döviz çevir",
    "Uygulama simgesine basılı tut → Face ID ile kilitle",
    "iPhone'ları yaklaştır → Wi-Fi şifresi otomatik paylaşılır",
    "İki iPhone'u üstten birleştir → NameDrop ile numara değiş",
    "Şarjı %80'de sınırla → pil daha geç yıpranır",
    "Silinen fotoğraflar 30 gün Son Silinenler'de",
    "Haritaları indir → internetsiz yol tarifi",
    "Safari'de Sayfayı Dinle → makaleler sesli okunur",
    "Bildirim gelince flaş yansın (LED Flaş)",
    "Beyaz Noktayı Azalt → ekran en düşükten de karanlık",
]

CARDIVO_ABOUT = [
    "💓 Cardivo nedir?\nSadece parmağını iPhone kamerasına koyarak nabzını ölçen uygulama. Akıllı saate gerek yok; ölçümlerini kaydeder, gelişimini grafiklerle gösterir.",
    "❤️ Bonus: Cardivo\niPhone kameran aslında bir nabız ölçere dönüşebiliyor! Parmağını arka kameraya koy, Cardivo nabzını saniyeler içinde ölçsün ve geçmişini takip etsin.",
    "💡 Son taktik: Cardivo\nSaat takmadan nabzını ölçmek ister misin? Cardivo kamera ve flaşı kullanarak kalp atışını ölçer, sonuçlarını günlük olarak kaydeder.",
    "📈 Cardivo ile tanış\nKamerayla nabız ölçümü, kalp atışı geçmişi, sade grafikler ve günlük seriler. Hepsi iPhone'unda, ekstra cihaz olmadan.",
]

CTA_STEPS = [
    "📲 Nasıl indirilir?\n1. App Store'u aç\n2. \"Cardivo\" yaz\n3. \"Al\" butonuna dokun — ücretsiz indir",
    "📲 Cardivo'yu indirmek için:\n1. App Store'a gir\n2. Arama kısmına \"Cardivo\" yaz\n3. İndir ve hemen ölç",
    "👉 İndirmesi 10 saniye:\nApp Store › \"Cardivo\" ara › Al",
]

CORE_TAGS = ["#iphone", "#iphonetaktikleri", "#cardivo"]
ROTATING_TAGS = [
    "#iphoneipuçları", "#iphonehileleri", "#apple", "#ios", "#teknoloji", "#keşfet",
    "#keşfetbeniöneçıkar", "#fyp", "#iphonetürkiye", "#teknolojitaktikleri", "#ios18",
    "#iphone16", "#iphone15", "#iphone17", "#appletürkiye", "#bilgi", "#hayathileleri",
    "#telefontaktikleri", "#keşfetteyiz",
]


def build_caption_tr(rng: random.Random, part_no: int) -> str:
    lines = [rng.choice(HOOKS).format(n=part_no), rng.choice(SUB_HOOKS).format(n=part_no), ""]
    lines.append(rng.choice(TRICK_INTROS))
    lines += [f"• {t}" for t in rng.sample(CAPTION_TRICKS, rng.randint(4, 6))]
    lines += ["", rng.choice(CARDIVO_ABOUT), "", rng.choice(CTA_STEPS), ""]
    tags = CORE_TAGS + rng.sample(ROTATING_TAGS, rng.randint(4, 6))
    rng.shuffle(tags)
    lines.append(" ".join(tags))
    return "\n".join(lines)
