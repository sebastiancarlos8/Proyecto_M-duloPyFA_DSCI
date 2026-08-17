import streamlit as st
import numpy as np

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Sebastian Carlos")

st.image("Python_logo.png", width = 300)
st.sidebar.image("DMC.png", width = 100)

modulos = st.sidebar.selectbox("Seleccione un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":
  st.write("Bienvenido al módulo de Home")

elif modulos == "Ejercicio 1":
  st.write("Bienvenido al módulo de Ejercicio 1")

elif modulos == "Ejercicio 2":
  st.write("Bienvenido al módulo de Ejercicio 2")

elif modulos == "Ejercicio 3":
  st.write("Bienvenido al módulo de Ejercicio 3")

else:
 st.write("Bienvenido al módulo de Ejercicio 4")
  
