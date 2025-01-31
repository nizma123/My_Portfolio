import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv(r"C:\Users\nizma\OneDrive\Desktop\Proyek Analisis Data - Dicoding\submission\dashboard\day.csv")

# Mengganti nama kolom agar mudah dibaca untuk dataframe day_df
day_df.rename(columns = {'dteday': 'dateday', 'yr': 'year', 'mnth': 'month', 'weathersit': 'weather_situation', 'hum': 'humidity', 'cnt': 'count'}, inplace = True)

# Mengkonversi isi kolom agar mudah dipahami
# Konversi kolom 'season' menjadi: 1:Spring, 2: Summer, 3:Fall, 4:Winter
day_df['season'] = day_df['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: ' Winter'})

# Konversi kolom 'month' menjadi: 1:Jan, 2:Feb, 3:Mar, 4:Apr, 5:May, 6:Jun, 7:Jul, 8:Aug, 9:Sep, 10:Oct, 11:Nov, 12:Dec
day_df['month'] = day_df['month'].replace({1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'})

# Konversi kolom 'weather_situation' menjadi: 1: Clear/Partly Cloudy, 2: Mist/Cloudy, 3:Light Snow/Rain, 4: Heavy Rain/Snow
day_df['weather_situation'] = day_df['weather_situation'].replace({1: 'Clear/Partly Cloudy', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'})

# Konversi kolom 'weekday' menjadi: 0: Sun, 1: Mon, 2: Tue, 3: Wed, 4: Thu, 5: Fri, 6: Sat
day_df['weekday'] = day_df['weekday'].replace({0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'})

# Konversi kolom 'year' menjadi: 0: 2011, 1: 2012
day_df['year'] = day_df['year'].replace({0: '2011', 1: '2012'})

# Mengatur urutan bulan
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day_df['month'] = pd.Categorical(day_df['month'], categories=month_order, ordered=True)

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_years = st.sidebar.multiselect("Pilih Tahun:", day_df['year'].unique(), default=day_df['year'].unique())
selected_seasons = st.sidebar.multiselect("Pilih Musim:", day_df['season'].unique(), default=day_df['season'].unique())
selected_weather = st.sidebar.multiselect("Pilih Kondisi Cuaca:", day_df['weather_situation'].unique(), default=day_df['weather_situation'].unique())

# Filter dataset berdasarkan pilihan
filtered_df = day_df[(day_df['year'].isin(selected_years)) &
                      (day_df['season'].isin(selected_seasons)) &
                      (day_df['weather_situation'].isin(selected_weather))]

# Dashboard Title
st.title("📊 Dashboard Penyewaan Sepeda 🚲")

# Checkbox untuk memilih visualisasi
if st.checkbox("📈 Tampilkan Tren Penyewaan Sepeda per Bulan & Tahun"):
    monthly_counts = filtered_df.groupby(['month', 'year']).agg({'count': 'sum'}).reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(data=monthly_counts, x='month', y='count', hue='year', marker='o', palette='rocket')
    ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Bulan dan Tahun")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    st.pyplot(fig)

if st.checkbox("🌦️ Tampilkan Pengaruh Musim terhadap Penyewaan Sepeda"):
    seasonal_users = filtered_df.groupby('season').agg({'registered': 'sum', 'casual': 'sum'}).reset_index()
    fig, ax = plt.subplots()
    ax.bar(seasonal_users['season'], seasonal_users['registered'], label='Registered', color='tab:green')
    ax.bar(seasonal_users['season'], seasonal_users['casual'], label='Casual', color='tab:orange')
    ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.legend()
    st.pyplot(fig)

if st.checkbox("🌤️ Tampilkan Pengaruh Cuaca terhadap Penyewaan Sepeda"):
    fig, ax = plt.subplots()
    sns.barplot(x='weather_situation', y='count', data=filtered_df, ax=ax)
    ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    st.pyplot(fig)

if st.checkbox("📅 Tampilkan Penyewaan Sepeda Berdasarkan Hari Kerja dan Libur"):
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 12))
    sns.barplot(x='workingday', y='count', data=filtered_df, ax=axes[0])
    axes[0].set_title("Penyewaan Sepeda pada Hari Kerja")
    sns.barplot(x='holiday', y='count', data=filtered_df, ax=axes[1])
    axes[1].set_title("Penyewaan Sepeda pada Hari Libur")
    sns.barplot(x='weekday', y='count', data=filtered_df, ax=axes[2])
    axes[2].set_title("Penyewaan Sepeda pada Hari dalam Seminggu")
    plt.tight_layout()
    st.pyplot(fig)

if st.checkbox("👥 Tampilkan Perbandingan Pengguna Terdaftar vs Kasual"):
    total_casual = filtered_df['casual'].sum()
    total_registered = filtered_df['registered'].sum()
    fig, ax = plt.subplots()
    ax.pie([total_casual, total_registered], labels=['Casual', 'Registered'], autopct='%1.1f%%', colors=['#B2FFFF', '#00CED1'])
    ax.set_title("Perbandingan Pengguna Terdaftar dan Kasual")
    st.pyplot(fig)

# Button untuk Menampilkan Ringkasan Data
if st.button("Tampilkan Ringkasan Data"):
    st.write(filtered_df.describe())

# Footer
st.markdown("📌 **Dashboard ini dibuat menggunakan Streamlit untuk menganalisis pola penyewaan sepeda berdasarkan berbagai faktor.**")