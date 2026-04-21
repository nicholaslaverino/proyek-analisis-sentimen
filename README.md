\# Code-Mixed Sentiment Analysis in Indonesian E-Government



Repository ini berisi source code dan dataset untuk penelitian: \*\*"Code-Mixed Sentiment Analysis in Indonesian E-Government: A Controlled Benchmark of Monolingual vs Multilingual Transformers"\*\*. 



Penelitian ini mengevaluasi kinerja model Transformer monolingual (IndoBERT) dan multilingual (mBERT) dalam mengklasifikasikan sentimen ulasan publik pada tiga aplikasi layanan digital pemerintah di Indonesia (SATUSEHAT, SIGNAL, dan IKD). Fokus utama penelitian ini adalah menangani fenomena \*code-mixing\* (perpaduan bahasa Indonesia informal dengan istilah teknis bahasa Inggris) menggunakan pendekatan \*controlled benchmarking\*.



\## 📂 Struktur Repository



Alur kerja (\*pipeline\*) dalam repository ini dibagi menjadi 5 tahapan utama yang dapat dijalankan secara berurutan:



\* \*\*`01\_Data\_Scraping.py`\*\* : Script untuk melakukan ekstraksi ulasan pengguna dari Google Play Store menggunakan library `google-play-scraper`.

\* \*\*`02\_Preprocessing\_and\_Cleaning.py`\*\* : Script untuk membersihkan data, melakukan \*case folding\*, dan menormalisasi bahasa \*slang\* Indonesia tanpa menerjemahkan istilah \*code-mixed\* (seperti 'error', 'bug', 'login') untuk menjaga konteks aslinya.

\* \*\*`03\_WordCloud\_Exploration.py`\*\* : Script untuk menghasilkan visualisasi Word Cloud guna mengidentifikasi kemunculan kata-kata teknis asing yang dominan pada masing-masing aplikasi.

\* \*\*`04\_Model\_Finetuning\_IndoBERT\_mBERT.ipynb`\*\* : Notebook eksperimen utama untuk melakukan \*fine-tuning\* pada model pre-trained `indobenchmark/indobert-base-p1` dan `bert-base-multilingual-cased`.

\* \*\*`05\_Evaluation\_and\_Confusion\_Matrix.py`\*\* : Script untuk mengevaluasi performa model menggunakan metrik F1-Score, Precision, Recall, Accuracy, dan menghasilkan visualisasi \*Confusion Matrix\*.



\## 📊 Dataset



Dataset yang digunakan dalam penelitian ini disimpan dalam folder `dataset/` (jika tersedia secara publik).

\* `raw\_dataset.csv` : Hasil ekstraksi asli dari Google Play Store (total 14.204 ulasan).

\* `cleaned\_dataset.csv` : Dataset yang telah diproses dan siap digunakan untuk pelatihan model.



\*(Catatan: Dataset disediakan untuk keperluan reproduksi akademis. Jika file tidak tersedia karena batasan ukuran GitHub, silakan hubungi penulis untuk akses).\*



\## 🚀 Cara Menjalankan (How to Run)



1\. Lakukan \*clone repository\* ini:

&#x20;  ```bash

&#x20;  git clone \[https://github.com/username-kamu/nama-repo-kamu.git](https://github.com/username-kamu/nama-repo-kamu.git)

&#x20;  cd nama-repo-kamu

