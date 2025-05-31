import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import numpy as np

# Sample veri oluşturma
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
n_incidents = len(dates)

data = {
    'Tarih': dates,
    'Yangin_Sayisi': np.random.poisson(lam=5, size=n_incidents),
    'Mudahale_Suresi_Dk': np.random.normal(15, 5, n_incidents),
    'Bolge': np.random.choice(['Merkez', 'Kuzey', 'Güney', 'Doğu', 'Batı'], n_incidents),
    'Yangin_Turu': np.random.choice(['Ev', 'İşyeri', 'Orman', 'Araç', 'Diğer'], n_incidents, 
                                   p=[0.4, 0.2, 0.15, 0.15, 0.1])
}

df = pd.DataFrame(data)

# Grafikleri oluşturma
plt.figure(figsize=(15, 10))

# 1. Aylık yangın sayısı trendi
plt.subplot(2, 2, 1)
monthly_fires = df.groupby(df['Tarih'].dt.strftime('%Y-%m'))['Yangin_Sayisi'].sum()
plt.plot(range(len(monthly_fires)), monthly_fires.values, marker='o')
plt.title('Aylık Yangın Sayısı Trendi (2023)')
plt.xlabel('Ay')
plt.ylabel('Yangın Sayısı')
plt.xticks(range(len(monthly_fires)), ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 
                                      'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'], 
           rotation=45)

# 2. Bölgelere göre yangın dağılımı
plt.subplot(2, 2, 2)
df['Bolge'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Bölgelere Göre Yangın Dağılımı')

# 3. Yangın türlerine göre dağılım
plt.subplot(2, 2, 3)
sns.barplot(x=df['Yangin_Turu'].value_counts().index, 
            y=df['Yangin_Turu'].value_counts().values)
plt.title('Yangın Türlerine Göre Dağılım')
plt.xticks(rotation=45)
plt.xlabel('Yangın Türü')
plt.ylabel('Sayı')

# 4. Ortalama müdahale süresi dağılımı
plt.subplot(2, 2, 4)
sns.boxplot(x='Bolge', y='Mudahale_Suresi_Dk', data=df)
plt.title('Bölgelere Göre Müdahale Süresi Dağılımı')
plt.xlabel('Bölge')
plt.ylabel('Müdahale Süresi (Dakika)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('yangin_analiz_raporu.png', dpi=300, bbox_inches='tight')

# İstatistiksel özet raporu
print("\nYANGIN ANALİZ RAPORU - 2023")
print("=" * 50)
print(f"\nToplam Yangın Sayısı: {df['Yangin_Sayisi'].sum()}")
print(f"Ortalama Günlük Yangın Sayısı: {df['Yangin_Sayisi'].mean():.2f}")
print(f"Ortalama Müdahale Süresi: {df['Mudahale_Suresi_Dk'].mean():.2f} dakika")
print("\nBölgelere Göre Yangın Sayıları:")
print(df.groupby('Bolge')['Yangin_Sayisi'].sum().sort_values(ascending=False))
print("\nYangın Türlerine Göre Dağılım:")
print(df.groupby('Yangin_Turu')['Yangin_Sayisi'].sum().sort_values(ascending=False)) 