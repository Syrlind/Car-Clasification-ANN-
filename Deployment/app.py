import streamlit as st
import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Stanislaus Kanopi Johan Trielianto ')
    st.write('Batch     : FTDS HCK 10 ')
    st.write('G7        : Mengidentifikasi jenis jenis mobil  mengunakan model CNN  ')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Di Graded challange ini saya memilih dataset multiclass dimana kita akan menebak jenis jenis mobil berdasarkan dataset yang diberikan  ')

    with st.expander("Kesimpulan"):
        st.caption('Model ini masih sangat jauh dari sempurna ,saya rasa masih banyak  hal yang bisa di improve ,seperti arsitek ann ,dan mungkin mengunakan transfer learning  . ')


else:
     models.run()