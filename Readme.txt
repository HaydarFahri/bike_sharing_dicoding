Proyek Analisis Data: Tren Penyewaan Sepeda – Mengkaji Pengaruh Suhu dan Hari Libur pada Pengguna Kasual 🚴‍♂️

Proyek ini bertujuan untuk mengeksplorasi faktor-faktor yang memengaruhi penyewaan sepeda, termasuk musim dengan jumlah penyewaan tertinggi, pengaruh suhu terhadap penyewaan harian dan per jam, serta dampak kondisi cuaca terhadap total penyewaan sepeda. Analisis dilakukan melalui visualisasi bar plot, scatter plot, dan line plot untuk mengidentifikasi pola dan hubungan yang signifikan.

Fitur Utama 🚀

Pertanyaan Bisnis
Proyek ini fokus pada dua pertanyaan utama:
- Bagaimana pengaruh musim terhadap jumlah total pengguna (cnt) yang menggunakan sepeda?
- Apa pola penggunaan sepeda berdasarkan jam dalam sehari, dan bagaimana faktor cuaca mempengaruhi jumlah pengguna pada jam-jam tertentu?

Import Data & Wrangling
Proses pemuatan, penilaian, dan pembersihan data dilakukan secara bertahap, termasuk penghapusan kolom yang tidak diperlukan seperti `instant`.

Exploratory Data Analysis (EDA)
Bertujuan untuk mengeksplorasi faktor-faktor yang memengaruhi penyewaan sepeda, termasuk musim dengan jumlah penyewaan tertinggi, pengaruh suhu terhadap penyewaan harian dan per jam, serta dampak kondisi cuaca terhadap total penyewaan sepeda. Visualisasi dilakukan menggunakan bar plot, scatter plot, dan line plot untuk mengidentifikasi pola dan hubungan signifikan.

Regresi Linear
Melakukan analisis regresi linear untuk memodelkan hubungan antara suhu dan jumlah penyewa sepeda harian.

Visualisasi Interaktif
Menggunakan **Streamlit** untuk menghasilkan visualisasi dan analisis interaktif.

Struktur Proyek 📂


Cara Menjalankan Proyek 💻

1. Menjalankan Jupyter Notebook
Untuk menjalankan analisis di **Jupyter Notebook**:
1. Pastikan semua dependensi sudah terpasang dengan perintah berikut:
   ```bash
   pip install -r requirements.txt
Jalankan Jupyter Notebook:

bash
Copy code
jupyter notebook notebook.ipynb
Menjalankan Dasbor Streamlit Proyek ini juga menyediakan dashboard interaktif menggunakan Streamlit. Ikuti langkah berikut untuk menjalankannya:

Instal semua dependensi menggunakan:

bash
Copy code
pip install -r requirements.txt
Jalankan aplikasi Streamlit:

bash
Copy code
streamlit run dashboard.py
Insight Utama 📊

Bagaimana Pengaruh Musim terhadap Jumlah Total Pengguna (cnt) yang Menggunakan Sepeda?
Analisis menunjukkan bahwa musim memiliki dampak signifikan terhadap jumlah penyewa sepeda. Musim panas mencatatkan jumlah penyewa tertinggi, dengan aktivitas penyewaan yang sangat tinggi pada hari-hari cerah dan hangat. Hal ini menunjukkan meningkatnya minat masyarakat untuk berolahraga dan bersantai di luar ruangan selama cuaca yang baik.
Musim semi juga menunjukkan rata-rata jumlah penyewa yang cukup tinggi.
Musim gugur mencatatkan penurunan jumlah penyewa dibandingkan dengan dua musim sebelumnya, namun tetap mempertahankan tingkat penyewaan yang layak.
Sebaliknya, musim dingin mencatat jumlah pengguna terendah. Suhu yang sangat dingin, kemungkinan salju, dan kondisi cuaca yang tidak nyaman membuat orang lebih memilih moda transportasi lain.
Apa Pola Penggunaan Sepeda Berdasarkan Jam dalam Sehari, dan Bagaimana Faktor Cuaca Mempengaruhi Jumlah Pengguna pada Jam-jam Tertentu?
Analisis pola penggunaan sepeda berdasarkan jam dalam sehari menunjukkan bahwa jam-jam sibuk terjadi terutama antara pagi dan sore. Peningkatan signifikan dalam jumlah penyewa pada jam-jam ini konsisten dengan pola aktivitas harian masyarakat, di mana banyak orang menggunakan sepeda untuk pergi bekerja, sekolah, atau aktivitas luar ruangan lainnya.
Jam puncak pagi dan sore mencerminkan pola perjalanan umum, di mana pengguna lebih cenderung menyewa sepeda saat menuju atau pulang dari pekerjaan. Analisis ini penting untuk memahami kapan permintaan penyewaan sepeda berada di puncaknya.
Dataset Dataset yang digunakan dalam proyek ini adalah:

day.csv: Dataset harian yang mencatat data penyewaan sepeda termasuk informasi tentang suhu, kondisi cuaca, dan status hari libur.
hour.csv: Dataset per jam yang mencatat data penyewaan sepeda per jam, memberikan detail yang lebih spesifik terkait waktu.
Library yang Digunakan

Python: Bahasa pemrograman yang digunakan untuk analisis dan visualisasi data.
Streamlit: Library Python untuk membuat aplikasi web interaktif.
Matplotlib & Seaborn: Digunakan untuk visualisasi data.
Pandas: Pustaka sumber terbuka yang digunakan untuk analisis dan manipulasi data.
