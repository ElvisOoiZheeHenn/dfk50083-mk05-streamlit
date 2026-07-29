import streamlit as st
import pandas as pd
from datetime import date

# =========================================================
#  KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(page_title="Profil Elvis", page_icon="👤", layout="wide")

# =========================================================
#  BAHAGIAN SUSUN ATUR: SIDEBAR (st.sidebar)
# =========================================================
st.sidebar.title("🧭 Menu Navigasi")
menu = st.sidebar.radio(
    "Pilih bahagian:",
    ["Profil", "Kalkulator BMI", "Kalkulator Umur"]
)

st.sidebar.markdown("---")
mood = st.sidebar.selectbox(
    "Mood anda hari ini?",
    ["😀 Ceria", "😌 Tenang", "😴 Penat", "🔥 Bersemangat"]
)
st.sidebar.info(f"Mood dikesan: {mood}")


# =========================================================
#  1) BAHAGIAN PROFIL
# =========================================================
if menu == "Profil":
    st.title("👋 Selamat Datang ke Profil Saya")
    st.header("Elvis Ooi Zhee Henn")

    # Susun atur menggunakan Kolum (st.columns)
    col1, col2 = st.columns([1, 2])

    with col1:
        # Gantikan URL ini dengan gambar anda sendiri,
        # atau letak fail 'profile.jpg' dan tukar kepada:  st.image("profile.jpg")
        st.image("profile.jpeg", width=250)

    with col2:
        st.subheader("Pengenalan Diri")
        st.write(
            """
            Hai! Nama saya **Elvis**. Saya seorang pelajar
            **Diploma Teknologi Maklumat** di Politeknik Tuanku Syed
            Sirajuddin (PTSS), Perlis.

            - 🎓 **Bidang Pengajian:** Teknologi Maklumat
            - 💻 **Minat:** Pembangunan web & aplikasi mudah alih
            - 🎌 **Hobi:** Belajar Bahasa Jepun, menonton anime,
              dan membuat projek pengaturcaraan
            """
        )

    st.markdown("---")

    # Elemen visual: carta bar tahap kemahiran
    st.subheader("📊 Tahap Kemahiran Saya")
    data = pd.DataFrame(
        {
            "Kemahiran": ["Python", "PHP", "JavaScript", "MySQL", "Bahasa Jepun"],
            "Tahap (%)": [50, 50, 50, 50, 80],
        }
    ).set_index("Kemahiran")
    st.bar_chart(data)


# =========================================================
#  2) BAHAGIAN INTERAKTIF - KALKULATOR BMI
# =========================================================
elif menu == "Kalkulator BMI":
    st.title("⚖️ Kalkulator BMI")
    st.write("Masukkan berat dan tinggi anda untuk mengira Indeks Jisim Badan (BMI).")

    col1, col2 = st.columns(2)
    with col1:
        berat = st.number_input(
            "Berat badan (kg)", min_value=1.0, max_value=300.0, value=60.0, step=0.5
        )
    with col2:
        tinggi = st.number_input(
            "Tinggi (cm)", min_value=50.0, max_value=250.0, value=165.0, step=0.5
        )

    # Logik: beri output berdasarkan input pengguna
    if st.button("Kira BMI"):
        tinggi_m = tinggi / 100
        bmi = berat / (tinggi_m ** 2)
        st.metric("BMI anda", f"{bmi:.1f}")

        if bmi < 18.5:
            st.warning("Kategori: **Kurang berat badan** 🥗")
        elif bmi < 25:
            st.success("Kategori: **Berat badan normal** ✅")
        elif bmi < 30:
            st.warning("Kategori: **Berlebihan berat badan** ⚠️")
        else:
            st.error("Kategori: **Obesiti** 🚨")


# =========================================================
#  BAHAGIAN INTERAKTIF - KALKULATOR UMUR
# =========================================================
elif menu == "Kalkulator Umur":
    st.title("🎂 Kalkulator Umur")
    st.write("Pilih tarikh lahir anda, dan sistem akan mengira umur anda.")

    tarikh_lahir = st.date_input(
        "Tarikh lahir",
        value=date(2004, 1, 1),
        min_value=date(1950, 1, 1),
        max_value=date.today(),
    )

    # Logik: beri output berdasarkan input pengguna
    if st.button("Kira Umur"):
        hari_ini = date.today()
        umur = (
            hari_ini.year
            - tarikh_lahir.year
            - ((hari_ini.month, hari_ini.day) < (tarikh_lahir.month, tarikh_lahir.day))
        )
        st.success(f"Umur anda ialah **{umur} tahun**. 🎉")
        st.balloons()