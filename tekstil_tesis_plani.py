import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle

# Deneyim ve başarı bilgileri
RAD_DENEYIM = """
RAD TEKSTİL DENEYİM VE BAŞARILARI
==================================
Rad Tekstil, tekstil sektöründe gösterdiği üstün performans ve kalite odaklı yaklaşımıyla öne çıkmaktadır:

1. Makine ve Ekipman Yönetimi:
   - Modern teknoloji makine parkı kurulumu
   - Optimum yerleşim planı ile maksimum verimlilik
   - Düzenli bakım ve kalibrasyon programları
   - Enerji tasarruflu üretim sistemleri

2. Üretim Süreç Yönetimi:
   - Sıfır fire prensibi ile çalışma
   - Kalite kontrol sistemlerinin etkin kullanımı
   - Üretim süreçlerinin sürekli optimizasyonu
   - Modern üretim teknikleri uygulaması

3. Kalite Standartları:
   - ISO 9001 Kalite Yönetim Sistemi
   - Uluslararası kalite standartlarına uygunluk
   - Düzenli kalite denetim süreçleri
   - Müşteri memnuniyeti odaklı üretim

4. Başarılar:
   - Sıfır fire ile üretim hedeflerine ulaşma
   - Yüksek kaliteli ürün portföyü
   - Müşteri memnuniyetinde sürekli artış
   - Sektörde örnek gösterilen üretim tesisi
"""

# Tesis boyutları (metre cinsinden)
TESIS_GENISLIK = 50
TESIS_UZUNLUK = 100

# Makine ve donanım bilgileri
makineler = {
    'Örme Makinesi': {
        'adet': 10,
        'boyut': (3, 2),
        'maliyet': 150000,
        'güç_tüketimi': 5.5,  # kW
        'üretim_kapasitesi': 100,  # kg/gün
        'fire_oranı': 0.001  # %0.1
    },
    'Dokuma Tezgahı': {
        'adet': 15,
        'boyut': (4, 2.5),
        'maliyet': 200000,
        'güç_tüketimi': 7.5,
        'üretim_kapasitesi': 150,
        'fire_oranı': 0.001
    },
    'Boya Makinesi': {
        'adet': 5,
        'boyut': (6, 3),
        'maliyet': 300000,
        'güç_tüketimi': 15.0,
        'üretim_kapasitesi': 200,
        'fire_oranı': 0.002
    },
    'Kurutma Ünitesi': {
        'adet': 3,
        'boyut': (8, 4),
        'maliyet': 250000,
        'güç_tüketimi': 20.0,
        'üretim_kapasitesi': 300,
        'fire_oranı': 0.001
    },
    'Kalite Kontrol Masası': {
        'adet': 4,
        'boyut': (3, 1.5),
        'maliyet': 15000,
        'güç_tüketimi': 1.0,
        'üretim_kapasitesi': 400,
        'fire_oranı': 0.0
    }
}

# Yerleşim planı çizimi
plt.figure(figsize=(15, 10))

# Tesis sınırları
plt.subplot(2, 2, 1)
plt.title('Tesis Yerleşim Planı')
plt.gca().add_patch(Rectangle((0, 0), TESIS_UZUNLUK, TESIS_GENISLIK, 
                            fill=False, color='black'))

# Makine yerleşimleri (basit gösterim)
colors = ['red', 'blue', 'green', 'orange', 'purple']
x, y = 5, 5
for (makine_adi, ozellikler), color in zip(makineler.items(), colors):
    for i in range(ozellikler['adet']):
        width, height = ozellikler['boyut']
        if x + width > TESIS_UZUNLUK - 5:
            x = 5
            y += 8
        plt.gca().add_patch(Rectangle((x, y), width, height, 
                                    fill=True, color=color, alpha=0.5))
        plt.text(x + width/2, y + height/2, makine_adi.split()[0], 
                ha='center', va='center')
        x += width + 2

plt.xlim(-5, TESIS_UZUNLUK + 5)
plt.ylim(-5, TESIS_GENISLIK + 5)
plt.grid(True)

# Maliyet dağılımı
plt.subplot(2, 2, 2)
maliyetler = {k: v['adet'] * v['maliyet'] for k, v in makineler.items()}
plt.pie(maliyetler.values(), labels=maliyetler.keys(), autopct='%1.1f%%')
plt.title('Makine Maliyetleri Dağılımı')

# Güç tüketimi analizi
plt.subplot(2, 2, 3)
güç_tüketimi = {k: v['adet'] * v['güç_tüketimi'] for k, v in makineler.items()}
plt.bar(güç_tüketimi.keys(), güç_tüketimi.values())
plt.xticks(rotation=45)
plt.title('Toplam Güç Tüketimi (kW)')
plt.tight_layout()

# Üretim kapasitesi analizi
plt.subplot(2, 2, 4)
kapasite = {k: v['adet'] * v['üretim_kapasitesi'] for k, v in makineler.items()}
plt.bar(kapasite.keys(), kapasite.values())
plt.xticks(rotation=45)
plt.title('Günlük Üretim Kapasitesi (kg/gün)')
plt.tight_layout()

plt.savefig('tekstil_tesis_raporu.png', dpi=300, bbox_inches='tight')

# İstatistiksel rapor oluşturma
print(RAD_DENEYIM)

print("\nRAD TEKSTİL TESİS PLANLAMA RAPORU")
print("=" * 50)
print("\n1. GENEL BİLGİLER")
print(f"Tesis Boyutları: {TESIS_UZUNLUK}m x {TESIS_GENISLIK}m")
print(f"Toplam Alan: {TESIS_UZUNLUK * TESIS_GENISLIK} m²")

print("\n2. MAKİNE PARKI VE KALİTE PERFORMANSI")
for makine, özellik in makineler.items():
    print(f"\n{makine}:")
    print(f"  - Adet: {özellik['adet']}")
    print(f"  - Boyutlar: {özellik['boyut'][0]}m x {özellik['boyut'][1]}m")
    print(f"  - Birim Maliyet: {özellik['maliyet']:,} TL")
    print(f"  - Güç Tüketimi: {özellik['güç_tüketimi']} kW")
    print(f"  - Günlük Kapasite: {özellik['üretim_kapasitesi']} kg/gün")
    print(f"  - Fire Oranı: %{özellik['fire_oranı']*100:.3f}")

print("\n3. TOPLAM MALİYET ANALİZİ")
toplam_maliyet = sum(v['adet'] * v['maliyet'] for v in makineler.values())
print(f"Toplam Makine Yatırımı: {toplam_maliyet:,} TL")

print("\n4. ENERJİ TÜKETİMİ")
toplam_güç = sum(v['adet'] * v['güç_tüketimi'] for v in makineler.values())
print(f"Toplam Güç Tüketimi: {toplam_güç:,.2f} kW")
günlük_enerji = toplam_güç * 16  # 16 saat çalışma varsayımı
print(f"Tahmini Günlük Enerji Tüketimi: {günlük_enerji:,.2f} kWh")

print("\n5. ÜRETİM KAPASİTESİ VE KALİTE")
toplam_kapasite = sum(v['adet'] * v['üretim_kapasitesi'] for v in makineler.values())
ortalama_fire = sum(v['fire_oranı'] * v['adet'] * v['üretim_kapasitesi'] 
                   for v in makineler.values()) / toplam_kapasite
print(f"Toplam Günlük Üretim Kapasitesi: {toplam_kapasite:,} kg/gün")
print(f"Tahmini Aylık Kapasite: {toplam_kapasite * 26:,} kg/ay")  # 26 iş günü varsayımı
print(f"Ortalama Fire Oranı: %{ortalama_fire*100:.3f}")
print(f"Kalite Başarı Oranı: %{(1-ortalama_fire)*100:.3f}")

print("\n6. KALİTE VE VERİMLİLİK BAŞARILARI")
print("- Sıfıra yakın fire oranı ile üretim")
print("- ISO 9001 kalite standartlarına uygunluk")
print("- Sürekli iyileştirme ve optimizasyon")
print("- Modern teknoloji kullanımı")
print("- Enerji verimli üretim sistemleri")
print("- Yüksek müşteri memnuniyeti") 