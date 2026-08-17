import streamlit as st
import numpy as np

st.sidebar.image("DMC.png", width = 100)
st.sidebar.title("Contenido")
modulos = st.sidebar.selectbox("Seleccione un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":
  st.title("Trabajo Práctico - Módulo Python Fundamentals")
  st.image("Python_logo.png", width = 500)
  st.subheader("Módulo: Especialización en Python for Analytics")
  st.subheader("Elaborado por")
  st.write("**Nombre completo:** David Sebastian Carlos Ipanaque")
  st.write("**Año:** 2026")
  st.subheader("Información general")
  st.markdown("""Egresado de la carrera de Ingeniería Industrial, con experiencia en análitica de datos en el sector retail, consumo masivo y seguros, dentro del área comercial y de recursos humanos. \nApasionado por la lógica, datos y programación""")
  st.subheader("Descripción del proyecto")
  
elif modulos == "Ejercicio 1":
  st.write("Bienvenido al módulo de Ejercicio 1")

elif modulos == "Ejercicio 2":
  st.write("Bienvenido al módulo de Ejercicio 2")

elif modulos == "Ejercicio 3":
  st.write("Bienvenido al módulo de Ejercicio 3")

else:
 st.write("Bienvenido al módulo de Ejercicio 4")
  
