# Impor library yang dibutuhkan
import pandas as pd
from google_play_scraper import reviews, Sort
import json
import time  # Untuk memberi jeda jika diperlukan
from tqdm import tqdm

# --- Konfigurasi Scraping ---
# Ganti dengan ID aplikasi target di Google Play Store
# Contoh: Tokopedia: com.tokopedia.tkpd
#         Shopee: com.shopee.id
#         Gojek: com.gojek.app
APP_ID = 'com.tokopedia.tkpd'  # <<< GANTI INI SESUAI TARGET ANDA

# Jumlah ulasan yang ingin diambil (targetkan > 10.000 untuk bintang 5)
JUMLAH_ULASAN_TARGET = 50000  # <<< SESUAIKAN TARGET ANDA

# Nama file output
NAMA_FILE_OUTPUT = f'hasil_scraping_{APP_ID}.csv'

print(f"Memulai scraping ulasan untuk aplikasi: {APP_ID}")
print(f"Target jumlah ulasan: {JUMLAH_ULASAN_TARGET}")

try:
    # Inisialisasi variabel untuk menyimpan ulasan dan token kelanjutan
    semua_ulasan = []
    token = None
    batch_size = 100  # jumlah ulasan per iterasi

    # Membuat progress bar dengan total target ulasan
    with tqdm(total=JUMLAH_ULASAN_TARGET, desc="Scraping ulasan") as pbar:
        while True:
            # Ambil batch ulasan
            result, token = reviews(
                APP_ID,
                lang='id',           # Bahasa ulasan (Indonesia)
                country='id',        # Negara (Indonesia)
                sort=Sort.NEWEST,    # Urutkan berdasarkan terbaru
                count=batch_size,
                continuation_token=token
            )
            semua_ulasan.extend(result)
            pbar.update(len(result))
            
            # Jika sudah mencapai atau melebihi target atau tidak ada token lagi, berhenti
            if token is None or len(semua_ulasan) >= JUMLAH_ULASAN_TARGET:
                break

    # Potong jika ulasan yang didapat melebihi target
    if len(semua_ulasan) > JUMLAH_ULASAN_TARGET:
        print(f"Mengambil {len(semua_ulasan)} ulasan, memotong menjadi {JUMLAH_ULASAN_TARGET}.")
        semua_ulasan = semua_ulasan[:JUMLAH_ULASAN_TARGET]
    elif len(semua_ulasan) < 3000:
        print(f"PERINGATAN: Hanya berhasil mendapatkan {len(semua_ulasan)} ulasan.")
        print("Pastikan aplikasi target memiliki cukup ulasan atau coba lagi.")

    print(f"Berhasil mendapatkan {len(semua_ulasan)} ulasan.")

    # Konversi ke DataFrame Pandas
    df_ulasan = pd.DataFrame(semua_ulasan)

    # Pilih kolom yang relevan saja (misalnya: userName, score, at, content)
    df_final = df_ulasan[['userName', 'score', 'at', 'content']]

    # Simpan ke file CSV
    df_final.to_csv(NAMA_FILE_OUTPUT, index=False, encoding='utf-8-sig')  # utf-8-sig agar kompatibel Excel

    print(f"Data berhasil disimpan ke file: {NAMA_FILE_OUTPUT}")

except Exception as e:
    print(f"Terjadi kesalahan saat scraping: {e}")
    print("Pastikan ID Aplikasi benar dan koneksi internet stabil.")
