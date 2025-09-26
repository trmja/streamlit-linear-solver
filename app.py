import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="📘")

st.title("📘 Resolver Ecuaciones de Primer Grado")

# Generar coeficientes aleatorios para ax + b = c con solución entera
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.x = random.randint(-10, 10)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b

a = st.session_state.a
b = st.session_state.b
c = st.session_state.c
solucion = st.session_state.x

st.write(f"Resuelve la ecuación: **{a}x + {b} = {c}**")

respuesta = st.number_input("Tu respuesta para x:", step=1, format="%d")

if st.button("Verificar"):
    if respuesta == solucion:
        st.success("✅ ¡Correcto! Bien hecho.")
        st.balloons()
        # Generar nueva ecuación automáticamente
        st.session_state.a = random.randint(1, 10)
        st.session_state.x = random.randint(-10, 10)
        st.session_state.b = random.randint(-10, 10)
        st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b
    else:
        st.error("❌ Incorrecto. Intenta de nuevo.")
