import streamlit as st
import numpy as np

st.sidebar.title("Contenido")
modulos = st.sidebar.selectbox("Seleccione un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":
  st.title("Bienvenido Trabajo Práctico Módulo Python Fundamentals")
  st.image("Python_logo.png", width = 300)
  st.sidebar.image("DMC.png", width = 100)
  st.subheader("Elaborado por:")
  st.write("David Sebastian Carlos Ipanaque")
  st.subheader("Módulo:")
  st.write("Especialización en Python for Analytics")
  st.subheader("Información general:")
  st.write("Información general: Egresado de la carrera de Ingeniería Industrial, con experiencia en análitica de datos dentro del sector retail, consumo masivo y seguros, dentro del área comercial y de recursos humanos")
  st.markdown("2026")

elif modulos == "Ejercicio 1":
  st.write("Bienvenido al módulo de Ejercicio 1")

elif modulos == "Ejercicio 2":
  st.write("Bienvenido al módulo de Ejercicio 2")

elif modulos == "Ejercicio 3":
  st.write("Bienvenido al módulo de Ejercicio 3")

else:
 st.write("Bienvenido al módulo de Ejercicio 4")
  
