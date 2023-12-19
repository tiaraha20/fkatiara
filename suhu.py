import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
# Header
st.header('Sufiati :sparkles:')
st.subheader('Konversi Suhu')

c1, c2 = st.columns(2)

with c1:
    x = st.number_input('Suhu ', value=100)
    st.write('Dikonversikan ke: ')
with c2:
    satuan = st.selectbox(
        'Satuan',
        ('C', 'F', 'R','K'),key='k1')
    konversi = st.selectbox(
        'Konversi',
        ('C', 'F', 'R','K'),key='k2')

if(satuan=='C'):
   if(konversi=='C'):
      y = x
   elif(konversi=='F'):
      y = x * 9/5 + 32
   elif(konversi=='R'):
      y = x * 4/5
   elif(konversi=='K'):
      y = x + 273
if(satuan=='F'):
   if(konversi=='C'):
      y = (x - 32) * 5/9
   elif(konversi=='F'):
      y = x
   elif(konversi=='R'):
      y = (x - 32) * 4/9
   elif(konversi=='K'):
      y = (x + 32) * 5/9 + 273
if(satuan=='R'):
   if(konversi=='C'):
      y = x * 5/4
   elif(konversi=='F'):
      y = x * 9/4 + 32
   elif(konversi=='R'):
      y = x
   elif(konversi=='K'):
      y = x * 5/4 + 273
if(satuan=='K'):
   if(konversi=='C'):
      y = x - 273
   elif(konversi=='F'):
      y = (x - 273) * 9/5 + 32
   elif(konversi=='R'):
      y = (x - 273) * 4/5
   elif(konversi=='K'):
      y = x

st.write(x,' ',satuan,' = ',y,' ',konversi)

st.caption('Copyright © Sufiati 2023')
