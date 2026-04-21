import pandas as pd
import re

# 1. Kamus Slang (Kata Gaul) sederhana
slang_dict = {
    "yg": "yang", "gk": "tidak", "gak": "tidak", "nggak": "tidak",
    "tdk": "tidak", "udah": "sudah", "sdh": "sudah", "bgt": "banget",
    "krn": "karena", "karna": "karena", "dgn": "dengan", "tp": "tapi",
    "kalo": "kalau", "klo": "kalau", "klow": "kalau", "jd": "jadi",
    "dr": "dari", "sy": "saya", "aq": "saya", "gw": "saya",
    "km": "kamu", "lu": "kamu", "elo": "kamu", "dpt": "dapat",
    "bs": "bisa", "bisaa": "bisa", "tks": "terima kasih", "thx": "terima kasih",
    "trims": "terima kasih", "apk": "aplikasi", "apps": "aplikasi",
    "blm": "belum", "udh": "sudah", "aja": "saja", "saja": "saja",
    "sama": "sama", "msh": "masih", "dlm": "dalam", "utk": "untuk",
    "pake": "pakai", "pakek": "pakai", "bangettt": "banget"
}

# 2. Fungsi untuk membersihkan teks
def clean_text(text):
    if type(text) != str:
        return ""
    
    text = text.lower() # Case folding (huruf kecil)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE) # Hapus URL
    text = re.sub(r'[^\w\s]', '', text) # Hapus tanda baca dan emoji
    text = re.sub(r'\d+', '', text) # Hapus angka
    
    # Normalisasi Slang
    words = text.split()
    cleaned_words = [slang_dict.get(word, word) for word in words]
    text = ' '.join(cleaned_words)
    
    # Hapus spasi berlebih
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 3. Fungsi untuk pelabelan berdasarkan rating (score)
def label_sentiment(score):
    if score in [1, 2]:
        return 'Negatif'
    elif score in [4, 5]:
        return 'Positif'
    else:
        return 'Netral' # Bintang 3 akan kita drop nanti

# Daftar file yang akan diproses
apps = ['satusehat', 'signal', 'ikd']

for app in apps:
    print(f"Memproses data {app.upper()}...")
    
    try:
        # Baca file CSV hasil scraping
        df = pd.read_csv(f"{app}_reviews.csv")
        
        # Ambil hanya kolom yang dibutuhkan
        df = df[['content', 'score']].copy()
        
        # Terapkan fungsi pelabelan
        df['sentiment'] = df['score'].apply(label_sentiment)
        
        # Buang ulasan bintang 3 (Netral) dan ulasan yang kosong
        df = df[df['sentiment'] != 'Netral']
        df = df.dropna(subset=['content'])
        
        # Terapkan pembersihan teks
        df['cleaned_content'] = df['content'].apply(clean_text)
        
        # Buang baris yang teksnya jadi kosong setelah dibersihkan
        df = df[df['cleaned_content'] != ""]
        
        # --- PROSES PENYIMPANAN ---
        
        # 1. Simpan ke CSV
        nama_file_csv = f"{app}_cleaned_reviews.csv"
        df.to_csv(nama_file_csv, index=False, encoding='utf-8-sig')
        
        # 2. Simpan ke Excel (.xlsx)
        nama_file_xlsx = f"{app}_cleaned_reviews.xlsx"
        df.to_excel(nama_file_xlsx, index=False)
        
        print(f"✅ Berhasil! Data disimpan ke:")
        print(f"   - {nama_file_csv}")
        print(f"   - {nama_file_xlsx}")
        
        # Tampilkan ringkasan jumlah label
        print(df['sentiment'].value_counts())
        print("-" * 30)
        
    except FileNotFoundError:
        print(f"❌ File {app}_reviews.csv tidak ditemukan. Pastikan sudah di-scrape!\n")
    except Exception as e:
        print(f"❌ Terjadi kesalahan pada {app}: {e}\n")

print("Seluruh proses Prapemrosesan Data Selesai!")