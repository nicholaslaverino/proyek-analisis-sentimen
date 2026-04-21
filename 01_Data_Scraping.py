from google_play_scraper import Sort, reviews
import pandas as pd
import numpy as np

# Daftar aplikasi E-Government yang akan di-scrape
apps_to_scrape = {
    'SATUSEHAT': 'com.telkom.tracencare',
    'SIGNAL': 'app.signal.id',
    'IKD': 'gov.dukcapil.mobile_id'
}

# Target jumlah ulasan yang ingin diambil per aplikasi
jumlah_review = 5000

for app_name, app_id in apps_to_scrape.items():
    print(f"Memulai scraping untuk aplikasi: {app_name} ({app_id})...")
    
    try:
        # Proses Scraping Data
        result, continuation_token = reviews(
            app_id,
            lang='id', 
            country='id', 
            sort=Sort.NEWEST, 
            count=jumlah_review, 
            filter_score_with=None 
        )
        
        # Memasukkan hasil scraping ke dalam DataFrame Pandas
        df = pd.DataFrame(np.array(result), columns=['review'])
        df = df.join(pd.DataFrame(df.pop('review').tolist()))
        
        # --- PROSES PENYIMPANAN KE DUA FORMAT ---
        nama_dasar = f"{app_name.lower()}_reviews"
        
        # 1. Simpan ke CSV
        nama_file_csv = f"{nama_dasar}.csv"
        df.to_csv(nama_file_csv, index=False, encoding='utf-8-sig')
        
        # 2. Simpan ke Excel (.xlsx)
        nama_file_excel = f"{nama_dasar}.xlsx"
        df.to_excel(nama_file_excel, index=False)
        
        print(f"✅ Berhasil! Dapatkan {len(df)} ulasan.")
        print(f"   -> Disimpan sebagai: {nama_file_csv} & {nama_file_excel}\n")
        
    except Exception as e:
        print(f"❌ Gagal scraping {app_name}. Error: {e}\n")

print("Semua proses scraping selesai! Silakan cek folder kamu.")