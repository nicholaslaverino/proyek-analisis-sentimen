import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- PENGATURAN FONT ALA PAPER AKADEMIK ---
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

# Daftar file data bersih yang sudah kita buat sebelumnya
apps = ['satusehat', 'signal', 'ikd']
all_dfs = []

print("=== 1. TABEL DISTRIBUSI DATA ===")
summary_data = []

for app in apps:
    df = pd.read_csv(f"{app}_cleaned_reviews.csv")
    all_dfs.append(df)
    
    # Hitung jumlah per sentimen
    counts = df['sentiment'].value_counts()
    pos = counts.get('Positif', 0)
    neg = counts.get('Negatif', 0)
    total = pos + neg
    
    summary_data.append({
        'Aplikasi': app.upper(),
        'Total Ulasan': total,
        'Positif (n)': pos,
        'Positif (%)': round((pos/total)*100, 2),
        'Negatif (n)': neg,
        'Negatif (%)': round((neg/total)*100, 2)
    })

# Tampilkan Tabel Distribusi
df_summary = pd.DataFrame(summary_data)
print(df_summary.to_string(index=False))

print("\n=== 2. GENERATING COMPARATIVE WORD CLOUDS ===")

# Pengaturan Stopwords (Ditambah beberapa kata agar lebih bersih)
stopwords = set(['yang', 'dan', 'di', 'ke', 'dari', 'ini', 'itu', 'aplikasi', 'sudah', 
                'bisa', 'saya', 'nya', 'untuk', 'dengan', 'ada', 'tidak', 'tapi', 
                'kalau', 'jadi', 'karena', 'sama', 'mohon', 'tolong', 'saja', 'buat', 'lagi', 'kok', 'sih'])

# Membuat frame subplot: 1 baris, 3 kolom
fig, axes = plt.subplots(1, 3, figsize=(21, 7))

# Palet warna elegan untuk masing-masing aplikasi (opsional: bisa disamakan semua)
colormaps = ['Blues', 'Greens', 'Purples']

for i, app in enumerate(apps):
    # Mengambil teks ulasan dari dataframe aplikasi terkait
    text = " ".join(all_dfs[i]['cleaned_content'].astype(str))
    
    # Membuat Word Cloud untuk aplikasi ini dengan gaya RAPI
    wordcloud = WordCloud(
        width=800, 
        height=800, 
        background_color='white',
        stopwords=stopwords,
        colormap=colormaps[i],    # Tone warna yang tidak mencolok (elegan)
        max_words=35,             # Dibatasi 35 kata agar tidak sumpek
        prefer_horizontal=0.9     # Membuat 90% kata mendatar agar gampang dibaca
    ).generate(text)
    
    # Menampilkan pada subplot yang sesuai
    axes[i].imshow(wordcloud, interpolation='bilinear')
    # Menggunakan font yang seragam
    axes[i].set_title(f'{app.upper()}', fontsize=24, fontweight='bold', pad=20)
    axes[i].axis('off')

# Mengatur tata letak agar tidak tumpang tindih
plt.tight_layout(pad=3.0)

# Simpan gambar perbandingan dengan kualitas HD (600 DPI)
plt.savefig('wordcloud_comparative_rapi.png', dpi=600, bbox_inches='tight')
plt.show()

print("✅ Selesai! Tabel distribusi muncul di atas.")
print("✅ Gambar Word Cloud komparatif disimpan sebagai 'wordcloud_comparative_rapi.png'")