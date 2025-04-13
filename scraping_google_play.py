# Impor library yang dibutuhkan
import pandas as pd
from google_play_scraper import reviews, Sort, reviews_all
import json
import time # Untuk memberi jeda jika diperlukan

# --- Konfigurasi Scraping ---
# Ganti dengan ID aplikasi target di Google Play Store
# Contoh: Tokopedia: com.tokopedia.tkpd
#         Shopee ID: com.shopee.id
#         Gojek: com.gojek.app
APP_ID = 'com.tokopedia.tkpd' # <<< GANTI INI SESUAI TARGET ANDA

# Jumlah ulasan yang ingin diambil (targetkan > 10.000 untuk bintang 5)
JUMLAH_ULASAN_TARGET = 15000 # <<< SESUAIKAN TARGET ANDA

# Nama file output
NAMA_FILE_OUTPUT = f'hasil_scraping_{APP_ID}.csv'

print(f"Memulai scraping ulasan untuk aplikasi: {APP_ID}")
print(f"Target jumlah ulasan: {JUMLAH_ULASAN_TARGET}")

try:
    # Menggunakan reviews_all untuk mengambil semua ulasan (lebih mudah)
    # Perhatikan: Ini bisa memakan waktu lama dan mengambil banyak data
    # Opsi lain: Gunakan reviews() dalam loop dengan continuation_token jika perlu kontrol lebih
    print("Menggunakan reviews_all (mungkin memakan waktu)...")
    result = reviews_all(
        APP_ID,
        lang='id',           # Bahasa ulasan (Indonesia)
        country='id',        # Negara (Indonesia)
        sort=Sort.NEWEST,    # Urutkan berdasarkan terbaru (atau MOST_RELEVANT)
        count=JUMLAH_ULASAN_TARGET # Batas jumlah (reviews_all mungkin mengabaikan ini dan ambil semua)
    )

    # Jika reviews_all mengembalikan lebih dari target, potong manual
    if len(result) > JUMLAH_ULASAN_TARGET:
        print(f"Mengambil {len(result)} ulasan, memotong menjadi {JUMLAH_ULASAN_TARGET}.")
        result = result[:JUMLAH_ULASAN_TARGET]
    elif len(result) < 3000: # Pastikan minimal 3000 terpenuhi
         print(f"PERINGATAN: Hanya berhasil mendapatkan {len(result)} ulasan.")
         print("Pastikan aplikasi target memiliki cukup ulasan atau coba lagi.")
         # Anda bisa menghentikan script di sini jika mau: exit()

    print(f"Berhasil mendapatkan {len(result)} ulasan.")

    # Konversi ke DataFrame Pandas
    df_ulasan = pd.DataFrame(result)

    # Pilih kolom yang relevan saja (misalnya: userName, score, at, content)
    # 'content' adalah teks ulasan, 'score' adalah rating bintang
    df_final = df_ulasan[['userName', 'score', 'at', 'content']]

    # Simpan ke file CSV
    df_final.to_csv(NAMA_FILE_OUTPUT, index=False, encoding='utf-8-sig') # utf-8-sig agar kompatibel Excel

    print(f"Data berhasil disimpan ke file: {NAMA_FILE_OUTPUT}")

except Exception as e:
    print(f"Terjadi kesalahan saat scraping: {e}")
    print("Pastikan ID Aplikasi benar dan koneksi internet stabil.")