import streamlit as st
import numpy as np

st.sidebar.image("DMC.png", width = 100)
st.sidebar.title("Contenido")
modulos = st.sidebar.selectbox("Seleccione un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":
  st.title("Trabajo Práctico - Módulo Python Fundamentals")
  st.image("Python_logo.png", width = 500)
  st.subheader("Módulo: Especialización en Python for Analytics")
  st.write("**Año:** 2026")
  st.subheader("Elaborado por")
  st.write("**Nombre completo:** David Sebastian Carlos Ipanaque")
  st.subheader("Información general")
  st.markdown("""Egresado de la carrera de Ingeniería Industrial, con experiencia en análitica de datos en el sector retail, consumo masivo y seguros, dentro del área comercial y de recursos humanos. \nApasionado por la lógica, recursos humanos, uso de datos masivos y programación.""")
  st.subheader("Descripción del proyecto")
  st.markdown("""Portafolio de ejercicios que muestran los conocimientos aplicados en Python, mediantes casuísticas de la vida cotidiana que implique el uso respecto a listas, registros con NumPy, arrays, DataFrame, librerías externas y clases.""")
  st.subheader("Tecnologías utilizadas")
  st.markdown("""""")
  
elif modulos == "Ejercicio 1":
  st.title("Bienvenido al módulo de Ejercicio 1 – Flujo de caja con listas")

  # -------------------------
  # Registro del movimiento
  # -------------------------
  
  st.session_state.flujos = []

  Concepto = st.text_input("Concepto")
  Tipo = st.selectbox("Tipo de movimiento",["Ingreso","Gasto"])
  Monto = st.number_input("Monto",min_value=0.0, step = 0.01, format="%.2f")
  
  if st.button("Registrar movimiento"):

    flujo = {
      "Concepto": Concepto,
      "Tipo": Tipo,
      "Monto": Monto
    }

    st.session_state.flujos.append(flujo)

    st.success("Movimiento registrado de manera correcta")

  # -------------------------
  # Cálculos
  # -------------------------

  total_ingresos = sum(
    flujo["monto"]
    for flujo in st.session_state.movimientos
    if flujo["tipo"] == "Ingreso"
  )

  total_gastos = sum(
    flujo["monto"]
    for flujo in st.session_state.movimientos
    if flujo["tipo"] == "Gasto"
  )

  saldo_final = total_ingresos - total_gastos

  
  st.subheader("Flujo de caja")

  st.subheader("Resumen")

  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric("Total ingresos", f"S/ {total_ingresos:.2f}")

  with col2:
      st.metric("Total gastos", f"S/ {total_gastos:.2f}")

  with col3:
      st.metric("Saldo final", f"S/ {saldo_final:.2f}")


  for flujo in st.session_state.flujos:
    st.write(
      f"**{flujo['Concepto']}** | "
      f"{flujo['Tipo']} | "
      f"S/ {flujo['Monto']:.2f}"
    )


elif modulos == "Ejercicio 2":
  st.write("Bienvenido al módulo de Ejercicio 2 – Registro con NumPy, arrays y DataFrame")

elif modulos == "Ejercicio 3":
  st.write("Bienvenido al módulo de Ejercicio 3 – Uso de funciones desde una librería externa")

else:
 st.write("Bienvenido al módulo de Ejercicio 4 – Uso de clases desde una librería externa con CRUD")
  
