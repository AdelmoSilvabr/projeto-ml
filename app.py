import streamlit as st
import pandas as pd
# from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Qual o tamanho da pizza desejado?")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com o tamnho de {diametro: .0f} é de R$ {preco_previsto: .2f}")