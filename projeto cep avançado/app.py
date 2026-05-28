import streamlit as st
from ferramentas import buscar_cep
import pandas as pd

st.sidebar.title("CEP location")
st.sidebar.image("logo.png")
cep = st.sidebar.text_input("digite o cep que deseja consultar: ")

if st.sidebar.button("consultar"):
   dados = buscar_cep(cep)
   lat = float(dados.get("lat"))
   lng = float(dados .get("lng"))

   cordenadas = pd.DataFrame({"latitude":[lat], "longitude":[lng]})
   st.map(cordenadas, zoom=15,color="#5CFF5C3E")


   st.json(dados) 

    
      