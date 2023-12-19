import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
# Header
st.header('Grafik Sinus & Cosinus :sparkles:')
st.subheader('Plot Grafik')

nama =st.text_input('Nama', ' ', label_visibility='collapsed')
st.write('Hallo ',nama)

f1 =st.number_input('f1 = ',value=1)
f2 =st.number_input('f2 = ',value=1)
st.write('Frekuensi plot sinus adalah ',f1)
st.write('Frekuensi plot cosinus adalah ',f2)

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
y = np.sin(f1*x)  # Calculating sin(x) values
z = np.cos(f2*x)  # Calculating sin(x) values
 
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b')  # Plotting sin(x) curve
ax.plot(x, z, label='cos(x)', color='c')  # Plotting sin(x) curve
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)
 
# subheader
st.subheader("Plot Sin & Cos")
 
col1, col2 = st.columns(2)
 
with col1:
    st.caption('Sin')
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
    y = np.sin(f1*x)  # Calculating sin(x) values
 
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(x, y, label='sin(x)', color='b')  # Plotting sin(x) curve
    ax.set_ylabel("Sin x")
    ax.set_xlabel("x")
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    ax.tick_params(axis='x', labelsize=15)
 
    st.pyplot(fig)
 
with col2:
    st.caption('Cos')
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
    y = np.cos(f2*x)  # Calculating sin(x) values
 
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(x, y, label='cos(x)', color='c')  # Plotting cos(x) curve
    ax.set_ylabel("Cos x")
    ax.set_xlabel("x")
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    ax.tick_params(axis='x', labelsize=15)
 
    st.pyplot(fig)  
 
st.caption('Copyright © Tiara Hanifah Anwar 2023')
