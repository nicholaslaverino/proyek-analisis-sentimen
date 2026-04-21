import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- PENGATURAN FONT PAPER (TIMES NEW ROMAN) ---
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

# --- 1. MASUKKAN ANGKA CONFUSION MATRIX DI SINI ---
# Format: [[True Negative, False Positive], [False Negative, True Positive]]

# Data IndoBERT (KIRI) - Ganti angka ini dengan data aslimu!
cm_indobert = np.array([[560, 70], 
                        [100, 210]])

# Data mBERT (KANAN) - Ini menggunakan data SIGNAL yang asli
cm_mbert = np.array([[569, 73], 
                     [95, 212]])

# --- 2. MEMBUAT CANVAS (1 Baris, 2 Kolom) ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Fungsi pembantu agar tulisan di dalam kotak rapi (ada label TN, FP, dll)
def make_labels(cm):
    group_names = ['TN', 'FP', 'FN', 'TP']
    group_counts = ["{0:0.0f}".format(value) for value in cm.flatten()]
    labels = [f"{v1}\n{v2}" for v1, v2 in zip(group_names, group_counts)]
    return np.asarray(labels).reshape(2,2)

# --- 3. GAMBAR INDOBERT (KIRI) ---
sns.heatmap(cm_indobert, annot=make_labels(cm_indobert), fmt='', cmap='Blues', 
            xticklabels=['Negatif', 'Positif'], yticklabels=['Negatif', 'Positif'], 
            cbar=False, ax=axes[0], annot_kws={"size": 14, "weight": "bold"})

axes[0].set_title('IndoBERT', fontweight='bold', fontsize=16, pad=15)
axes[0].set_xlabel('Tebakan Model', fontweight='bold', labelpad=10, fontsize=12)
axes[0].set_ylabel('Kenyataan (Actual)', fontweight='bold', labelpad=10, fontsize=12)

# --- 4. GAMBAR mBERT (KANAN) ---
sns.heatmap(cm_mbert, annot=make_labels(cm_mbert), fmt='', cmap='Blues', 
            xticklabels=['Negatif', 'Positif'], yticklabels=['Negatif', 'Positif'], 
            cbar=False, ax=axes[1], annot_kws={"size": 14, "weight": "bold"})

axes[1].set_title('mBERT', fontweight='bold', fontsize=16, pad=15)
axes[1].set_xlabel('Tebakan Model', fontweight='bold', labelpad=10, fontsize=12)
axes[1].set_ylabel('') # Sengaja dikosongkan agar y-label tidak dobel dan lebih bersih

# --- 5. SENTUHAN AKHIR & SIMPAN ---
plt.suptitle('Perbandingan Confusion Matrix pada Aplikasi SIGNAL', fontsize=18, fontweight='bold', y=1.05)
plt.tight_layout()

nama_file = 'Komparasi_CM_SIGNAL_HD.png'
plt.savefig(nama_file, dpi=600, bbox_inches='tight')
plt.show()

print(f"✅ Selesai! Gambar siap masuk paper! Silakan download {nama_file}")