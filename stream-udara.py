import pickle
import streamlit as st 

model = pickle.load(open('udara_model.sav', 'rb'))

# Judul
st.title("PREDIKSI KUALITAS STANDAR PENCEMARAN UDARA")
st.header("Tugas UAS Business intelligence")
st.subheader("NENDA PUTRI SUCIATY")
st.subheader("191351065")

col1, col2, = st.columns(2)

with col1:
    pm10 = st.text_input('Partikel debu dalam emisi gas buang (PM10)')
with col2:
    pm25 = st.text_input('Partikel debu dalam emisi gas buang (PM25)')
with col1:
    so2 = st.text_input('Sulfida (SO2)')
with col2:
    co = st.text_input('Carbon Monoksida (CO)')
with col1:
    o3 = st.text_input('Ozon (03)')
with col2:
    no2 = st.text_input('Nitrogen Dioksida (NO2)')

max = st.text_input(
    'Nilai ukur paling tinggi dari seluruh parameter yang diukur dalam waktu yang sama (MAX)')


udara_diagnosis = ''

if st.button('STATUS PENCEMARAN UDARA'):
    udara_prediction = model.predict([[pm10, pm25, so2, co, o3, no2, max]])

    if (udara_prediction[0]==0):
        udara_diagnosis = 'STATUS TIDAK SEHAT'

    elif (udara_prediction[0]==1):
        udara_diagnosis = 'STATUS SEDANG'

    else:
        udara_diagnosis = 'STATUS BAIK'

st.success(udara_diagnosis)
