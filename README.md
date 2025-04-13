# Proyek Analisis Sentimen Ulasan Aplikasi Google Play Store

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan pengguna aplikasi yang diambil dari Google Play Store. Proses ini meliputi pengambilan data (scraping), pembersihan dan pra-pemrosesan teks, ekstraksi fitur, pelatihan model Machine Learning (SVM, Random Forest) dan Deep Learning (LSTM), evaluasi model, serta implementasi fungsi inferensi untuk memprediksi sentimen ulasan baru.

## Tujuan Proyek

Proyek ini dibuat sebagai bagian dari submission untuk kelas Belajar Pengembangan Machine Learning di Dicoding Indonesia (atau kelas relevan lainnya). Tujuan utamanya adalah untuk mendemonstrasikan pemahaman dan penerapan teknik Natural Language Processing (NLP) untuk analisis sentimen, dengan target **memenuhi seluruh kriteria dan saran untuk mendapatkan penilaian bintang 5**.

## Fitur Utama

- **Scraping Data:** Mengambil ulasan aplikasi dari Google Play Store menggunakan library `google-play-scraper`.
- **Preprocessing Teks:** Membersihkan data teks ulasan (lowercase, hapus URL, tanda baca, angka, dll.) dan menghapus stopwords Bahasa Indonesia menggunakan `nltk`.
- **Pelabelan Sentimen:** Mengklasifikasikan ulasan ke dalam 3 kategori (Positif, Negatif, Netral) berdasarkan rating bintang.
- **Ekstraksi Fitur:** Menggunakan TF-IDF (`scikit-learn`) untuk model ML klasik dan Sequence Padding (`tensorflow.keras.preprocessing`) untuk model Deep Learning.
- **Pelatihan Model:** Melatih dan membandingkan 3 skema model:
  1.  SVM + TF-IDF (Split 80/20)
  2.  Random Forest + TF-IDF (Split 70/30)
  3.  LSTM (Bidirectional) + Embedding Keras (Split 80/20)
- **Evaluasi Model:** Mengevaluasi performa model menggunakan metrik akurasi, classification report, dan confusion matrix.
- **Inference:** Menyediakan fungsi untuk memprediksi sentimen dari teks ulasan baru menggunakan model terbaik yang telah dilatih.

## Struktur Direktori

```
.
├── scraping_google_play.py         # Skrip untuk mengambil data ulasan
├── sentiment_analysis_notebook.ipynb # Notebook utama untuk analisis dan pelatihan
├── requirements.txt                # Daftar library Python yang dibutuhkan
├── hasil_scraping_[APP_ID].csv     # Contoh output data scraping (nama file akan bervariasi)
└── README.md                       # File ini
```

## Persyaratan

- Python 3.8 atau versi lebih baru
- pip (Python package installer)
- Library Python yang tercantum dalam `requirements.txt`

## Instalasi

1.  **Clone Repository (Jika Ada):**

    ```bash
    git clone https://github.com/KillerKing93/Dicoding-Proyek-Analisis-Sentimen
    cd Dicoding-Proyek-Analisis-Sentimen
    ```

2.  **Buat Virtual Environment (Sangat Direkomendasikan):**

    ```bash
    python -m venv venv
    ```

    - **Windows:** `venv\Scripts\activate`
    - **macOS/Linux:** `source venv/bin/activate`

3.  **Instal Dependensi:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Download Data NLTK:**
    Meskipun notebook mencoba mengunduh secara otomatis jika belum ada, Anda bisa mengunduhnya manual:
    ```bash
    python -m nltk.downloader punkt stopwords
    ```

## Penggunaan

Proses terdiri dari dua langkah utama: scraping data dan menjalankan notebook analisis.

### 1. Scraping Data

- Buka file `scraping_google_play.py`.
- **Ubah variabel `APP_ID`** dengan ID aplikasi target Anda di Google Play Store (misal: `com.tokopedia.tkpd`).
- **Sesuaikan variabel `JUMLAH_ULASAN_TARGET`** (minimal 3.000, targetkan >10.000 untuk bintang 5).
- Jalankan skrip dari terminal:
  ```bash
  python scraping_google_play.py
  ```
- Skrip akan menghasilkan file `.csv` (misal: `hasil_scraping_com.tokopedia.tkpd.csv`) yang berisi data ulasan.

### 2. Analisis Sentimen & Pelatihan Model

- Buka file `sentiment_analysis_notebook.ipynb` menggunakan Jupyter Notebook, JupyterLab, Google Colab, atau VS Code dengan ekstensi Jupyter.
- **Pastikan variabel `NAMA_FILE_DATASET`** (di SEL 2) sesuai dengan nama file CSV hasil scraping Anda.
- **Jalankan semua sel notebook secara berurutan** dari atas ke bawah. Notebook ini akan melakukan:
  - Memuat data
  - Membersihkan dan memproses data
  - Melatih dan mengevaluasi 3 skema model (SVM, RF, LSTM)
  - Menampilkan hasil evaluasi (akurasi, report, confusion matrix)
  - Menjalankan fungsi inferensi pada contoh ulasan

### 3. Inference

- Hasil inferensi (prediksi sentimen untuk ulasan baru) dapat dilihat pada output **SEL 8** di dalam notebook `sentiment_analysis_notebook.ipynb`. Output ini berfungsi sebagai bukti penerapan inferensi.

## Target Kriteria Submission (Bintang 5)

Proyek ini dirancang untuk memenuhi kriteria berikut demi mencapai target bintang 5:

1.  ✅ Data merupakan hasil scraping mandiri (`scraping_google_play.py`).
2.  ✅ Melakukan tahapan ekstraksi fitur (TF-IDF, Sequence Padding) dan pelabelan data (3 kelas).
3.  ✅ Menggunakan algoritma pelatihan Machine Learning dan Deep Learning (SVM, RF, **LSTM**).
4.  ✅ Akurasi testing set **minimal 85%** untuk _ketiga_ skema pelatihan.
5.  ✅ **(Saran 1)** Menggunakan algoritma **Deep Learning** (LSTM).
6.  ✅ **(Saran 2)** Akurasi pada **training set dan testing set** untuk model Deep Learning diusahakan **di atas 92%**.
7.  ✅ **(Saran 3)** Dataset memiliki **minimal tiga kelas** (Positif, Negatif, Netral).
8.  ✅ **(Saran 4)** Memiliki jumlah data **minimal 10.000 sampel** (setelah cleaning).
9.  ✅ **(Saran 5)** Melakukan **3 percobaan skema pelatihan** yang berbeda (Variasi: Algoritma, Ekstraksi Fitur, Pembagian Data).
10. ✅ **(Saran 6)** Melakukan **inference** dalam file notebook (`.ipynb`) dengan output kelas kategorikal.

## Hasil Eksperimen (Contoh - Harap Diisi Sesuai Hasil Anda!)

- **Eksperimen 1 (SVM + TF-IDF + 80/20):**
  - Akurasi Test Set: [Isi Akurasi Di Sini]%
- **Eksperimen 2 (Random Forest + TF-IDF + 70/30):**
  - Akurasi Test Set: [Isi Akurasi Di Sini]%
- **Eksperimen 3 (LSTM + Padding + 80/20):**
  - Akurasi Training Set Terbaik: [Isi Akurasi Di Sini]%
  - Akurasi Test Set Terbaik: [Isi Akurasi Di Sini]%

_(Pastikan akurasi Eksperimen 1, 2, dan 3 di Test Set >= 85%. Untuk bintang 5, usahakan Akurasi Training & Test Eksperimen 3 > 92%)_

## Catatan Tambahan

- Hasil akurasi dapat bervariasi tergantung pada aplikasi yang dipilih, jumlah data yang berhasil di-scrape, kualitas preprocessing, dan hyperparameter model. Mungkin diperlukan penyesuaian lebih lanjut untuk mencapai target akurasi.
- Proses scraping dan pelatihan model Deep Learning (terutama dengan data >10.000) dapat memakan waktu dan sumber daya komputasi.
- Pastikan untuk melakukan scraping secara etis dan tidak membebani server Google Play Store.
