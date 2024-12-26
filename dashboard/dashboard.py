import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Sidebar untuk input
st.sidebar.title("Menu Proyek")
st.sidebar.markdown("### Pilih Opsi:")
menu = st.sidebar.selectbox(
    "Pilih Halaman",
    ("Informasi Proyek", "Data Wrangling", "Visualisasi", "Analisis Lanjut")
)

# Menampilkan informasi proyek
if menu == "Informasi Proyek":
    st.title("Proyek Analisis Data: Bike Sharing Dataset")
    st.markdown("- **Nama:** Haydar Fahri Alaudin")
    st.markdown("- **Email:** haidaralaudin0@gmail.com")
    st.markdown("- **ID Dicoding:** HAYDAR FAHRI ALAUDIN")

# Mengimpor dataset
@st.cache_data
def load_data():
    # Ganti dengan path yang sesuai untuk dataset Anda
    day_df = pd.read_csv('https://raw.githubusercontent.com/HaydarFahri/bike_sharing_dicoding/refs/heads/main/dashboard/main_data_day.csv')
    hour_df = pd.read_csv('https://raw.githubusercontent.com/HaydarFahri/bike_sharing_dicoding/refs/heads/main/dashboard/main_data_hour.csv')
    return day_df, hour_df

day_df, hour_df = load_data()

# Pembersihan data (dilakukan di awal sehingga dapat digunakan di seluruh kode)
day_df_cleaned = day_df.drop(columns=['instant'], errors='ignore')
hour_df_cleaned = hour_df.drop(columns=['instant'], errors='ignore')

# Menghapus duplikasi jika ada
day_df_cleaned = day_df_cleaned.drop_duplicates()
hour_df_cleaned = hour_df_cleaned.drop_duplicates()

# Data Wrangling
if menu == "Data Wrangling":
    st.header("Data Wrangling")

    # Menampilkan beberapa baris awal dari masing-masing dataset
    st.subheader("Beberapa Baris Pertama dari Dataset 'day.csv'")
    st.write(day_df.head())

    st.subheader("Beberapa Baris Pertama dari Dataset 'hour.csv'")
    st.write(hour_df.head())

    # Menilai informasi dasar dari dataset 'day.csv'
    st.subheader("Informasi Dasar dari Dataset 'day.csv'")
    st.write(day_df.info())

    # Statistik deskriptif dari dataset 'day.csv'
    st.subheader("Statistik Deskriptif dari Dataset 'day.csv'")
    st.write(day_df.describe())

    # Menilai informasi dasar dari dataset 'hour.csv'
    st.subheader("Informasi Dasar dari Dataset 'hour.csv'")
    st.write(hour_df.info())

    # Statistik deskriptif dari dataset 'hour.csv'
    st.subheader("Statistik Deskriptif dari Dataset 'hour.csv'")
    st.write(hour_df.describe())

    # Mengecek nilai yang hilang dalam dataset 'day.csv'
    missing_day = day_df.isnull().sum()
    st.subheader("Jumlah Nilai yang Hilang di Dataset 'day.csv'")
    st.write(missing_day[missing_day > 0])

    # Mengecek nilai yang hilang dalam dataset 'hour.csv'
    missing_hour = hour_df.isnull().sum()
    st.subheader("Jumlah Nilai yang Hilang di Dataset 'hour.csv'")
    st.write(missing_hour[missing_hour > 0])

# Visualisasi
if menu == "Visualisasi":
    # Visualisasi distribusi jumlah total pengguna (cnt) dalam dataset 'day.csv'
    st.header("Visualisasi Distribusi Jumlah Total Pengguna (cnt) per Hari")
    plt.figure(figsize=(12, 6))
    counts, bin_edges = np.histogram(day_df_cleaned['cnt'], bins=30)

    for i in range(len(counts)):
        plt.bar(bin_edges[i], counts[i], width=bin_edges[i + 1] - bin_edges[i], 
                color='lightblue', alpha=0.5, edgecolor='black', linewidth=1.5)

    max_count = counts.max()
    max_bin_index = np.argmax(counts)

    plt.bar(bin_edges[max_bin_index], 
             counts[max_bin_index], 
             width=bin_edges[max_bin_index + 1] - bin_edges[max_bin_index], 
             color='darkblue', alpha=0.7, edgecolor='black', linewidth=1.5, label='Balok Tertinggi')

    plt.title('Distribusi Jumlah Total Pengguna (cnt) per Hari')
    plt.xlabel('Jumlah Total Pengguna')
    plt.ylabel('Frekuensi')
    plt.axvline(max_count, color='red', linestyle='--', linewidth=2, label='Jumlah Pengguna Tertinggi')
    plt.legend()
    plt.grid()
    st.pyplot(plt)

    # Visualisasi hubungan antara suhu dan kelembapan dengan garis tren
    st.header("Hubungan antara Suhu dan Kelembapan")
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=day_df_cleaned, x='temp', y='hum', hue='weathersit', palette='viridis', alpha=0.7)
    sns.regplot(data=day_df_cleaned, x='temp', y='hum', scatter=False, color='red', line_kws={'linewidth': 2})
    plt.title('Hubungan antara Suhu dan Kelembapan')
    plt.xlabel('Suhu (normalisasi)')
    plt.ylabel('Kelembapan')
    plt.legend(title='Situasi Cuaca')
    plt.grid()
    st.pyplot(plt)

    # Boxplot untuk melihat variasi jumlah penyewa berdasarkan musim
    st.header("Variasi Jumlah Penyewa berdasarkan Musim")
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=day_df_cleaned, x='season', y='cnt')
    plt.title('Variasi Jumlah Penyewa berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewa')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Musim Dingin', 'Musim Semi', 'Musim Panas', 'Musim Gugur'])
    plt.grid()
    st.pyplot(plt)

    # Heatmap untuk melihat korelasi antara variabel
    st.header("Heatmap Korelasi antara Variabel")
    plt.figure(figsize=(12, 8))
    numeric_cols = day_df_cleaned.select_dtypes(include=[np.number])
    correlation_matrix = numeric_cols.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Heatmap Korelasi antara Variabel')
    st.pyplot(plt)
