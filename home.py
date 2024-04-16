import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pickle
import math

LOGO_IMAGE = "./MJ-logo-vertical.png"
#Disable Warning
st.set_option('deprecation.showPyplotGlobalUse', False)
#Set Size
sns.set(rc={'figure.figsize':(8,8)})
#read data
data = pd.read_excel("./apbdesok.xlsx")
#Coloring
colors_1 = ['#66b3ff','#99ff99']
colors_2 = ['#66b3ff','#99ff99']
colors_3 = ['#79ff4d','#4d94ff']
colors_4 = ['#ff0000','#ff1aff']
st.markdown(
    f"""
    <div style="text-align: center;">
    <img class="logo-img" src="data:png;base64,{base64.b64encode(open(LOGO_IMAGE, 'rb').read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: #FFFFFF; font-family:sans-serif'>Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #FFFFFF; font-family:sans-serif'>Laporan Keuangan Desa Manud Jaya</h2>", unsafe_allow_html=True)
menu = st.sidebar.selectbox("Select Menu", ("Dashboard", "Unduh Data","Tanya Data")) 
st.sidebar.image("./MJ-logo-only.png", width=120)
if menu == "Dashboard":
    st.write("Menu Dashboard")
    tahun = st.sidebar.selectbox("Pilih Tahun",(2022,2023,2024))
    if tahun == 2022:
        data_2022 = data[data.Tahun == 2022]
        fig1 = px.pie(data_2022[data_2022['Jenis'] == 'Pendapatan'], values='Anggaran', names='Uraian', title='Pendapatan per Jenis Sumbernya')
        st.plotly_chart(fig1, use_container_width=True)
        fig2 = px.pie(data_2022[data_2022['Jenis'] == 'Belanja'], values='Anggaran', names='Uraian', title='Belanja per Jenis Belanja')
        st.plotly_chart(fig2, use_container_width=True)
    if tahun == 2023:
        data_2023 = data[data.Tahun == 2023]
        fig1 = px.pie(data_2023[data_2023['Jenis'] == 'Pendapatan'], values='Anggaran', names='Uraian', title='Pendapatan per Jenis Sumbernya')
        st.plotly_chart(fig1, use_container_width=True)
        fig2 = px.pie(data_2023[data_2023['Jenis'] == 'Belanja'], values='Anggaran', names='Uraian', title='Belanja per Jenis Belanja')
        st.plotly_chart(fig2, use_container_width=True)
    if tahun == 2024:
        data_2024 = data[data.Tahun == 2024]
        fig1 = px.pie(data_2024[data_2024['Jenis'] == 'Pendapatan'], values='Anggaran', names='Uraian', title='Pendapatan per Jenis Sumbernya')
        st.plotly_chart(fig1, use_container_width=True)
        fig2 = px.pie(data_2024[data_2024['Jenis'] == 'Belanja'], values='Anggaran', names='Uraian', title='Belanja per Jenis Belanja')
        st.plotly_chart(fig2, use_container_width=True)
if menu == 'Unduh Data':
    st.write('Unduh Data')
    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    tahun_unduh = st.selectbox("Pilih Tahun",(2022,2023,2024))
    if tahun_unduh == 2022:
        data_unduh = data[data.Tahun == 2022]
        csv = convert_df(data_unduh)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='data_apbdes.csv',
            mime='text/csv',
        )
    if tahun_unduh == 2023:
        data_unduh = data[data.Tahun == 2023]
        csv = convert_df(data_unduh)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='data_apbdes.csv',
            mime='text/csv',
        )
    if tahun_unduh == 2024:
        data_unduh = data[data.Tahun == 2024]
        csv = convert_df(data_unduh)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='data_apbdes.csv',
            mime='text/csv',
        )
